# frontend/pages/1_tasas.py
import streamlit as st
from utils import load_css, render_footer

# 1. Aplicar estilos globales al inicio
load_css()

# 2. Lógica de la interfaz de usuario
st.header("Conversión de Tasas de Interés")
st.markdown("Interconexión con el motor de cálculo en el backend (FastAPI).")

col1, col2 = st.columns(2)

with col1:
    tasa_origen = st.number_input("Tasa Origen (%)", min_value=0.0, format="%.4f")
    periodos = st.number_input("Número de Periodos (n)", min_value=1, step=1)

with col2:
    tipo_origen = st.selectbox("Tipo de Tasa Origen", ["Nominal", "Efectiva Anual (EA)", "Periódica"])
    tipo_destino = st.selectbox("Tipo de Tasa Destino", ["Nominal", "Efectiva Anual (EA)", "Periódica"])

st.divider()

if st.button("Ejecutar Cálculo"):
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
            st.success(f"**Resultado:** {resultado['tasa_resultado']:.4f}%")
        else:
            st.error(f"Error de cálculo: {response.json()['detail']}")
    except requests.exceptions.ConnectionError:
        st.error("Error de conexión: El backend de FastAPI no está en ejecución.")
    
    st.info("Cálculo delegado al backend. Esperando endpoint REST para renderizar el resultado determinista.")

# 3. Renderizar el footer al final de la página
render_footer()

