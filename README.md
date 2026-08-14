# 🤖 Gemini Personal Chatbot

A simple AI-powered personal chatbot built with **Python** and **Google Gemini 2.5 Flash**.

This project demonstrates how to integrate Google's Gemini API into a Python application and build a conversational AI assistant with persistent conversation context during a session.

## 🚀 Features

* 🤖 AI-powered conversations using Gemini 2.5 Flash
* 💬 Interactive command-line chatbot
* 🧠 Maintains conversation context during the session
* ⚡ Fast responses using Gemini 2.5 Flash
* 🛡️ Basic error handling
* 🐍 Built completely with Python
* 🔌 Simple Gemini API integration
* 🚪 Exit command for safely closing the application

## 🛠️ Tech Stack

| Technology        | Purpose                   |
| ----------------- | ------------------------- |
| Python            | Core programming language |
| Google Gemini API | AI / LLM                  |
| Gemini 2.5 Flash  | Generative AI model       |
| Google GenAI SDK  | API integration           |

## 📁 Project Structure

```text
gemini-personal-chatbot/
│
├── chatbot.py
├── requirements.txt
├── .gitignore
├── README.md
└── LICENSE
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/gemini-personal-chatbot.git
```

### 2. Open the project

```bash
cd gemini-personal-chatbot
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Gemini API key

Open `chatbot.py` and replace:

```python
API_KEY = "YOUR_GEMINI_API_KEY"
```

with your own Gemini API key.

> ⚠️ Never upload your real API key to GitHub.

### 5. Run the chatbot

```bash
python chatbot.py
```

## 💬 Example

```text
🤖 Gemini Personal Chatbot
Type 'exit' to stop.

You: Hello

Bot: Hello! How can I help you today?

You: What is machine learning?

Bot: Machine learning is a branch of artificial intelligence...

You: Explain Python in simple words.

Bot: Python is a programming language known for its simple and readable syntax.

You: exit

Bot: Goodbye! 👋
```

## 🧠 How It Works

The application creates a Gemini client using the Google GenAI SDK.

The user enters a message through the terminal:

```text
User → Python Application → Gemini API → AI Response
```

The chatbot uses **Gemini 2.5 Flash** to generate responses.

A system instruction defines the chatbot's personality and response style.

## 🔄 Conversation Flow

```text
                ┌──────────────────┐
                │      User        │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │  Python Chatbot  │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │  Gemini 2.5      │
                │      Flash       │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │   AI Response    │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │      User        │
                └──────────────────┘
```

## 🎯 Learning Objectives

This project was created to understand:

* Generative AI fundamentals
* Large Language Model APIs
* Gemini API integration
* Python API development
* Conversational AI
* Prompt/system instructions
* Error handling
* Basic AI application architecture

## 🔮 Future Improvements

The project can be extended with:

* 🎤 Voice input
* 🔊 Text-to-speech
* 🖥️ Graphical user interface
* 🧠 Long-term conversation memory
* 📄 PDF/document analysis
* 🌐 Web search
* 📝 Personal notes
* ⏰ Reminder system
* 💻 System automation
* 🔐 Secure environment-variable API management

## 👨‍💻 Author

**LazyDeveloper TechEd**

AI & Machine Learning | Python | Generative AI | Software Development

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

## 📄 License

This project is licensed under the MIT License.
