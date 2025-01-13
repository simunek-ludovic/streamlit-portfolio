import streamlit as st

# Barre de navigation
page_selection = st.sidebar.selectbox("Choisissez un des projets :", ["Recommandations de films", "Toys & Models"], index=0)

# Affichage de la page sélectionnée
if page_selection == "Toys & Models":
    st.header("Projets Toys & Models")
    # Exécuter le code du fichier python en utilisant exec()
    with open("projet_toys&models.py", "r", encoding="utf-8") as f:
        content = f.read()
    exec(content)

elif page_selection == "Recommandations de films":
    st.header("Recommandations de films")
    # Exécuter le code du fichier python en utilisant exec()
    with open("projet_recommandations_films.py", "r", encoding="utf-8") as f:
        content = f.read()
    exec(content)
