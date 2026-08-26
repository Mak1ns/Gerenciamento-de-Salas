import streamlit as st
from controllers.usuario_controller import UsuarioController


def show_inicio():
    controller = UsuarioController()

    st.title(text_alignment="center", color="blue", text="ÁTILA")
    st.write("Seja Bem-Vindo ao Sistema de Gerenciamento de Salas de Aula.")


    if "autenticado" not in st.session_state:
        st.session_state["autenticado"] = False

    st.divider()

    if st.session_state["autenticado"]:
        st.success(
            f"Você está conectado como **{st.session_state.get('usuario_logado', 'Usuário')}**!"
        )

        if st.button("🚪 Sair / Logout"):
            st.session_state["autenticado"] = False
            st.session_state["usuario_logado"] = None
            st.rerun()

    # usuário NÃO estiver logado:
    else:
        st.subheader("Login")
        

        with st.form("form_login"):
            email = st.text_input("E-mail")
            
            senha = st.text_input("Senha", type="password")
            btn_entrar = st.form_submit_button("Entrar")

            if btn_entrar:
                
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