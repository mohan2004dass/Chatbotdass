import streamlit as st
import google.generativeai as genai


genai.configure(api_key=st.secrets["gemini_api"])
def ai(txt):
    
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("from now your name is Mohandass and your a Student pursuing a bca Datascience, im a future data scientist and reply to this in short: "+txt)
    return response.text




st.title("Mohandass Ai Assistant")

command = st.chat_input("ena thala?")

if "message" not in st.session_state:
    st.session_state.message = []

for chat in st.session_state.message:
    with st.chat_message(chat["role"]):
        st.write(chat["message"])


if command:
    with st.chat_message("USER"):
        st.write(command)
        st.session_state.message.append({"role":"USER","message":command})
    if "hello" in command:
        with st.chat_message("BOT"):
            st.write("Hi What brings you here? ")
            st.session_state.message.append({"role":"BOT","message":"What brings you here?"})
    elif "who" in command:
        with st.chat_message("BOT"):
            st.write("Im Mohandass ")
            st.session_state.message.append({"role":"BOT","message":"Im Mohandass "})
    else:
        with st.chat_message("BOT"):
            data = ai(command)
            st.write(data)
            st.session_state.message.append({"role":"BOT","message":data})




print(st.session_state.message)
