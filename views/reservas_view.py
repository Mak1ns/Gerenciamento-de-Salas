import streamlit as st
import datetime
from models.salas_model import SalasModel
from models.reservas_model import ReservasModel

reserva_model = ReservasModel()

def render_reserva_salas():
    st.markdown("<h2 style='color: #FFA500;'>🗓️ Solicitar Nova Reserva</h2>", unsafe_allow_html=True)
    st.write("Preencha os campos abaixo para realizar o agendamento de uma sala.")

    usuario_logado = st.session_state.get("usuario_logado", {})
    if isinstance(usuario_logado, dict):
        usuario_id = usuario_logado.get("id", 1)
        nome_usuario = usuario_logado.get("nome", "Usuário")
    else:
        usuario_id = 1
        nome_usuario = str(usuario_logado)

    salas_model = SalasModel()
    salas = salas_model.listar_salas_disponiveis()

    if not salas:
        salas_todas = salas_model.listar_todos()
        if not salas_todas:
            st.error("Nenhuma sala cadastrada no banco de dados.")
            return
        salas = [(s[0], s[1], s[2], s[3], s[4], s[5]) for s in salas_todas]

    opcoes_salas = {
        f"{sala[1]} — {sala[3]} (Capacidade: {sala[2]} pessoas)": {
            "id": sala[0],
            "tem_projetor": bool(sala[4]),
            "tem_caixa_som": bool(sala[5]),
        }
        for sala in salas
    }

    sala_label = st.selectbox("Selecione a Sala", list(opcoes_salas.keys()))
    sala_info = opcoes_salas[sala_label]

    col_projetor, col_som = st.columns(2)
    col_projetor.markdown(f"📽️ **Tem projetor:** {'✅ Sim' if sala_info['tem_projetor'] else '❌ Não'}")
    col_som.markdown(f"🔊 **Caixa de som:** {'✅ Sim' if sala_info['tem_caixa_som'] else '❌ Não'}")

    with st.form("form_solicitar_reserva"):
        st.info(f"**Solicitante:** {nome_usuario}")
        
        col_data, col_vazia = st.columns([1, 1])
        with col_data:
        
            data_reserva = st.date_input(
                "Data da Reserva", 
                min_value=datetime.date.today(),
                format="DD/MM/YYYY"
            )
        
        col_ini, col_fim = st.columns(2)
        with col_ini:
            horario_inicio = st.time_input("Horário de Início", datetime.time(8, 0))
        with col_fim:
            horario_fim = st.time_input("Horário de Término", datetime.time(10, 0))
        
        finalidade = st.text_area(
            "Finalidade da Reserva", 
            placeholder="Ex: Aula prática de Engenharia do Conhecimento, Apresentação de TCC, etc."
        )
        
        btn_submeter = st.form_submit_button("Confirmar Solicitação de Reserva")

        if btn_submeter:
            if not finalidade.strip():
                st.error("Por favor, informe a finalidade da reserva.")
            elif horario_inicio >= horario_fim:
                st.error("O horário de término deve ser posterior ao horário de início.")
            else:
                sala_id_selecionada = sala_info["id"]
                
                reserva_model = ReservasModel()
                sucesso, mensagem = reserva_model.criar_reserva(
                    professor_id=usuario_id,
                    sala_id=sala_id_selecionada,
                    data=data_reserva,
                    horario_inicio=horario_inicio,
                    horario_fim=horario_fim,
                    finalidade=finalidade
                )

                if sucesso:
                    st.success(f"✅ {mensagem}")
                else:
                    st.error(f"❌ {mensagem}")