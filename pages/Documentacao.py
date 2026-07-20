import streamlit as st
from utils.i18n import t

def app():
    st.title(t("docs_menu"))
    st.write("Página de Documentação / Documentation Page")
