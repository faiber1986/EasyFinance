import streamlit as st
import requests
from utils import load_css, render_footer

# 1. Aplicar estilos globales al inicio
load_css()

st.header("Asesor Financiero Pro (RAG + Math)")
st.caption("Consultas basadas en normatividad técnica y cálculos exactos.")

# Inicializar historial de chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensajes previos
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input del usuario
if prompt := st.chat_input("¿En qué puedo asesorarte hoy?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Llamada al Backend
    with st.chat_message("assistant"):
        with st.spinner("Consultando base de conocimientos y modelos..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/api/ia/consultar",
                    json={"mensaje": prompt},
                    timeout=30 # Los agentes RAG pueden tardar un poco más
                )
                
                if response.status_code == 200:
                    respuesta_ia = response.json()["respuesta"]
                    st.markdown(respuesta_ia)
                    st.session_state.messages.append({"role": "assistant", "content": respuesta_ia})
                else:
                    st.error(f"Error {response.status_code}: {response.text}")
            except Exception as e:
                st.error(f"No se pudo conectar con el agente: {e}")
    
    # 3. Renderizar el footer al final de la página
    render_footer()

