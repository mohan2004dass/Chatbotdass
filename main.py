import streamlit as st

st.title("chat bot")

command = st.chat_input("how can i help you")

if command:
    with st.chat_message("USER"):
        st.write(command)
    if "hello" in command:
        with st.chat_message("bot")