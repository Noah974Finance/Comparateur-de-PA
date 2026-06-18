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
    padding-top: 0rem !important;
    padding-bottom: 0rem !important;
    padding-left: 0rem !important;
    padding-right: 0rem !important;
    max-width: 100% !important;
}
.main, .block-container, div[data-testid="stHtml"] {
    background-color: #080b11 !important;
    overflow: hidden !important;
}
iframe {
    width: 100% !important;
    height: 100vh !important;
    background-color: #080b11 !important;
    border: none;
    display: block;
}
div[data-testid="stHtml"] {
    height: 100vh !important;
}
</style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

# Get query parameters to handle navigation
page = st.query_params.get("page", "comparateur")

# Choose which file to read based on page parameter
if page == "tarifs":
    filename = "prix.html"
else:
    filename = "index.html"

# Lecture et affichage du comparateur HTML
try:
    with open(filename, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # Affichage du comparateur dans un iframe dynamique et scrollable
    components.html(html_content, height=1000, scrolling=True)
except Exception as e:
    st.error(f"Erreur lors du chargement de la page ({filename}) : {e}")
