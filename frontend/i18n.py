# frontend/i18n.py
"""Traducciones de la interfaz (Español/English) para Easy Finance."""
import streamlit as st

DEFAULT_LANG = "es"

TRANSLATIONS = {
    "es": {
        "page_title": "Easy Finance",
        "nav_tasas": "1. Conversión de Tasas",
        "nav_anualidades": "2. Anualidades y Gradientes",
        "nav_amortizacion": "3. Tablas de Amortización",
        "nav_chatbot": "4. Asistente IA (RAG)",

        "login_title": "Acceso al Sistema Easy Finance",
        "login_instructions": "Por favor, inicie sesión para acceder a los motores de cálculo deterministas.",
        "login_user": "Usuario / Email",
        "login_password": "Contraseña",
        "login_button": "Ingresar",
        "login_error": "Credenciales inválidas. Acceso denegado.",

        "sidebar_user": "**Usuario:**",
        "logout_button": "Cerrar Sesión",
        "theme_toggle": "Modo oscuro",
        "language_toggle": "Idioma",

        "footer_developed_by": "Desarrollado por:",
        "footer_role": "Ingeniero Financiero",
        "footer_rights": "Todos los derechos reservados.",

        "tasas_header": "Conversión de Tasas de Interés",
        "tasas_subtitle": "Interconexión con el motor de cálculo en el backend (FastAPI).",
        "tasas_origen_label": "Tasa Origen (%)",
        "tasas_periodos_label": "Número de Periodos (n)",
        "tasas_tipo_origen_label": "Tipo de Tasa Origen",
        "tasas_tipo_destino_label": "Tipo de Tasa Destino",
        "tasas_calcular_button": "Ejecutar Cálculo",
        "tasas_resultado": "**Resultado:**",
        "tasas_calc_error": "Error de cálculo:",
        "tasas_conn_error": "Error de conexión: El backend de FastAPI no está en ejecución.",
        "tasas_info": "Cálculo delegado al backend. Esperando endpoint REST para renderizar el resultado determinista.",

        "anualidades_header": "Valor Presente, Futuro, Anualidades y Gradientes",
        "anualidades_radio_question": "¿Qué desea calcular?",
        "anualidades_instrumento_label": "Seleccione el instrumento",
        "anualidades_cuota_label": "Valor de la Primera Cuota (A)",
        "anualidades_tasa_label": "Tasa de Interés Periódica (%)",
        "anualidades_periodos_label": "Periodos (n)",
        "anualidades_gradiente_aritmetico_label": "Valor del Gradiente en Moneda (G)",
        "anualidades_gradiente_geometrico_label": "Tasa del Gradiente en % (j)",
        "anualidades_calcular_button": "Calcular Flujo",
        "anualidades_calc_error": "Error de cálculo:",
        "anualidades_conn_error": "Error: Backend desconectado.",

        "amortizacion_header": "Generación de Tablas de Amortización",
        "amortizacion_monto_label": "Monto del Crédito",
        "amortizacion_plazo_label": "Plazo (meses)",
        "amortizacion_tasa_label": "Tasa de Interés Periódica (%)",
        "amortizacion_sistema_label": "Sistema de Amortización",
        "amortizacion_generar_button": "Generar Tabla",
        "amortizacion_total_interes": "Total Intereses Pagados",
        "amortizacion_error_motor": "Error del motor:",
        "amortizacion_conn_error": "Error: Backend desconectado.",

        "chatbot_header": "Asesor Financiero Pro (RAG + Math)",
        "chatbot_caption": "Consultas basadas en normatividad técnica y cálculos exactos.",
        "chatbot_input_placeholder": "¿En qué puedo asesorarte hoy?",
        "chatbot_spinner": "Consultando base de conocimientos y modelos...",
        "chatbot_conn_error": "No se pudo conectar con el agente:",
    },
    "en": {
        "page_title": "Easy Finance",
        "nav_tasas": "1. Rate Conversion",
        "nav_anualidades": "2. Annuities and Gradients",
        "nav_amortizacion": "3. Amortization Tables",
        "nav_chatbot": "4. AI Assistant (RAG)",

        "login_title": "Easy Finance System Access",
        "login_instructions": "Please sign in to access the deterministic calculation engines.",
        "login_user": "Username / Email",
        "login_password": "Password",
        "login_button": "Sign In",
        "login_error": "Invalid credentials. Access denied.",

        "sidebar_user": "**User:**",
        "logout_button": "Log Out",
        "theme_toggle": "Dark mode",
        "language_toggle": "Language",

        "footer_developed_by": "Developed by:",
        "footer_role": "Financial Engineer",
        "footer_rights": "All rights reserved.",

        "tasas_header": "Interest Rate Conversion",
        "tasas_subtitle": "Live connection to the backend calculation engine (FastAPI).",
        "tasas_origen_label": "Source Rate (%)",
        "tasas_periodos_label": "Number of Periods (n)",
        "tasas_tipo_origen_label": "Source Rate Type",
        "tasas_tipo_destino_label": "Target Rate Type",
        "tasas_calcular_button": "Run Calculation",
        "tasas_resultado": "**Result:**",
        "tasas_calc_error": "Calculation error:",
        "tasas_conn_error": "Connection error: the FastAPI backend is not running.",
        "tasas_info": "Calculation delegated to the backend. Waiting for the REST endpoint to render the deterministic result.",

        "anualidades_header": "Present Value, Future Value, Annuities and Gradients",
        "anualidades_radio_question": "What would you like to calculate?",
        "anualidades_instrumento_label": "Select the instrument",
        "anualidades_cuota_label": "First Installment Value (A)",
        "anualidades_tasa_label": "Periodic Interest Rate (%)",
        "anualidades_periodos_label": "Periods (n)",
        "anualidades_gradiente_aritmetico_label": "Gradient Value in Currency (G)",
        "anualidades_gradiente_geometrico_label": "Gradient Rate in % (j)",
        "anualidades_calcular_button": "Calculate Cash Flow",
        "anualidades_calc_error": "Calculation error:",
        "anualidades_conn_error": "Error: backend disconnected.",

        "amortizacion_header": "Amortization Table Generator",
        "amortizacion_monto_label": "Loan Amount",
        "amortizacion_plazo_label": "Term (months)",
        "amortizacion_tasa_label": "Periodic Interest Rate (%)",
        "amortizacion_sistema_label": "Amortization System",
        "amortizacion_generar_button": "Generate Table",
        "amortizacion_total_interes": "Total Interest Paid",
        "amortizacion_error_motor": "Engine error:",
        "amortizacion_conn_error": "Error: backend disconnected.",

        "chatbot_header": "Pro Financial Advisor (RAG + Math)",
        "chatbot_caption": "Answers grounded in technical regulations and exact calculations.",
        "chatbot_input_placeholder": "How can I help you today?",
        "chatbot_spinner": "Querying the knowledge base and models...",
        "chatbot_conn_error": "Could not connect to the agent:",
    },
}

