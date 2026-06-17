import streamlit as st
import streamlit.components.v1 as components

# Configuration de la page
st.set_page_config(
    page_title="Comparateur PA — Plateformes Agréées Facturation Électronique 2026",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Suppression des éléments d'interface par défaut de Streamlit pour un rendu propre et immersif
hide_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
div[data-testid="stDecoration"] {visibility: hidden;}
div[data-testid="stToolbar"] {visibility: hidden;}
button[title="View source code"] {visibility: hidden;}
/* Reset margins of the main block to allow maximum display area */
.block-container {
    padding-top: 0rem;
    padding-bottom: 0rem;
    padding-left: 0rem;
    padding-right: 0rem;
}
iframe {
    width: 100% !important;
    border: none;
}
</style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

# Lecture et affichage du comparateur HTML
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # Affichage du comparateur dans un iframe dynamique et scrollable
    components.html(html_content, height=1500, scrolling=True)
except Exception as e:
    st.error(f"Erreur lors du chargement du comparateur : {e}")
