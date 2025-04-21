🌟 Smart Voice and Text Assistant
This project provides a smart assistant with both voice and text input capabilities, built with a web-based interface using Flask, JavaScript, and Tailwind CSS. The assistant leverages the Web Speech API for voice recognition and integrates with Ollama for natural language processing, supporting Persian (Farsi) conversations.
📑 Table of Contents

📖 Project Overview
⚙️ Installation
📚 Usage
🔬 Algorithm Explanation
🔢 Examples
🤝 Contributing
📄 License
💖 Donation

📖 Project Overview
The Smart Voice and Text Assistant is designed to facilitate natural language interactions in Persian. Users can interact via text input or voice commands, with conversation history stored in a SQLite database. The assistant supports multiple language models (e.g., Llama 3, Mistral, Gemma) through Ollama, with a customizable server URL for flexibility.
⚙️ Installation
To run this project, you need Python 3.x, a web browser, and optionally Ollama for local language model inference. Check your Python version by running:
python --version

Install Dependencies
Install the required Python dependencies using pip:
pip install flask flask-cors requests

Install Ollama (Optional for Local Model Inference)
Ollama is used to run language models locally. Follow the instructions for your operating system:
Windows

Download the Ollama installer from Ollama's official website.
Run the installer and follow the prompts to install Ollama.
Open a terminal (e.g., Command Prompt or PowerShell) and pull a model (e.g., Llama 3):ollama pull llama3


Start the Ollama server:ollama run llama3



Linux

Install Ollama using the provided script:curl https://ollama.ai/install.sh | sh


Pull a model (e.g., Llama 3):ollama pull llama3


Start the Ollama server:ollama run llama3



For more details, visit the Ollama documentation.
Clone the Repository
Clone the repository using Git:
git clone https://github.com/your-username/smart-assistant.git
cd smart-assistant

📚 Usage
The program provides a web-based interface for interacting with the assistant. To start the application, run the Flask server:
python app.py

Open a web browser and navigate to http://localhost:5000 to access the interface.
Features

Text Input: Type messages in Persian and receive responses.
Voice Input: Use the microphone to send voice commands (requires browser support for Web Speech API).
Conversation History: View and manage past conversations.
Model Selection: Choose from available models (e.g., Llama 3, Mistral, Gemma).
Theme Toggle: Switch between light and dark themes.

Example Output
The interface displays:

A chat window with user and assistant messages.
A sidebar showing conversation history with timestamps and model details.
Real-time voice transcription during recording.
Plots or visualizations (if integrated) for specific queries.

🔬 Algorithm Explanation
The assistant operates using the following components:

Frontend:

Built with HTML, Tailwind CSS, and JavaScript.
Uses the Web Speech API for voice recognition (SpeechRecognition interface).
Manages conversation history and UI updates dynamically.


Backend:

Flask server handles API requests (/api/chat, /api/conversations, etc.).
SQLite database stores conversation metadata and messages.
Integrates with Ollama for language model inference.


Processing:

User input (text or voice) is sent to the Flask backend.
The backend constructs a prompt with system instructions (e.g., respond in Persian) and conversation history.
Ollama processes the prompt and returns a response, which is stored and displayed.



🔢 Examples
The assistant can handle various interactions. Below are example inputs and their expected outputs:

Text Input: "سلام، امروز هوا怎么样 است؟"
Output: "سلام! برای اطلاع از وضعیت هوا، لطفاً شهر خود را مشخص کنید."


Voice Input: "یک شعر کوتاه بگو"
Output: "البته! این یک شعر کوتاه است:در آسمان دل، ستاره می‌درخشد،عشق در قلب، همیشه می‌پیچد."


Text Input: "Calculate 2 + 2"
Output: "نتیجه محاسبه: ۴"


Voice Input: "تاریخ امروز چیست؟"
Output: "امروز ۲۰ آوریل ۲۰۲۵ است."


Text Input: "Switch to English and say hello"
Output: "Hello!"



Each interaction is saved in the conversation history, accessible via the sidebar.
🤝 Contributing
Contributions are welcome! If you have suggestions for improvements or additional features, please fork the repository and create a pull request. Ensure your code follows the project's coding style and includes tests where applicable.
📄 License
This project is licensed under the MIT License. See the LICENSE file for details.
💖 Donation
If you found this project helpful, consider making a donation:
<a href="https://nowpayments.io/donation?api_key=REWCYVC-A1AMFK3-QNRS663-PKJSBD2&source=lk_donation&medium=referral" target="_blank"> <img src="https://nowpayments.io/images/embeds/donation-button-black.svg" alt="Crypto donation button by NOWPayments"> </a>
