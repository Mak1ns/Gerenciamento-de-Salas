import streamlit as st 
from controllers.usuario_controller import UsuarioController


def render_login():
    st.title("🔐 Login")
    st.markdown("<h1 style='text-align: center; color: #000000'>ATILA</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #FFA500'>Reseerva de Salas - UniSapiens</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
 
with col2:
    st.markdown("# Autenticação")
    
    with st.form("form_login"):
        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")
        btn_entrar = st.form_submit_button("Entrar")

        if btn_entrar:
            controller = UsuarioController()
            usuarios = controller.listar_usuarios() if hasattr(controller, 'listar_usuarios') else []
            
            usuario_encontrado = None
            if not usuarios.empty if hasattr(usuarios, 'empty') else usuarios:
                resultado = usuarios[usuarios["email"].astype(str).str.strip().str.lower() == email.strip().lower()]
                if not resultado.empty:
                    usuario_encontrado = resultado.iloc[0]

            if usuario_encontrado is not None:
                st.session_state["autenticado"] = True
                st.session_state["usuario_logado"] = usuario_encontrado["nome"]
                st.success("Login efetuado com sucesso!")
                st.rerun()
            else:
                st.error("E-mail ou senha inválidos.")