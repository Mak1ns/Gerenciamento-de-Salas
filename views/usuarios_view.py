import streamlit as st

from controllers.usuario_controller import UsuarioController


def show_usuarios():

    controller = UsuarioController()

    st.title("👥 Usuários")

    st.write("Consulta dos usuários cadastrados no sistema.")

    st.divider()

    nome = st.text_input(
        "Pesquisar usuário",
        placeholder="Digite um nome..."
    )

    usuarios = controller.buscar_usuario(nome)

    st.subheader("Usuários encontrados")

    st.dataframe(
        usuarios,
        use_container_width=True,
        hide_index=True
    )

    st.caption(
        f"{len(usuarios)} usuário(s) encontrado(s)."
    )