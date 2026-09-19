import streamlit as st
import pandas as pd
import datetime
from models.reservas_model import ReservasModel
from models.salas_model import SalasModel

def render_visao_geral():
    
    usuario_logado = st.session_state.get("usuario_logado", {})
    if isinstance(usuario_logado, dict):
        nome = usuario_logado.get("nome", "Usuário")
        perfil = usuario_logado.get("perfil", usuario_logado.get("tipo", "Professor(a)"))
        usuario_id = usuario_logado.get("id", 1)
    else:
        nome = "Usuário"
        perfil = "Professor(a)"
        usuario_id = 1

    st.markdown(f"<h2 style='color: #FFA500;'>📊 Bem-vindo(a), {nome}!</h2>", unsafe_allow_html=True)
    st.divider()

    reservas_model = ReservasModel()
    salas_model = SalasModel()


    hoje_str = datetime.date.today().strftime("%Y-%m-%d")

   
    # DASHBOARD DO ADMINISTRADOR
    
    if perfil == "Administrador":
        todas_reservas = reservas_model.listar_todas()
        todas_salas = salas_model.listar_todos()
        
        #reservas de hoje
        reservas_hoje = [r for r in todas_reservas if r[3] == hoje_str]
        
        # KPIs
        col1, col2, col3 = st.columns(3)
        col1.metric("🏢 Salas Cadastradas", len(todas_salas))
        col2.metric("📋 Total de Reservas", len(todas_reservas))
        col3.metric("🔥 Reservas Hoje", len(reservas_hoje))
        
        st.divider()
        st.subheader("📅 Agendamentos Realizados Hoje")
        
        if reservas_hoje:
            df = pd.DataFrame(reservas_hoje, columns=["ID", "Solicitante", "Sala", "Data", "Início", "Término", "Finalidade", "Status"])
            df["Data"] = pd.to_datetime(df["Data"]).dt.strftime("%d/%m/%Y")
           
            st.dataframe(df[["Solicitante", "Sala", "Início", "Término", "Finalidade"]], hide_index=True, use_container_width=True)
        else:
            st.info("Nenhuma reserva programada para hoje.")
            

    # DASHBOARD DO PROFESSOR 

    else:
        minhas_reservas = reservas_model.listar_por_usuario(usuario_id)
        
    
        reservas_hoje = [r for r in minhas_reservas if r[3] == hoje_str]
        
    
        col1, col2 = st.columns(2)
        col1.metric("📌 Meu Total de Reservas", len(minhas_reservas))