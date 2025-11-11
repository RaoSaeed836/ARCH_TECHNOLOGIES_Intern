# 🤖 Chatbot using Ollama and Streamlit

This project is a simple AI-powered chatbot built using **Ollama** as the backend model and **Streamlit** for the frontend interface. It allows users to interact with a local **Large Language Model (LLM)** in real time through a browser.

---

## 🧠 Project Overview

The chatbot takes user input from the Streamlit interface, sends it to the Ollama model, and displays the model’s generated response back to the user. It demonstrates how to integrate a **local LLM (like Gemma, Llama, etc.)** with a **Streamlit app** for conversational AI.

---

## 📂 Project Structure
project-folder/
│
├── Backend.py # Handles Ollama model communication
├── frontend.py # Streamlit app (user interface)
└── README.md # Project documentation


---

## ⚙️ Requirements

Make sure you have installed the following before running the project:

- Python 3.10+
- Streamlit
- Ollama

---

## 📦 Installation Steps

1. Clone or download this repository to your local machine.
2. Open terminal inside the project folder.
3. Install the required libraries:

   ```bash
   pip install streamlit ollama
4. Make sure Ollama is running:
   ollama serve
5. Pull your preferred model (for example gemma3:1b):
   ollama pull gemma3:1b
🚀 How to Run
Run the Streamlit frontend using:
streamlit run frontend.py
Then open the link shown in the terminal:
💡 Key Features

✅ Real-time chat interface using Streamlit
✅ Backend powered by Ollama LLM
✅ Conversation memory within the session
✅ Simple and beginner-friendly structure

🛠️ How It Works

1.User types a message in Streamlit chat input.

2.The message is passed to the get_response() function in Backend.py.

3.Backend communicates with the Ollama model and retrieves a response.

4.The chatbot displays the reply and stores both user and assistant messages in session history.
