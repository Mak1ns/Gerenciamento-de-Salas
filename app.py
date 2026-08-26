import streamlit as st

from views.inicio_view import show_inicio
from views.usuarios_view import show_usuarios
from views.salas_view import show_salas

st.set_page_config(
    page_title="Reserva de Salas",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)


if "autenticado" not in st.session_state:
    st.session_state["autenticado"] = False

with st.sidebar:
    st.title("🏢 Reserva de Salas")
    st.divider()

    pagina = st.radio(
        "Navegação",
        [
            "🏠 Inicio",
            "👥 Usuários",
            "🏫 Salas de Aula",
        ]
    )
    st.divider()
    st.caption("Versão 1.0.0")

if pagina == "🏠 Inicio":
    show_inicio()

elif pagina == "👥 Usuários":
    show_usuarios()

elif pagina == "🏫 Salas de Aula":
    show_salas()