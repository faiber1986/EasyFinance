import streamlit as st
import requests
from utils import load_css, render_footer

# 1. Aplicar estilos globales al inicio
load_css()

# 2. Lógica de la interfaz de usuario
st.header("Valor Presente, Futuro, Anualidades y Gradientes")

tipo_calculo = st.radio("¿Qué desea calcular?", ["VP (Valor Presente)", "VF (Valor Futuro)"], horizontal=True)
tipo_instrumento = st.selectbox("Seleccione el instrumento", [
    "Anualidad Vencida", 
    "Anualidad Anticipada", 
    "Gradiente Aritmetico", 
    "Gradiente Geometrico"
])

st.divider()

col1, col2 = st.columns(2)
with col1:
    cuota = st.number_input("Valor de la Primera Cuota (A)", min_value=0.0, step=1000.0, value=100000.0)
    tasa = st.number_input("Tasa de Interés Periódica (%)", format="%.4f", value=1.0)

with col2:
    n = st.number_input("Periodos (n)", min_value=1, step=1, value=12)
    
    gradiente = 0.0
    if tipo_instrumento == "Gradiente Aritmetico":
        gradiente = st.number_input("Valor del Gradiente en Moneda (G)", value=5000.0)
    elif tipo_instrumento == "Gradiente Geometrico":
        gradiente = st.number_input("Tasa del Gradiente en % (j)", value=0.5, format="%.4f")

if st.button("Calcular Flujo"):
    payload = {
        "tipo_calculo": "VP" if "VP" in tipo_calculo else "VF",
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
            st.success(f"**{tipo_calculo}:** ${resultado:,.2f}")
        else:
            st.error(f"Error de cálculo: {response.json()['detail']}")
    except requests.exceptions.ConnectionError:
        st.error("Error: Backend desconectado.")

# 3. Renderizar el footer al final de la página
render_footer()

