import streamlit as st 
from controllers.usuario_controller import UsuarioController


def render_login():
    st.title("Login")

    st.write("Faça login para acessar o sistema.")

    st.divider()

    username = st.text_input(
        "Nome de usuário",
        placeholder="Digite seu nome de usuário..."
    )

    password = st.text_input(
        "Senha",
        type="password",
        placeholder="Digite sua senha..."
    )

    if st.button("Entrar"):
        controller = UsuarioController()
        if controller.autenticar_usuario(username, password):
            st.success("Login bem-sucedido!")
            # Redirecionar para a página inicial ou outra página
            st.experimental_set_query_params(page="inicio")
        else:
            st.error("Nome de usuário ou senha inválidos.")