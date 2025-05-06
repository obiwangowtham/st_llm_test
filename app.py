import streamlit as st
from openai import OpenAI
f = open('keys.txt','r') 
OPENAI_API_KEY = f.read().strip()
client = OpenAI(api_key=OPENAI_API_KEY)

st.title(" AI Chatbot")
st.chat_message("assistant").write("Hi, How may I help you?")
if "messages" not in st.session_state:
    st.session_state["messages"] = []


for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg['content'])

user_input = st.chat_input("Ask something about Data science/AI")
if user_input:
    st.chat_message("user").write(user_input)
    response = client.chat.completions.create(model = "gpt-3.5-turbo",
                                             messages=[{"role":"system",
                                                        "content":"""You are know to be polite and helpful AI BOT. Act as a teaching assistant for a Data Science course working with 
                                                        edtech. Your job here is to help students resolve there doubts regarding specific data science topics. if there doubt is not relevant to data science you can politely ask the 
                                                        user for another doubt."""}] + st.session_state["messages"] + [{"role":"user","content": user_input}])
    
    st.chat_message("assistant").write(response.choices[0].message.content) 
    st.session_state["messages"].append({"role":"user", "content":user_input})
    st.session_state["messages"].append({"role":"assistant","content":response.choices[0].message.content}) 
    # Clear Chat Button
if st.button("🗑️ Clear Chat"):
    st.session_state["messages"] = []
