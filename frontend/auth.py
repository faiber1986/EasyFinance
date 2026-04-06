import streamlit as st

def init_session():
    """Inicializa el estado de autenticación."""
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.session_state.user = None

def authenticate_user(email, password):
    """
    Validación de credenciales.
    TODO: Reemplazar con validación real (ej. auth.sign_in_with_email_and_password de Pyrebase).
    """
    # Mock para desarrollo
    if email == "admin@riesgos.com" and password == "admin123":
        st.session_state.authenticated = True
        st.session_state.user = email
        return True
    return False

def logout():
    st.session_state.authenticated = False
    st.session_state.user = None

