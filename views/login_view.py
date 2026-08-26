import streamlit as st 
from controllers.auth_controller import AuthController

def render_login(form_key="form_login"):
    st.markdown("<h1 style='text-align: center; margin-bottom: 0; color: #FFA500'>ÁTILA</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #FFA500'>Reserva de Salas - UniSapiens</p>", unsafe_allow_html=True)

    st.write("") # Espaçamento
    
    col1, col2, col3 = st.columns([1, 1.2, 1])
 
    with col2:
    
        with st.form(form_key):
            email = st.text_input("E-mail")
            senha = st.text_input("Senha", type="password")
            btn_entrar = st.form_submit_button("Entrar")

        if btn_entrar:
            controller = AuthController()
            is_authenticated, usuario, mensagem = controller.tentar_login(email, senha)

            if is_authenticated:
                st.session_state["autenticado"] = True
                st.session_state["usuario_logado"] = usuario["nome"]
                st.success("Login efetuado com sucesso!")
                st.rerun()
            else:
                st.error(mensagem)
                usuario_encontrado = None

            if usuario_encontrado is not None:
                st.session_state["autenticado"] = True
                st.session_state["usuario_logado"] = usuario_encontrado["nome"]
                st.success("Login efetuado com sucesso!")
                st.rerun()
            else:
                st.error("E-mail ou senha inválidos.")