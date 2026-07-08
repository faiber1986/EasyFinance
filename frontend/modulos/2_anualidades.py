import streamlit as st
import requests
from utils import load_css, render_footer
from i18n import t, opt

# 1. Aplicar estilos globales al inicio
load_css()

# 2. Lógica de la interfaz de usuario
st.header(t("anualidades_header"))

tipo_calculo = st.radio(
    t("anualidades_radio_question"),
    ["VP", "VF"],
    format_func=lambda v: opt("calculo_tipo", v),
    horizontal=True,
)
tipo_instrumento = st.selectbox(
    t("anualidades_instrumento_label"),
    ["Anualidad Vencida", "Anualidad Anticipada", "Gradiente Aritmetico", "Gradiente Geometrico"],
    format_func=lambda v: opt("instrumento", v),
)

st.divider()

col1, col2 = st.columns(2)
with col1:
    cuota = st.number_input(t("anualidades_cuota_label"), min_value=0.0, step=1000.0, value=100000.0)
    tasa = st.number_input(t("anualidades_tasa_label"), format="%.4f", value=1.0)

with col2:
    n = st.number_input(t("anualidades_periodos_label"), min_value=1, step=1, value=12)

    gradiente = 0.0
    if tipo_instrumento == "Gradiente Aritmetico":
        gradiente = st.number_input(t("anualidades_gradiente_aritmetico_label"), value=5000.0)
    elif tipo_instrumento == "Gradiente Geometrico":
        gradiente = st.number_input(t("anualidades_gradiente_geometrico_label"), value=0.5, format="%.4f")

if st.button(t("anualidades_calcular_button")):
    payload = {
        "tipo_calculo": tipo_calculo,
        "tipo_instrumento": tipo_instrumento,
        "tasa": tasa,
        "periodos": n,
        "cuota_base": cuota,
        "gradiente": gradiente
    }

    try:
        response = requests.post("http://127.0.0.1:8000/api/math/flujos/", json=payload)

        if response.status_code == 200:
            resultado = response.json()["valor_calculado"]
            st.success(f"**{opt('calculo_tipo', tipo_calculo)}:** ${resultado:,.2f}")
        else:
            st.error(f"{t('anualidades_calc_error')} {response.json()['detail']}")
    except requests.exceptions.ConnectionError:
        st.error(t("anualidades_conn_error"))

# 3. Renderizar el footer al final de la página
render_footer()
