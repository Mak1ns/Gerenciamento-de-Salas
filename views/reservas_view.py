from datetime import datetime, time
import streamlit as st
from controllers.reservas_controller import ReservasController
from controllers.salas_controller import SalasController


def render_tela_reserva():
    st.subheader("Solicitar nova reserva")

    reservas_controller = ReservasController()
    salas_controller = SalasController()

    usuario_logado = st.session_state.get("usuario_logado", {})

    if isinstance(usuario_logado, dict):
        id_usuario = usuario_logado.get("id", 1)
    else:
        id_usuario = 1

    df_salas = salas_controller.listar_salas()

    if df_salas.empty:
        st.warning("Nenhuma sala encontrada no Sistema")

    opcoes_salas = {
        f"{row['nome_sala']} ({row['bloco_andar']})": row["id_sala"]
        for _, row in df_salas.iterrows
    }

    with st.form("Form Nova Reserva"):
        sala_selecionada = st.selectbox(
            "Selecione a Sala", options=list(opcoes_salas.keys())
        )
        date_reserva = st.date_input(
            "Data da Reserva", min_value=datetime.today()
        )

        col1, col2 = st.columns(2)
        with col1:
            hora_inicio = st.time_input("Hora de Inicio", value=time(8, 0))
        with col2:
            hora_fim = st.time_input("Hora de Término", value=(10, 0))

        btn_confirmar = st.form_submit_button("Confirmar Agendamento")

        if btn_confirmar:
            id_sala = opcoes_salas[sala_selecionada]
            sucesso, msg = reservas_controller.agendar_sala(
                id_usuario, id_sala, date_reserva, hora_inicio, hora_fim
            )

            if sucesso:
                st.success(msg)
                st.rerun()
            else:
                st.error(msg)

    st.markdown("---")
    st.subheader(" Minhas Reservas")

    df_minhas_reservas = reservas_controller.listar_reservas_por_usuario(
        id_usuario
    )

    if not df_minhas_reservas.empty:
        df_exibicao = df_minhas_reservas.merge(df_salas, on="id_sala")
        st.dataframe(
            df_exibicao[
                [
                    "id_reserva",
                    "nome_sala",
                    "data",
                    "hora_inicio",
                    "hora_fim",
                    "status",
                ]
            ].rename(
                columns={
                    "id_reserva": "ID",
                    "nome_sala": "Sala",
                    "data": "Data",
                    "hora_inicio": "Inicio",
                    "hora_fim": "Fim",
                    "status": "Status",
                }
            ),
            use_container_width=True,
        )
    else:
        st.info("Você ainda não possui reservas cadastradas.")