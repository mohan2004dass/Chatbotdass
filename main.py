import streamlit as st
import google.generativeai as genai


genai.configure(api_key=st.secrets["gemini_api"])
def ai(txt):
    
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("from now your a helpful assistence, reply to this in skillful : "+txt)
    return response.text




st.title("Mohandass Ai Assistant")

command = st.chat_input("Hello! there")

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
    elif "What is your name" in command:
         with st.chat_message("BOT"):
            st.write("I am Dass ")
            st.session_state.message.append({"role":"BOT","message":"I am Dass"})
    elif "age" in command:
        with st.chat_message("BOT"):
            st.write("I am 20ty ")
            st.session_state.message.append({"role":"BOT","message":"I am 20ty"})
    elif "where are you from" in command:
         with st.chat_message("BOT"):
            st.write("I am from arupukottai ")
            st.session_state.message.append({"role":"BOT","message":"I am from arupukottai"})  
    elif "where are you currently living" in command:
         with st.chat_message("BOT"):
            st.write("I am currently living in Bangalore")
            st.session_state.message.append({"role":"BOT","message":"I am currently living in Bangalore"})
    elif "what is date of birth of mohandass" in command:
        with st.chat_message("BOT"):
            st.write("his dob is 21.07.2004 ")
            st.session_state.message.append({"role":"BOT","message":"his dob is 21.07.2004 "})
    elif "when mohandass born and age " in command:
        with st.chat_message("BOT"):
            st.write("His dob is 21.07.2004 and the age is 20ty ")
            st.session_state.message.append({"role":"BOT","message":"his dob is 21.07.2004 and the age is 20ty "})
    elif "who" in command:
        with st.chat_message("BOT"):
            st.write("Im Mohandass ")
            st.session_state.message.append({"role":"BOT","message":"Im Mohandass MCA student! "})
    elif "have you eaten" in command:
        with st.chat_message("BOT"):
            st.write("yea! im full thanks for your concern ")
            st.session_state.message.append({"role":"BOT","message":"yea! im full thanks for your concern "})
    else:
        with st.chat_message("BOT"):
            data = ai(command)
            st.write(data)
            st.session_state.message.append({"role":"BOT","message":data})




print(st.session_state.message)
