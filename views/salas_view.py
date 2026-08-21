import streamlit as st

from controllers.salas_controller import SalasController

def show_salas():
    
    controller = SalasController()

    st.title("🏫 Salas de Aula")

    st.write("Consulta de Sala de Aula.")

    st.divider()

    nome_sala = st.text_input(
        "Pesquisar sala",
        placeholder="Digite nome da sala..."
    )

    salas = controller.buscar_sala(nome_sala)

    st.subheader("Salas encontradas")

    st.dataframe(
        salas,
        use_container_width=True,
        hide_index=True
    )

    st.caption(
        f"{len(salas)} sala(s) encontrada(s)."
    )