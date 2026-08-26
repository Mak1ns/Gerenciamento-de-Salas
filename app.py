import streamlit as st
from views.login_view import render_login
from views.dashboard_view import render_dasboard

st.set_page_config(
    page_title="ÁTILA",
    page_icon="🏫",
    layout="wide"        
)

if "autenticado" not in st.session_state:
    st.session_state["autenticado"] = False
    
if "usuario_logado" not in st.session_state:
    st.session_state["usuario_logado"] = None

def main():
    if not st.session_state["autenticado"]:
        render_login()
    else:
        render_dasboard()
        
if __name__ == "__main__":
    main()