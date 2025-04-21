from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.static_folder = 'static'
CORS(app)

# Database setup
def init_db():
    conn = sqlite3.connect('chat_history.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS conversations 
                 (id TEXT, user_id TEXT, title TEXT, model TEXT, timestamp TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS messages 
                 (conversation_id TEXT, sender TEXT, content TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message')
    conversation_id = data.get('conversation_id')
    user_id = data.get('user_id', 'default_user')
    model = data.get('model', 'llama3')
    host = data.get('host', 'http://localhost:11434')

    conn = sqlite3.connect('chat_history.db')
    c = conn.cursor()
    c.execute("INSERT INTO messages (conversation_id, sender, content) VALUES (?, ?, ?)",
              (conversation_id, 'user', message))
    
    c.execute("SELECT sender, content FROM messages WHERE conversation_id = ? ORDER BY timestamp LIMIT 5",
              (conversation_id,))
    history = [{'role': row[0], 'content': row[1]} for row in c.fetchall()]
    
    # اضافه کردن پرامپت سیستمی برای اطمینان از پاسخ به فارسی
    system_prompt = (
        "You are a helpful assistant that responds in Persian (Farsi). "
        "Always answer in Persian, regardless of the language of the input, unless explicitly asked to use another language. "
        "If the user asks to switch languages, follow their instructions accurately.\n"
    )
    context = "\n".join([f"{msg['role']}: {msg['content']}" for msg in history])
    full_prompt = f"{system_prompt}\n{context}\nuser: {message}\nassistant:"
    
    try:
        response = requests.post(f"{host}/api/generate", json={
            'model': model,
            'prompt': full_prompt,
            'stream': False
        })
        response.raise_for_status()
        ollama_response = response.json().get('response', 'No response received.')
        
        c.execute("INSERT INTO messages (conversation_id, sender, content) VALUES (?, ?, ?)",
                  (conversation_id, 'assistant', ollama_response))
        conn.commit()
        conn.close()
        
        return jsonify({'response': ollama_response})
    except requests.exceptions.RequestException as e:
        conn.close()
        return jsonify({'error': f'Ollama error: {str(e)}'}), 500

@app.route('/api/conversations', methods=['GET'])
def get_conversations():
    user_id = request.args.get('user_id', 'default_user')
    conn = sqlite3.connect('chat_history.db')
    c = conn.cursor()
    c.execute("SELECT id, title, model, timestamp FROM conversations WHERE user_id = ?", (user_id,))
    conversations = [{'id': row[0], 'title': row[1], 'model': row[2], 'timestamp': row[3]} for row in c.fetchall()]
    conn.close()
    return jsonify({'conversations': conversations})

@app.route('/api/conversation/<conversation_id>', methods=['GET'])
def get_conversation(conversation_id):
    conn = sqlite3.connect('chat_history.db')
    c = conn.cursor()
    c.execute("SELECT sender, content FROM messages WHERE conversation_id = ? ORDER BY timestamp", (conversation_id,))
    messages = [{'role': row[0], 'content': row[1]} for row in c.fetchall()]
    conn.close()
    return jsonify({'messages': messages})

@app.route('/api/conversation', methods=['POST'])
def create_conversation():
    data = request.json
    user_id = data.get('user_id', 'default_user')
    conversation_id = data.get('conversation_id')
    title = data.get('title', 'New Conversation')
    model = data.get('model', 'llama3')
    
    conn = sqlite3.connect('chat_history.db')
    c = conn.cursor()
    c.execute("INSERT INTO conversations (id, user_id, title, model, timestamp) VALUES (?, ?, ?, ?, ?)",
              (conversation_id, user_id, title, model, datetime.now().isoformat()))
    conn.commit()
    conn.close()
    
    return jsonify({'conversation_id': conversation_id})

@app.route('/api/conversation/<conversation_id>', methods=['DELETE'])
def delete_conversation(conversation_id):
    conn = sqlite3.connect('chat_history.db')
    c = conn.cursor()
    c.execute("DELETE FROM messages WHERE conversation_id = ?", (conversation_id,))
    c.execute("DELETE FROM conversations WHERE id = ?", (conversation_id,))
    conn.commit()
    conn.close()
    return jsonify({'success': True})

@app.route('/')
def serve_frontend():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