OPTIONS = {
    "tipo_tasa": {
        "es": {"Nominal": "Nominal", "Efectiva Anual (EA)": "Efectiva Anual (EA)", "Periódica": "Periódica"},
        "en": {"Nominal": "Nominal", "Efectiva Anual (EA)": "Effective Annual (EA)", "Periódica": "Periodic"},
    },
    "calculo_tipo": {
        "es": {"VP": "VP (Valor Presente)", "VF": "VF (Valor Futuro)"},
        "en": {"VP": "PV (Present Value)", "VF": "FV (Future Value)"},
    },
    "instrumento": {
        "es": {
            "Anualidad Vencida": "Anualidad Vencida",
            "Anualidad Anticipada": "Anualidad Anticipada",
            "Gradiente Aritmetico": "Gradiente Aritmético",
            "Gradiente Geometrico": "Gradiente Geométrico",
        },
        "en": {
            "Anualidad Vencida": "Ordinary Annuity",
            "Anualidad Anticipada": "Annuity Due",
            "Gradiente Aritmetico": "Arithmetic Gradient",
            "Gradiente Geometrico": "Geometric Gradient",
        },
    },
    "sistema": {
        "es": {"Frances": "Cuota Fija (Francés)", "Aleman": "Abono Fijo a Capital (Alemán)"},
        "en": {"Frances": "Fixed Installment (French System)", "Aleman": "Fixed Principal (German System)"},
    },
}


def init_language():
    """Inicializa el idioma de la sesión."""
    if "lang" not in st.session_state:
        st.session_state.lang = DEFAULT_LANG


def current_lang():
    return st.session_state.get("lang", DEFAULT_LANG)


def set_language(lang):
    st.session_state.lang = lang if lang in TRANSLATIONS else DEFAULT_LANG


def t(key):
    """Traduce una clave de texto estático al idioma activo."""
    lang = current_lang()
    return TRANSLATIONS.get(lang, TRANSLATIONS[DEFAULT_LANG]).get(key, TRANSLATIONS[DEFAULT_LANG].get(key, key))


def opt(category, value):
    """Traduce el texto visible de una opción, conservando el valor interno intacto."""
    lang = current_lang()
    return OPTIONS.get(category, {}).get(lang, {}).get(value, value)
