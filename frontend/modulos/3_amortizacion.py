import streamlit as st
import pandas as pd
import requests
from utils import load_css, render_footer

# 1. Aplicar estilos globales al inicio
load_css()

st.header("Generación de Tablas de Amortización")

col1, col2 = st.columns(2)
with col1:
    monto = st.number_input("Monto del Crédito", min_value=0.0, step=100000.0, value=10000000.0)
    n_periodos = st.number_input("Plazo (meses)", min_value=1, step=1, value=12)
with col2:
    tasa_credito = st.number_input("Tasa de Interés Periódica (%)", format="%.4f", value=1.5)
    sistema_ui = st.selectbox("Sistema de Amortización", [
        "Cuota Fija", 
        "Abono Fijo a Capital"
    ])

# Mapeo simple de la UI al backend
sistema_backend = "Frances" if "Frances" in sistema_ui else "Aleman"

if st.button("Generar Tabla"):
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
            st.metric("Total Intereses Pagados", f"${total_interes:,.2f}")
            
        else:
            st.error(f"Error del motor: {response.json()['detail']}")
            
    except requests.exceptions.ConnectionError:
        st.error("Error: Backend desconectado.")

# 3. Renderizar el footer al final de la página
render_footer()

