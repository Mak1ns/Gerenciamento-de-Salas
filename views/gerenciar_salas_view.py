import streamlit as st
import sqlite3

def conectar():
    return sqlite3.connect("reservas.db")

def render_gerenciar_salas():
    st.markdown("<h2 style='color: #FF6B00;'>⚙️ Gerenciar Salas</h2>", unsafe_allow_html=True)
    st.write("Cadastre novas salas ou remova as existentes do sistema.")

    # Cadastro de Nova Sala
    with st.form("form_cadastrar_sala"):
        st.subheader("➕ Adicionar Nova Sala")

        nome = st.text_input("Nome da Sala / Laboratório")
        col1, col2 = st.columns(2)
        with col1:
            capacidade = st.number_input("Capacidade (pessoas)", min_value=1, value=30)
            projetor = st.selectbox("Possui Projetor?", ["Sim", "Não"])
        with col2:
            localizacao = st.text_input("Localização / Bloco", placeholder="Ex: Bloco A")
            computadores = st.number_input("Qtd. de Computadores", min_value=0, value=0)

        submit_cadastrar = st.form_submit_button("Salvar Sala")

        if submit_cadastrar:
            if nome.strip() and localizacao.strip():
                try:
                    conexao = conectar()
                    cursor = conexao.cursor()
                    cursor.execute("""
                        INSERT INTO salas (nome, capacidade, localizacao, projetor, computadores, status)
                        VALUES (?, ?, ?, ?, ?, 'Disponível')
                    """, (nome, capacidade, localizacao, projetor, computadores))
                    conexao.commit()
                    conexao.close()
                    st.success(f"Sala '{nome}' cadastrada com sucesso!")
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao cadastrar sala: {e}")
            else:
                st.warning("Preencha o nome e a localização da sala.")

    st.divider()

    # Listagem e Exclusão de Salas Cadastradas
    st.subheader("📋 Salas Cadastradas no Sistema")

    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, capacidade, localizacao, projetor, computadores FROM salas")
        salas = cursor.fetchall()
        conexao.close()

        if salas:
            for sala in salas:
                sala_id, nome, capacidade, localizacao, projetor, computadores = sala

                with st.container():
                    col_info, col_btn = st.columns([4, 1])
                    with col_info:
                        st.markdown(f"**🏢 {nome}** ({localizacao})")
                        st.caption(f"Capacidade: {capacidade} | Projetor: {projetor} | Computadores: {computadores}")

                    with col_btn:
                        if st.button("Excluir", key=f"del_sala_{sala_id}"):
                            try:
                                conexao_del = conectar()
                                cursor_del = conexao_del.cursor()
                                cursor_del.execute("SELECT COUNT(*) FROM reservas WHERE sala_id = ?", (sala_id,))
                                tem_reservas = cursor_del.fetchone()[0]
                                if tem_reservas > 0:
                                    st.warning(f"'{nome}' tem {tem_reservas} reserva(s) vinculada(s). Exclusão bloqueada.")
                                else:
                                    cursor_del.execute("DELETE FROM salas WHERE id = ?", (sala_id,))
                                    conexao_del.commit()
                                    st.success(f"Sala '{nome}' removida!")
                                    st.rerun()
                                conexao_del.close()
                            except Exception as e:
                                st.error(f"Erro ao excluir sala: {e}")
                    st.markdown("---")
        else:
            st.info("Nenhuma sala cadastrada no momento.")

    except Exception as e:
        st.error(f"Erro ao carregar as salas: {e}")