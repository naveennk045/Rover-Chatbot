import streamlit as st
import sys
import os
import time
from groq import InternalServerError

# Add the directory containing Models to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from Models.Llama import prompt

# Streamlit app setup
st.title("💬 Rover")
st.caption("🚀 A Streamlit chatbot powered by the Meta Llama")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I assist you today?"}]

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User input
if prompt_text := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt_text})
    st.chat_message("user").write(prompt_text)
    
    # Placeholder for assistant's response
    assistant_placeholder = st.chat_message("assistant")
    typing_effect_placeholder = assistant_placeholder.empty()

    try:
        # Get response from Llama model
        response = prompt(prompt_text)
        
        # Typewriter effect: reveal text one letter at a time
        typed_text = ""
        for char in response:
            typed_text += char
            typing_effect_placeholder.write(typed_text)
            # time.sleep(0.01)  # Adjust typing speed here
        
        st.session_state.messages.append({"role": "assistant", "content": response})

    except InternalServerError:
        e = "Try Again"
        st.exception(e)
        typing_effect_placeholder.write(e)
