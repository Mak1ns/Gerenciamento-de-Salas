import streamlit as st
from views.reservas_view import render_reserva_salas
from views.consultar_reservas_view import render_consultar_reservas

def render_dasboard():
    # Recupera os dados do usuário logado
    usuario_logado = st.session_state.get("usuario_logado", {})
    if isinstance(usuario_logado, dict):
        nome = usuario_logado.get("nome", "Usuário")
        perfil = usuario_logado.get("perfil", usuario_logado.get("tipo", "Perfil não definido"))
    else:
        nome = "Usuário"
        perfil = "Perfil não definido"

    # Barra lateral
    st.sidebar.title("ÁTILA")
    st.sidebar.markdown(f"Bem-vindo, **{nome}**!")
    st.sidebar.markdown(f"Perfil: **{perfil}**")
    st.sidebar.divider()

    # Opções do menu
    menu = st.sidebar.radio(
        "Navegação",
        ["🏠 Início / Visão Geral", "📅 Reserva de Salas", "🔍 Consultar Reservas", "⚙️ Gerenciar Salas (Admin)"]
    )

    # Roteamento de telas
    if menu == "🏠 Início / Visão Geral":
        st.title("🏠 Início / Visão Geral")
        st.write("Sistema Inteligente de Gerenciamento de Salas de Aula - ÁTILA")
        # Insira aqui os seus métricas/cards do dashboard inicial

    elif menu == "📅 Reserva de Salas":
    
        render_reserva_salas()

    elif menu == "🔍 Consultar Reservas":
        render_consultar_reservas()

    elif menu == "⚙️ Gerenciar Salas (Admin)":
        st.title("⚙️ Gerenciar Salas")
        st.write("Em breve: cadastro e edição de salas.")

    # Botão de Logout
    st.sidebar.divider()
    if st.sidebar.button("Sair / Logout"):
        st.session_state["autenticado"] = False
        st.session_state["usuario_logado"] = None
        st.rerun()