import streamlit as st
from auth import init_session, authenticate_user, logout
from utils import load_css, render_footer, init_theme, set_theme, is_dark_mode
from i18n import init_language, set_language, current_lang, t

# 1. Inicialización de estado (debe ocurrir antes de set_page_config)
init_theme()
init_language()

# 2. Configuración base
st.set_page_config(page_title=t("page_title"), layout="wide", page_icon="📈")

# 3. Carga global de estilos y sesión
load_css()
init_session()

# --- CAMBIO CLAVE: Apuntamos a 'modulos/' en lugar de 'pages/' ---
page_tasas = st.Page("modulos/1_tasas.py", title=t("nav_tasas"), icon="🔄")
page_anualidades = st.Page("modulos/2_anualidades.py", title=t("nav_anualidades"), icon="📈")
page_amortizacion = st.Page("modulos/3_amortizacion.py", title=t("nav_amortizacion"), icon="📊")
page_chatbot = st.Page("modulos/4_chatbot_rag.py", title=t("nav_chatbot"), icon="🤖")

pages = [page_tasas, page_anualidades, page_amortizacion, page_chatbot]


LANG_OPTIONS = ["es", "en"]
LANG_LABELS = {"es": "🇪🇸 Español", "en": "🇬🇧 English"}


def _on_theme_change():
    set_theme("dark" if st.session_state.theme_switch else "light")


def _on_lang_change():
    set_language(st.session_state.lang_select)


def render_preferences(container):
    """Toggles de idioma y tema, disponibles en login y en la app autenticada.

    Usan on_change para que session_state se actualice ANTES del siguiente
    rerun; así ningún texto (incluidas las propias etiquetas) queda un
    render atrasado respecto al cambio de idioma/tema.
    """
    col1, col2 = container.columns(2)

    col1.toggle(
        f"🌓 {t('theme_toggle')}",
        value=is_dark_mode(),
        key="theme_switch",
        on_change=_on_theme_change,
    )

    col2.selectbox(
        t("language_toggle"),
        LANG_OPTIONS,
        index=LANG_OPTIONS.index(current_lang()),
        format_func=lambda code: LANG_LABELS[code],
        key="lang_select",
        on_change=_on_lang_change,
    )


# 4. Lógica de renderizado
if not st.session_state.authenticated:
    # VISTA PÚBLICA (LOGIN)
    render_preferences(st.container())

    st.title(t("login_title"))
    st.markdown(t("login_instructions"))

    with st.form("login_form"):
        email = st.text_input(t("login_user"))
        password = st.text_input(t("login_password"), type="password")
        submit = st.form_submit_button(t("login_button"))

        if submit:
            if authenticate_user(email, password):
                st.rerun()
            else:
                st.error(t("login_error"))

    render_footer()

else:
    # VISTA PRIVADA (MÓDULOS)
    st.sidebar.image("assets/logo_easyfinance.png", use_container_width=True)
    st.sidebar.markdown('<hr class="custom-hr">', unsafe_allow_html=True)
    st.sidebar.markdown(f"{t('sidebar_user')} {st.session_state.user}")

    render_preferences(st.sidebar)

    if st.sidebar.button(t("logout_button")):
        logout()
        st.rerun()

    st.sidebar.divider()

    pg = st.navigation(pages)
    pg.run()

    render_footer()

