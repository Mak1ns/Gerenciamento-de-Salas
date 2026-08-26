import streamlit as st

def render_dasboard():
    
   usuario_logado = st.session_state.get("usuario_logado", "Usuário")
   nome = usuario_logado.get("nome", "Usuário")
   perfil = usuario_logado.get("perfil", "Perfil não definido")
   
   with st.sidebar:
         st.markdown("### ÁTILA")
         st.write(f"Bem-vindo, **{nome}**!")
         st.write(f"Perfil: **{perfil}**")
         
         st.divider()
         
    if menu_opcao == st.radio(
        "Navegação",
        [
            "🏠 Início / Visão Geral",
            "👥 Usuários",
            "📅 Reserva de Salas",
            "🔍 Consultar Reservas",
            "🏫 Salas de Aula",
            "⚙️ Gerenciar Salas (Admin)",
        ]
    ):
        st.divider()
        
        
        if st.button("🚪 Sair / Logout"):
            st.session_state["autenticado"] = False
            st.session_state["usuario_logado"] = None
            st.rerun()
            
    if menu_opcao == "🏠 Início / Visão Geral":
        st.title("🏠 Início / Visão Geral"):
        st.markdown("Sistema Inteligente de Gerenciamento de Salas de Aula - ÁTILA")
        
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.metric(label="Salas Disponíveis", value="12", delta="Disponivel")
    with col2:
        st.metric(label="Reservas Ativas", value="5", delta="Ativas")
    with col3:
        st.metric(label="Ocupação Geral", value="75%", delta="-5% vs ontem")
        
        st.info("💡 Use o Menu Lateral para Navegar")
        
elif menu_opcao == "📅 Reserva de Salas":
    st.subheader("📅 Solicitar nova Reserva")
    st.write("em breve: Formulário para escolher sala, data, horário e motivo da reserva.")
    
elif menu_opcao == "🔍 Consultar Reservas":
    st.subheader("🔍 Consulta de Salas Reservadas")
    st.write("em breve: Consulta de reservas por sala, data, horario e histórico de reservas do usuário.")
    
elif menu_opcao == "⚙️ Gerenciar Salas (Admin)":
    if perfil.lower() == "administrador":
        st.subheader("⚙️ Administrador")
        st.write("em breve: Cadastro de novas salas, blocos e bloqueio de horários.")
    else:
        st.warning("⚠️ Acesso Negado: Você não tem permissão para acessar esta seção.")
    
        
        
        
        
        
        
        
        
        
        
        
        st.caption("Versão 1.0.0")