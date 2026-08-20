import streamlit as st

from controllers.usuario_controller import UsuarioController

def show_inicio():

    controller = UsuarioController()

    st.title("🏠 Início")

    st.write(
        "Exemplo de aplicação Streamlit utilizando arquitetura MVC."
    )

    st.divider()

    total_usuarios = controller.quantidade_usuarios()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="Usuários cadastrados",
            value=total_usuarios
        )

    with col2:
        st.metric(
            label="Status",
            value="Online"
        )

    with col3:
        st.metric(
            label="Arquitetura",
            value="MVC"
        )