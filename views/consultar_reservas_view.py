import streamlit as st
import pandas as pd
import datetime
from models.reservas_model import ReservasModel
from models.salas_model import SalasModel

def render_consultar_reservas():
    st.markdown("<h2 style='color: #FFA500;'>🔍 Consultar e Gerenciar Reservas</h2>", unsafe_allow_html=True)

    usuario_logado = st.session_state.get("usuario_logado", {})
    if isinstance(usuario_logado, dict):
        perfil = usuario_logado.get("perfil", usuario_logado.get("tipo", ""))
        usuario_id = usuario_logado.get("id", 1)
    else:
        perfil = ""
        usuario_id = 1

    reserva_model = ReservasModel()
    salas_model = SalasModel()

    # Admin vê tudo; usuário comum vê apenas as suas
    if perfil == "Administrador":
        reservas = reserva_model.listar_todas()
    else:
        reservas = reserva_model.listar_por_usuario(usuario_id)

    if not reservas:
        st.info("Nenhuma reserva encontrada.")
        return

    # Tabela visualização
    colunas = ["ID", "Solicitante", "Sala", "Data", "Início", "Término", "Finalidade", "Status"]
    df = pd.DataFrame(reservas, columns=colunas)
    df_exibicao = df.copy()
    df_exibicao["Data"] = pd.to_datetime(df_exibicao["Data"]).dt.strftime("%d/%m/%Y")

    st.dataframe(df_exibicao, use_container_width=True, hide_index=True)

    st.divider()
    st.markdown("### 🛠️ Gerenciar Reserva (Editar / Excluir)")

    # Dicionário para selecionar a reserva por ID
    opcoes_reservas = {
        f"ID #{r[0]} — {r[2]} ({r[3]} de {r[4]} às {r[5]})": r[0] 
        for r in reservas
    }
    
    reserva_selecionada_label = st.selectbox("Selecione uma reserva para alterar:", list(opcoes_reservas.keys()))
    reserva_id_sel = opcoes_reservas[reserva_selecionada_label]

    # Busca os dados atuais da reserva escolhida
    dados_reserva = next(r for r in reservas if r[0] == reserva_id_sel)
    # dados_reserva = (id, solicitante, sala_nome, data, ini, fim, finalidade, status)

    tab_editar, tab_excluir = st.tabs(["✏️ Editar Reserva", "🗑️ Excluir Reserva"])

    # --- ABA EDITAR ---
    with tab_editar:
        salas_disponiveis = salas_model.listar_todos()
        opcoes_salas = {f"{s[1]} ({s[3]})": s[0] for s in salas_disponiveis}

        # Converte strings de data/hora de volta para objetos python
        data_atual = datetime.datetime.strptime(dados_reserva[3], "%Y-%m-%d").date() if "-" in dados_reserva[3] else datetime.date.today()
        
        try:
            hora_ini_atual = datetime.datetime.strptime(dados_reserva[4], "%H:%M:%S").time()
            hora_fim_atual = datetime.datetime.strptime(dados_reserva[5], "%H:%M:%S").time()
        except ValueError:
            hora_ini_atual = datetime.time(8, 0)
            hora_fim_atual = datetime.time(10, 0)

        with st.form(f"form_editar_{reserva_id_sel}"):
            nova_sala_label = st.selectbox("Sala", list(opcoes_salas.keys()))
            nova_data = st.date_input("Data", value=data_atual, format="DD/MM/YYYY")
            
            col_i, col_f = st.columns(2)
            with col_i:
                novo_ini = st.time_input("Horário Início", value=hora_ini_atual)
            with col_f:
                novo_fim = st.time_input("Horário Término", value=hora_fim_atual)

            nova_finalidade = st.text_area("Finalidade", value=dados_reserva[6])

            btn_salvar_edicao = st.form_submit_button("Salvar Alterações")

            if btn_salvar_edicao:
                if not nova_finalidade.strip():
                    st.error("Informe a finalidade.")
                elif novo_ini >= novo_fim:
                    st.error("O horário de término deve ser posterior ao início.")
                else:
                    sala_id_nova = opcoes_salas[nova_sala_label]
                    ok, msg = reserva_model.atualizar_reserva(
                        reserva_id_sel, sala_id_nova, nova_data, novo_ini, novo_fim, nova_finalidade
                    )
                    if ok:
                        st.success(msg)
                        st.rerun()
                    else:
                        st.error(msg)

    # --- ABA EXCLUIR ---
    with tab_excluir:
        st.warning(f"Tem certeza que deseja excluir a Reserva **#{reserva_id_sel}**?")
        if st.button("Confirmar Exclusão", type="primary", key=f"btn_del_{reserva_id_sel}"):
            ok, msg = reserva_model.excluir_reserva(reserva_id_sel)
            if ok:
                st.success(msg)
                st.rerun()
            else:
                st.error(msg)