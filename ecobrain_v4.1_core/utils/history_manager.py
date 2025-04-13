import streamlit as st

def show_history():
    st.subheader("📈 Historique et comparaison")
    st.write("Comparaison des scores passés.")
    st.line_chart({"Semaine 1": [3], "Semaine 2": [2.5], "Semaine 3": [2.8], "Semaine 4": [2.3]})
