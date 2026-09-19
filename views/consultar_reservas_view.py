import streamlit as st
import pandas as pd
from models.reservas_model import ReservasModel
from models.salas_model import SalasModel

def render_consultar_reservas():
    st.title("🔍 Consultar Reservas")
    
    #  busca do perfil
    usuario_logado = st.session_state.get("usuario_logado", {})
    
    perfil = ""
    usuario_id = 1

    if isinstance(usuario_logado, dict):
        perfil = str(usuario_logado.get("perfil") or usuario_logado.get("tipo") or usuario_logado.get("funcao") or "").lower()
        usuario_id = usuario_logado.get("id", 1)

    # Verificaçao de perfil administrador
    eh_admin = perfil in ["administrador", "admin"]

    reservas_model = ReservasModel()
    salas_model = SalasModel()


    if eh_admin:
        reservas = reservas_model.listar_todas()
    else:
        reservas = reservas_model.listar_por_usuario(usuario_id)

    if not reservas:
        st.info("Nenhuma reserva encontrada.")
        return

    # exibi as reservas
    df = pd.DataFrame(reservas, columns=["ID", "Solicitante", "Sala", "Data", "Início", "Término", "Finalidade", "Status"])
    df["Data"] = pd.to_datetime(df["Data"]).dt.strftime("%d/%m/%Y")
    
    st.subheader("📋 Todas as Reservas" if eh_admin else "📋 Minhas Reservas")

    # Administrador
    if eh_admin:
        colunas_exibir = ["Solicitante", "Sala", "Data", "Início", "Término", "Finalidade", "Status"]
    else:
        colunas_exibir = ["Sala", "Data", "Início", "Término", "Finalidade", "Status"]

    st.dataframe(df[colunas_exibir], hide_index=True, use_container_width=True)

    # ADMINISTRADOR
    if eh_admin:
        st.divider()
        st.subheader("🛠️ Gerenciar Reserva (Editar / Excluir)")

        opcoes_reservas = {f"ID #{r[0]} — Sala: {r[2]} | Prof. {r[1]} ({r[3]} de {r[4]} às {r[5]})": r for r in reservas}
        reserva_selecionada = st.selectbox("Selecione uma reserva para alterar:", list(opcoes_reservas.keys()))

        if reserva_selecionada:
            dados_reserva = opcoes_reservas[reserva_selecionada]
            reserva_id = dados_reserva[0]

            tab_editar, tab_excluir = st.tabs(["✏️ Editar Reserva", "🗑️ Excluir Reserva"])

            with tab_editar:
                salas = salas_model.listar_todos()
                opcoes_salas = {f"{s[1]} ({s[2]})": s[0] for s in salas}
                
                idx_sala = 0
                for i, (nome_sala, id_sala) in enumerate(opcoes_salas.items()):
                    if dados_reserva[2] in nome_sala:
                        idx_sala = i
                        break

                sala_id = st.selectbox("Sala", list(opcoes_salas.keys()), index=idx_sala)
                data = st.date_input("Data", value=pd.to_datetime(dados_reserva[3], format="mixed", dayfirst=True), format="DD/MM/YYYY")
                inicio = st.time_input("Horário Início", value=pd.to_datetime(dados_reserva[4]).time())
                termino = st.time_input("Horário Término", value=pd.to_datetime(dados_reserva[5]).time())
                finalidade = st.text_input("Finalidade", value=dados_reserva[6])

                if st.button("Salvar Alterações"):
                    sucesso = reservas_model.atualizar(
                        reserva_id, 
                        opcoes_salas[sala_id], 
                        data.strftime("%d-%m-%Y"), 
                        inicio.strftime("%H:%M"), 
                        termino.strftime("%H:%M"), 
                        finalidade
                    )
                    if sucesso:
                        st.success("Reserva atualizada com sucesso!")
                        st.rerun()
                    else:
                        st.error("Erro ao atualizar a reserva.")

            with tab_excluir:
                st.warning(f"Tem certeza que deseja excluir a reserva **{reserva_selecionada}**?")
                if st.button("Confirmar Exclusão", type="primary"):
                    if reservas_model.excluir(reserva_id):
                        st.success("Reserva excluída com sucesso!")
                        st.rerun()
                    else:
                        st.error("Erro ao excluir a reserva.")