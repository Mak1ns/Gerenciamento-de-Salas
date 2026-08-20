import streamlit as st

from views.inicio_view import show_inicio
from views.usuarios_view import show_usuarios


st.set_page_config(
    page_title="Sistema Reserva de Salas",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)


with st.sidebar:
    st.title("🏢 Reserva de Salas")

    st.divider()

    pagina = st.radio(
        "Navegação",
        [
            "🏠 Início",
            "👥 Usuários",
        ]
    )

    st.divider()

    st.caption("Versão 1.0.0")


if pagina == "🏠 Início":
    show_inicio()

elif pagina == "👥 Usuários":
    show_usuarios()