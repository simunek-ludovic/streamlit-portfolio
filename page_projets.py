# PAGE projets
import streamlit as st

# Barre de navigation
page_selection = st.sidebar.selectbox("Choisissez un des projets :", ["Toys & Models", "Recommandations de films","La Boussole Lilloise"], index=0)

if page_selection == "Recommandations de films":
    st.header("Recommandations de films")
    # Exécuter le code du fichier python en utilisant exec()
    with open("projet_recommandations_films.py", "r", encoding="utf-8") as f:
        content = f.read()
    exec(content)

elif page_selection == "Toys & Models":
    st.header("Projet Toys & Models")
    # Exécuter le code du fichier python en utilisant exec()
    with open("projet_toys&models.py", "r", encoding="utf-8") as f:
        content = f.read()
    exec(content)


elif page_selection == "La Boussole Lilloise":
    st.header("La Boussole Lilloise")
    # Exécuter le code du fichier python en utilisant exec()
    with open("projet_boussole_lilloise.py", "r", encoding="utf-8") as f:
        content = f.read()
    exec(content)