import streamlit as st
from streamlit_option_menu import option_menu
from utils.i18n import set_language, t, get_lang

# Configure page early
st.set_page_config(page_title="PowerPolis - EnergiAI", layout="wide", initial_sidebar_state="expanded")

# Initialize language selector (ensures st.session_state.lang exists before pages import)
set_language()

# Importar as páginas (after initializing language)
from pages import Analise, Roadmap, Equipe, Documentacao

# --- Configurações de Estilo --- #
st.markdown("""
<style>
    .css-1d391kg { padding-top: 35px; }
    .stButton>button { width: 100%; }
    .stMetric { background-color: #1e293b; padding: 20px; border-radius: 10px; text-align: center; }
    .stMetric label { font-size: 1.2em; color: #f8fafc; }
    .stMetric .value { font-size: 2.5em; color: #10b981; font-weight: bold; }
    .stMetric .delta { font-size: 1em; color: #f8fafc; }
</style>
""", unsafe_allow_html=True)

# --- Sidebar --- #
with st.sidebar:
    st.image("https://github.com/lidimoura/esboco-roadmap-showcase/blob/main/assets/logo.png?raw=true", width=150) # Placeholder para o logo

    # `set_language()` was already called above to initialize session state and render the language selector.
    current_lang = get_lang()

    selected = option_menu(
        menu_title=t('app_title'),
        options=[t('home_menu'), t('analysis_menu'), t('roadmap_menu'), t('team_menu'), t('docs_menu')],
        icons=["house", "graph-up", "map", "people", "book"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#0f172a"},
            "icon": {"color": "#10b981", "font-size": "18px"},
            "nav-link": {"font-size": "18px", "text-align": "left", "margin": "0px", "--hover-color": "#1e293b"},
            "nav-link-selected": {"background-color": "#10b981", "color": "#0f172a"},
        }
    )

# --- Páginas --- #
if selected == t('home_menu'):
    st.title(t('app_title'))
    st.markdown(f"""
    {t('home_subtitle')}
    
    {t('home_intro_text')}
    
    --- 

    ### {t('mission_title')}
    {t('mission_text')}
    """)
    
    st.markdown(f"## {t('status_title')}")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label=t('training_records'), value="50.000+", delta=t('training_records_delta'))
    with col2:
        st.metric(label=t('ml_models_tested'), value="3", delta=t('ml_models_tested_delta'))
    with col3:
        st.metric(label=t('team_members'), value="9", delta=t('team_members_delta'))
    
    st.markdown(f"""
    --- 

    ### {t('what_you_can_do_title')}
    - {t('what_you_can_do_1')}
    - {t('what_you_can_do_2')}
    - {t('what_you_can_do_3')}
    - {t('what_you_can_do_4')}
    - {t('what_you_can_do_5')}
    """)

elif selected == t('analysis_menu'):
    Analise.app()

elif selected == t('roadmap_menu'):
    Roadmap.app()

elif selected == t('team_menu'):
    Equipe.app()

elif selected == t('docs_menu'):
    Documentacao.app()
