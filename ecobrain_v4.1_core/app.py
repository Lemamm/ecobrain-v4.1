import streamlit as st
from modules import mobility, scoring
from utils import history_manager

st.set_page_config(page_title="EcoBrain v4.1", page_icon="🌍", layout="wide")

with open("assets/banner.html", encoding="utf-8") as f:
    st.markdown(f.read(), unsafe_allow_html=True)


st.sidebar.title("🌱 Navigation")
page = st.sidebar.radio("Aller à", ["Accueil", "Mobilité", "Éco-score", "Historique"])

if page == "Accueil":
    st.markdown("### Bienvenue dans EcoBrain v4.1 – L'intelligence éco-responsable")
    st.image("assets/logo.png", width=150)
    st.write("Sélectionnez un module dans la barre latérale pour commencer.")

elif page == "Mobilité":
    mobility.show()

elif page == "Éco-score":
    score, details = scoring.calculate_score()
    st.metric("Éco-score global", score)
    st.write(details)

elif page == "Historique":
    history_manager.show_history()
