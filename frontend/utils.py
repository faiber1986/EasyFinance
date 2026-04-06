# frontend/utils.py
import streamlit as st
import base64
import datetime

def load_css(file_name="assets/style.css"):
    """Carga y aplica el CSS global."""
    try:
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"Advertencia: No se encontró el archivo de estilos en {file_name}")

def get_base64_image(image_path):
    """Codifica imágenes locales a Base64 para inyección HTML."""
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    except FileNotFoundError:
        return ""

def render_footer():
    """Genera e inyecta el footer corporativo usando SVG para evitar dependencias de archivos."""
    current_year = datetime.datetime.now().year
    
    # Firma vectorial en código (Monograma FAMG)
    svg_signature = """
    <svg xmlns="http://www.w3.org/2000/svg" width="140" height="30">
        <text x="0" y="20" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="#00305C" letter-spacing="1.5">FAMG</text>
        <text x="50" y="20" font-family="Arial, sans-serif" font-size="11" fill="#666666"></text>
    </svg>
    """
    import base64
    b64_signature = base64.b64encode(svg_signature.encode('utf-8')).decode('utf-8')
    
    footer_html = f"""
    <div class="custom-footer">
        <p>Desarrollado por:</p>
        <img src="data:image/svg+xml;base64,{b64_signature}" class="dev-firm" alt="Faiber Andres Montes Gomez" style="height: 25px; margin: 0 10px;">
        <p>Ingeniero Financiero</p>
        <p> | &nbsp; {current_year} &nbsp; | </p>
        <p><strong>&copy;</strong> &nbsp; Todos los derechos reservados.</p>
    </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)

