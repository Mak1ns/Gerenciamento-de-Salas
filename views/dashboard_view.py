import streamlit as st


def render_dasboard():
    usuario_logado = st.session_state.get("usuario_logado", {})

    
    if isinstance(usuario_logado, dict):
        nome = usuario_logado.get("nome", "Usuário")
        perfil = usuario_logado.get("perfil", "Perfil não definido")
    else:
        nome = usuario_logado
        perfil = "Perfil não definido"

    # Barra Lateral (Sidebar)
    with st.sidebar:
        st.markdown("### ÁTILA")
        st.write(f"Bem-vindo, **{nome}**!")
        st.write(f"Perfil: **{perfil}**")

        st.divider()

        menu_opcao = st.radio(
            "Navegação",
            [
                "🏠 Início / Visão Geral",
                "📅 Reserva de Salas",
                "🔍 Consultar Reservas",
                "⚙️ Gerenciar Salas (Admin)",
            ],
        )

        st.divider()

        if st.button("🚪 Sair / Logout"):
            st.session_state["autenticado"] = False
            st.session_state["usuario_logado"] = None
            st.rerun()

        st.caption("Versão 1.0.0")

    # Conteúdo Principal
    if menu_opcao == "🏠 Início / Visão Geral":
        st.title("🏠 Início / Visão Geral")
        st.markdown(
            "Sistema Inteligente de Gerenciamento de Salas de Aula - ÁTILA"
        )

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(
                label="Salas Disponíveis", value="12", delta="Disponível"
            )
        with col2:
            st.metric(label="Reservas Ativas", value="5", delta="Ativas")
        with col3:
            st.metric(
                label="Ocupação Geral", value="75%", delta="-5% vs ontem"
            )

        st.info("💡 Use o Menu Lateral para Navegar")

    elif menu_opcao == "👥 Usuários":
        st.subheader("👥 Gerenciamento de Usuários")
        st.write("Em breve: Listagem e cadastro de usuários.")

    elif menu_opcao == "📅 Reserva de Salas":
        st.subheader("📅 Solicitar nova Reserva")
        st.write(
            "Em breve: Formulário para escolher sala, data, horário e motivo da reserva."
        )

    elif menu_opcao == "🔍 Consultar Reservas":
        st.subheader("🔍 Consulta de Salas Reservadas")
        st.write(
            "Em breve: Consulta de reservas por sala, data, horário e histórico do usuário."
        )

    elif menu_opcao == "🏫 Salas de Aula":
        st.subheader("🏫 Visualização de Salas")
        st.write("Em breve: Lista de salas de aula e seus recursos.")

    elif menu_opcao == "⚙️ Gerenciar Salas (Admin)":
        if perfil.lower() == "administrador":
            st.subheader("⚙️ Administrador")
            st.write(
                "Em breve: Cadastro de novas salas, blocos e bloqueio de horários."
            )
        else:
            st.warning(
                "⚠️ Acesso Negado: Você não tem permissão para acessar esta seção."
            )