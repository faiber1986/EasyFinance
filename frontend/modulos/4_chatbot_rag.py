import streamlit as st
import requests
from utils import load_css, render_footer
from i18n import t

# 1. Aplicar estilos globales al inicio
load_css()

st.header(t("chatbot_header"))
st.caption(t("chatbot_caption"))

# Inicializar historial de chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensajes previos
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input del usuario
if prompt := st.chat_input(t("chatbot_input_placeholder")):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Llamada al Backend
    with st.chat_message("assistant"):
        with st.spinner(t("chatbot_spinner")):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/api/ia/consultar",
                    json={"mensaje": prompt},
                    timeout=30  # Los agentes RAG pueden tardar un poco más
                )

                if response.status_code == 200:
                    respuesta_ia = response.json()["respuesta"]
                    st.markdown(respuesta_ia)
                    st.session_state.messages.append({"role": "assistant", "content": respuesta_ia})
                else:
                    st.error(f"Error {response.status_code}: {response.text}")
            except Exception as e:
                st.error(f"{t('chatbot_conn_error')} {e}")

    # 3. Renderizar el footer al final de la página
    render_footer()
