import streamlit as st

def show():
    st.header("🚲 Module Mobilité locale")
    st.write("Analyse de vos trajets domicile-travail.")
    km = st.slider("Distance quotidienne en km", 0, 100, 15)
    transport = st.selectbox("Mode de transport", ["Voiture", "Transports en commun", "Vélo", "Marche"])
    co2 = km * {"Voiture": 0.2, "Transports en commun": 0.05, "Vélo": 0, "Marche": 0}[transport]
    st.metric("Émissions CO₂ estimées (kg/jour)", round(co2, 2))
