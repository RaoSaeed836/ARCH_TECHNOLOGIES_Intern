import streamlit as st
from Backend import get_response   # 👈 changed function name

st.set_page_config(page_title="Chat with Ollama", layout="centered")
st.title("🤖 Chatbot using Ollama")

# Initialize message history
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# Display previous chat messages
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

# User input
user_input = st.chat_input("Type your message here...")

if user_input:
    # User message
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)

    # Assistant reply
    bot_reply = get_response(user_input)   # 👈 fixed name
    st.session_state['message_history'].append({'role': 'assistant', 'content': bot_reply})
    with st.chat_message('assistant'):
        st.text(bot_reply)
