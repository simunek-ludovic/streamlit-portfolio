import streamlit as st


st.set_page_config(
    page_title="Mon Portfolio",  # Titre de la page
    page_icon="📈",
    layout="wide",  # Utilise toute la largeur de l'écran
    initial_sidebar_state="expanded"  # Affiche la barre latérale par défaut
)
st.sidebar.markdown("<p style='margin-bottom: 0;'><img src='https://img.icons8.com/ios-filled/16/000000/user.png'/> : <strong>SIMUNEK Ludovic</strong></p>", unsafe_allow_html=True)  # Nom avec icône de personnage
st.sidebar.markdown("<p style='margin-bottom: 0;'><img src='https://img.icons8.com/ios-filled/16/000000/phone.png'/> : 06 51 52 42 33</p>", unsafe_allow_html=True)  # Téléphone avec icône
st.sidebar.markdown("<p style='margin-bottom: 0;'><img src='https://img.icons8.com/ios-filled/16/000000/email.png'/> : <a href='mailto:ludovic@simunek.fr'> ludovic@simunek.fr</a></p>", unsafe_allow_html=True)  # Email avec icône et lien mailto
st.sidebar.markdown("<br>", unsafe_allow_html=True)

# Chemin du fichier où le compteur sera sauvegardé
compteur_file = "compteur.txt"

# Fonction pour lire la valeur du compteur depuis le fichier
def lire_compteur():
    try:
        with open(compteur_file, "r") as file:
            compteur = int(file.read())
    except FileNotFoundError:
        compteur = 0  # Si le fichier n'existe pas, commencer avec 0
    return compteur

# Fonction pour enregistrer la valeur du compteur dans le fichier
def enregistrer_compteur(compteur):
    with open(compteur_file, "w") as file:
        file.write(str(compteur))

# Lecture du compteur à partir du fichier
compteur = lire_compteur()

# Créer le bouton "J'aime" dans la colonne du milieu
if st.sidebar.button("J'aime"):
    compteur += 1  # Incrémentation du compteur
    enregistrer_compteur(compteur)  # Enregistrer la nouvelle valeur dans le fichier

# Affichage du compteur dans la sidebar
st.sidebar.markdown(
    f"<p style='text-align: left'>Nombre de Likes : {compteur}</p>", 
    unsafe_allow_html=True
)

# Titre principal du site avec la taille de police ajustée
st.title("Mon Portfolio de Data Analyst")

# Barre de navigation
page_selection = st.sidebar.radio("Choisissez une page :", ["Accueil", "Git / Github", "Python", "PowerBI", "SQL", "Streamlit", "Projets"], index=0)

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
    st.write("Ludovic")


elif page_selection == "Git / Github":
    # Exécuter le code du fichier python en utilisant exec()
    with open("page_github.py", "r", encoding="utf-8") as f:
        content = f.read()
    exec(content)

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

