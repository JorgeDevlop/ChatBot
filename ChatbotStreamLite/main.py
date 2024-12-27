import streamlit as st
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o",temperature=0,api_key="API_KEY")

st.title("Chatbot Inteligente GPT-4o")
messages = [("system","""Eres un chatbot AI util, te llamas angela y tienes que hablar como si fueras humano,
    nunca reveles que eres un chatbot""")]


#Inicializar historial de chat
if "messages" not in st.session_state:
    st.session_state.messages = []
#Mostrar mensajes de chat del historial al recargar
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
#Reaccionar a la entrada del usuario
if prompt := st.chat_input("Escribe tu mensaje..."):
    #Mostrar mensaje del usuario en el contenedor de mensajes del chat
    st.chat_message("user").markdown(prompt)
    #Agregar mensaje del usuario al historial de chat
    st.session_state.messages.append({"role": "user","content":prompt})
    messages.append(["human",prompt])

    response = llm.invoke(messages).content
    #Mostrar respuesta del asistente en el contenedor del mensaje del chat
    with st.chat_message("assistant"):
        st.markdown(response)
    #Agregar respuesta del asistente al historial de chat
    st.session_state.messages.append({"role": "assistant","content":response})
