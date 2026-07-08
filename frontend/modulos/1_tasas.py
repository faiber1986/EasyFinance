# frontend/pages/1_tasas.py
import streamlit as st
from utils import load_css, render_footer
from i18n import t, opt

# 1. Aplicar estilos globales al inicio
load_css()

# 2. Lógica de la interfaz de usuario
st.header(t("tasas_header"))
st.markdown(t("tasas_subtitle"))

TIPOS_TASA = ["Nominal", "Efectiva Anual (EA)", "Periódica"]

col1, col2 = st.columns(2)

with col1:
    tasa_origen = st.number_input(t("tasas_origen_label"), min_value=0.0, format="%.4f")
    periodos = st.number_input(t("tasas_periodos_label"), min_value=1, step=1)

with col2:
    tipo_origen = st.selectbox(
        t("tasas_tipo_origen_label"), TIPOS_TASA, format_func=lambda v: opt("tipo_tasa", v)
    )
    tipo_destino = st.selectbox(
        t("tasas_tipo_destino_label"), TIPOS_TASA, format_func=lambda v: opt("tipo_tasa", v)
    )

st.divider()

if st.button(t("tasas_calcular_button")):
    import requests
    payload = {
        "tasa_origen": tasa_origen,
        "n": periodos,
        "tipo_origen": tipo_origen,
        "tipo_destino": tipo_destino
    }
    try:
        response = requests.post("http://localhost:8000/api/math/tasas/", json=payload)
        if response.status_code == 200:
            resultado = response.json()
            st.success(f"{t('tasas_resultado')} {resultado['tasa_resultado']:.4f}%")
        else:
            st.error(f"{t('tasas_calc_error')} {response.json()['detail']}")
    except requests.exceptions.ConnectionError:
        st.error(t("tasas_conn_error"))

    st.info(t("tasas_info"))

# 3. Renderizar el footer al final de la página
render_footer()
