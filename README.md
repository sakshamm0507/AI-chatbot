# Gemini Chatbot with Content Filtering


This project is a Python-based chatbot that uses Google's **Gemini API** to generate responses to user queries. It includes a **content filtering mechanism** to detect and block inappropriate queries or responses. If a user enters an inappropriate query, the chatbot will notify the user and skip generating a response. Similarly, if the generated response is inappropriate, it will not be displayed.

---

## 🚀 Features

- **Interactive Chatbot**: Users can interact with the chatbot in real-time.
- **Content Filtering**: Detects and blocks inappropriate queries or responses using the Gemini API.
- **Streaming Responses**: Responses are streamed chunk by chunk for a smooth user experience.
- **Exit Command**: Users can type `"exit"` to end the chat session.

---

## 🛠️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/gemini-chatbot.git
   cd gemini-chatbot

2. Install the required Python library:
   ```bash
   pip install google-generativeai

3. Set Up Your Gemini API Key
   Obtain your Gemini API Key from Google AI Studio.
   Open the chatbot.py file in a text editor.
   Replace "your-gemini-api-key" with your actual Gemini API key. For example:
   ```bash
   Api_key = "sfsdfsd-fghdh2fd"

