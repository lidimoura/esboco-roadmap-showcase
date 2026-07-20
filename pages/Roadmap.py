import streamlit as st
from utils.i18n import t

def app():
    st.title(t("roadmap_title"))
    st.markdown(t("roadmap_intro"))

    st.markdown(f"## {t("week1_title")}")
    st.info(t("week1_focus"))
    st.markdown(t("week1_tasks"))

    st.markdown(f"## {t("week2_title")}")
    st.info(t("week2_focus"))
    st.markdown(t("week2_tasks"))

    st.markdown(f"## {t("week3_title")}")
    st.info(t("week3_focus"))
    st.markdown(t("week3_tasks"))

    st.markdown(f"## {t("week4_title")}")
    st.info(t("week4_focus"))
    st.markdown(t("week4_tasks"))

    st.markdown(f"--- \n### {t("current_progress_title")}")
    progress_percent = 0.25 # Exemplo: 25% para o final da Semana 1
    st.progress(progress_percent)
    st.write(t("progress_text", progress_percent=progress_percent))
