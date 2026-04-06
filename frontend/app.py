import streamlit as st
from auth import init_session, authenticate_user, logout
from utils import load_css, render_footer

# 1. Configuración base
st.set_page_config(page_title="Easy Finance", layout="wide", page_icon="📈")

# 2. Carga global de estilos y sesión
load_css()
init_session()

# --- CAMBIO CLAVE: Apuntamos a 'modulos/' en lugar de 'pages/' ---
page_tasas = st.Page("modulos/1_tasas.py", title="1. Conversión de Tasas", icon="🔄")
page_anualidades = st.Page("modulos/2_anualidades.py", title="2. Anualidades y Gradientes", icon="📈")
page_amortizacion = st.Page("modulos/3_amortizacion.py", title="3. Tablas de Amortización", icon="📊")
page_chatbot = st.Page("modulos/4_chatbot_rag.py", title="4. Asistente IA (RAG)", icon="🤖")

pages = [page_tasas, page_anualidades, page_amortizacion, page_chatbot]

# 4. Lógica de renderizado
if not st.session_state.authenticated:
    # VISTA PÚBLICA (LOGIN)
    st.title("Acceso al Sistema Easy Finance")
    st.markdown("Por favor, inicie sesión para acceder a los motores de cálculo deterministas.")
    
    with st.form("login_form"):
        email = st.text_input("Usuario / Email")
        password = st.text_input("Contraseña", type="password")
        submit = st.form_submit_button("Ingresar")
        
        if submit:
            if authenticate_user(email, password):
                st.rerun()
            else:
                st.error("Credenciales inválidas. Acceso denegado.")
                
    render_footer()

else:
    # VISTA PRIVADA (MÓDULOS)
    st.sidebar.image("assets/logo_easyfinance.png", use_container_width=True)
    st.sidebar.markdown('<hr class="custom-hr">', unsafe_allow_html=True)
    st.sidebar.markdown(f"**Usuario:** {st.session_state.user}")
    
    if st.sidebar.button("Cerrar Sesión"):
        logout()
        st.rerun()
    
    st.sidebar.divider()
    
    pg = st.navigation(pages)
    pg.run()
    
    render_footer()

