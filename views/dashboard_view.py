import streamlit as st
from views.reservas_view import render_reserva_salas
from views.consultar_reservas_view import render_consultar_reservas
from views.visao_geral_view import render_visao_geral 

def render_dasboard():
    # usuário logado
    usuario_logado = st.session_state.get("usuario_logado", {})
    if isinstance(usuario_logado, dict):
        nome = usuario_logado.get("nome", "Usuário")
        perfil = usuario_logado.get("perfil", usuario_logado.get("tipo", "Professor(a)"))
    else:
        nome = "Usuário"
        perfil = "Professor(a)"

    st.sidebar.title("ÁTILA")
    st.sidebar.markdown(f"Bem-vindo, **{nome}**!")
    st.sidebar.markdown(f"Perfil: **{perfil}**")
    st.sidebar.divider()

    # menu
    menu = st.sidebar.radio(
        "Navegação",
        ["🏠 Início / Visão Geral", "📅 Reserva de Salas", "🔍 Consultar Reservas", "⚙️ Gerenciar Salas (Admin)"]
    )

    
    if menu == "🏠 Início / Visão Geral":
        
        render_visao_geral()

    elif menu == "📅 Reserva de Salas":
        render_reserva_salas()

    elif menu == "🔍 Consultar Reservas":
        render_consultar_reservas()

    elif menu == "⚙️ Gerenciar Salas (Admin)":
        

    # Botão de Logout
        st.sidebar.divider()
        
    if  st.sidebar.button("Sair / Logout"):
        st.session_state["autenticado"] = False
        st.session_state["usuario_logado"] = None
        st.rerun()