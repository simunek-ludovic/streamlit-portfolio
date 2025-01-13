import streamlit as st

st.set_page_config(
    page_title="Mon Portfolio",  # Titre de la page
    layout="wide",  # Utilise toute la largeur de l'écran
    initial_sidebar_state="expanded"  # Affiche la barre latérale par défaut
)


# Titre principal du site avec la taille de police ajustée
st.title("Ludovic Simunek - Mon Portfolio de Data Analyst")

# Barre de navigation
page_selection = st.sidebar.radio("Choisissez une page :", ["Accueil", "Python", "PowerBI", "SQL", "Streamlit", "Projets"], index=0)

# Affichage de la page sélectionnée
if page_selection == "Accueil":
    # Résumé
# Utilisation de f-string pour formater la taille de la police dans le texte
    # st.header("Ma présentation")
    st.write("Fort de plus de 20 ans d’expérience en ressources humaines et en gestion des données, je me lance depuis septembre 2024 dans une reconversion professionnelle en tant que Data Analyst.")
    st.write("Cette transition est motivée par mon désir d'exploiter mes compétences analytiques et techniques pour aider les organisations à tirer parti de leurs données et à éclairer leurs décisions stratégiques.")
    st.write("En tant que spécialiste d’Excel, VBA et Access, j'ai acquis une solide expertise dans l’automatisation et l’organisation des données.")
    st.write("Ces compétences, qui m'ont permis de concevoir des outils d’analyse performants, sont désormais renforcées par une maîtrise des techniques modernes d'analyse de données, notamment en Python, SQL et Power BI.")
    st.write("Cette reconversion me permet de combiner mon expérience de gestion des données avec les outils actuels pour répondre aux enjeux actuels des entreprises.")
    st.write("Doté d’un esprit rigoureux et orienté solutions, je suis déterminé à accompagner les organisations dans l’exploitation de leurs données et à apporter une valeur ajoutée grâce à mes nouvelles compétences de Data Analyst.")
    st.write("N'hésitez pas à naviguer sur les différents projets qui illustrent la partie technique de mon activité.")
    st.write("Ludovic Simunek")

    st.header("Contactez-moi")
    st.write("Mail : ludovic@simunek.fr")
    st.write("Téléphone : 06 51 52 42 33")
    st.write("https://www.linkedin.com/in/ludovic-simunek/")

elif page_selection == "Python":
    # Exécuter le code du fichier python en utilisant exec()
    with open("page_python.py", "r", encoding="utf-8") as f:
        content = f.read()
    exec(content)

elif page_selection == "PowerBI":
    # Exécuter le code du fichier python en utilisant exec()
    with open("page_powerbi.py", "r", encoding="utf-8") as f:
        content = f.read()
    exec(content)

elif page_selection == "SQL":
    # Exécuter le code du fichier python en utilisant exec()
    with open("page_sql.py", "r", encoding="utf-8") as f:
        content = f.read()
    exec(content)

elif page_selection == "Streamlit":
    # Exécuter le code du fichier python en utilisant exec()
    with open("page_streamlit.py", "r", encoding="utf-8") as f:
        content = f.read()
    exec(content)
    
elif page_selection == "Projets":
    # Exécuter le code du fichier python en utilisant exec()
    with open("page_projets.py", "r", encoding="utf-8") as f:
        content = f.read()
    exec(content)
