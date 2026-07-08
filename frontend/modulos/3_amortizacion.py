import streamlit as st
import pandas as pd
import requests
from utils import load_css, render_footer
from i18n import t, opt

# 1. Aplicar estilos globales al inicio
load_css()

st.header(t("amortizacion_header"))

col1, col2 = st.columns(2)
with col1:
    monto = st.number_input(t("amortizacion_monto_label"), min_value=0.0, step=100000.0, value=10000000.0)
    n_periodos = st.number_input(t("amortizacion_plazo_label"), min_value=1, step=1, value=12)
with col2:
    tasa_credito = st.number_input(t("amortizacion_tasa_label"), format="%.4f", value=1.5)
    sistema_backend = st.selectbox(
        t("amortizacion_sistema_label"),
        ["Frances", "Aleman"],
        format_func=lambda v: opt("sistema", v),
    )

if st.button(t("amortizacion_generar_button")):
    payload = {
        "monto": monto,
        "tasa_interes": tasa_credito,
        "periodos": n_periodos,
        "sistema": sistema_backend
    }

    try:
        response = requests.post("http://127.0.0.1:8000/api/math/amortizacion/", json=payload)

        if response.status_code == 200:
            datos_json = response.json()["tabla"]
            df = pd.DataFrame(datos_json)

            # Formatear columnas como moneda para la visualización
            columnas_moneda = ["saldo_inicial", "cuota", "interes", "abono_capital", "saldo_final"]
            for col in columnas_moneda:
                df[col] = df[col].apply(lambda x: f"${x:,.2f}")

            st.dataframe(df, use_container_width=True, hide_index=True)

            # Métricas resumen
            total_interes = sum(item["interes"] for item in datos_json)
            st.metric(t("amortizacion_total_interes"), f"${total_interes:,.2f}")

        else:
            st.error(f"{t('amortizacion_error_motor')} {response.json()['detail']}")

    except requests.exceptions.ConnectionError:
        st.error(t("amortizacion_conn_error"))

# 3. Renderizar el footer al final de la página
render_footer()
