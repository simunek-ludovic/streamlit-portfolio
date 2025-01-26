
import streamlit as st

# Configuration de la page Streamlit
st.set_page_config(
    page_title="Mon Portfolio",  # Titre de la page
    page_icon="📈",
    layout="wide",  # Utilise toute la largeur de l'écran
    initial_sidebar_state="expanded"  # Affiche la barre latérale par défaut
)

# Barre de navigation à gauche avec modification du style de la barre de recherche
with st.sidebar:
    # Paramétrer la largeur bloquante de la sidebar
    st.markdown(
        """
        <style>
            section[data-testid="stSidebar"] {
                width: 300px !important; 
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Création d'un expander dans la barre latérale
with st.sidebar.expander("Contactez moi", expanded=False):  # Tu peux ajuster le titre du panneau
    # Afficher l'image de profil et ton nom dans l'expander
    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 1rem;">
            <img src="https://media.licdn.com/dms/image/v2/D4E03AQGomjyiBWFb1A/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1701427770915?e=2147483647&v=beta&t=vMUouV4yfe2IRYuX3psMCp9iJv_HIgvNbiT1lH-h-OU" 
                 alt="Photo de profil" style="border-radius: 50%; width: 100px; height: 100px; margin-bottom: 10px;">
        </div>
        <p style="margin: 0; font-weight: bold; font-size: 14px;">
            <img src="https://img.icons8.com/ios-filled/16/000000/user.png"/> : <strong>SIMUNEK Ludovic</strong>
        </p>
        """,
        unsafe_allow_html=True
    )
    
    # Téléphone avec icône
    st.markdown("<p style='margin-bottom: 0;'><img src='https://img.icons8.com/ios-filled/16/000000/phone.png'/> : 06 51 52 42 33</p>", unsafe_allow_html=True)

    # Email avec icône et lien mailto
    st.markdown("<p style='margin-bottom: 0;'><img src='https://img.icons8.com/ios-filled/16/000000/email.png'/> : <a href='mailto:ludovic@simunek.fr'> ludovic@simunek.fr</a></p>", unsafe_allow_html=True)

    # Lien vers le CV avec icônes de lecture et de téléchargement
    st.markdown(""" 
    <p style='margin-bottom: 0;'>
    <img src="https://img.icons8.com/ios-glyphs/16/000000/resume.png" alt="resume" /> CV : 
    <a href='https://github.com/simunek-ludovic/streamlit-portfolio/blob/main/docs/CV%20-%20SIMUNEK%20Ludovic.pdf' target='_blank'>Lire</a> | 
    <a href='https://github.com/simunek-ludovic/streamlit-portfolio/raw/main/docs/CV%20-%20SIMUNEK%20Ludovic.pdf' download> Télécharger</a>
    </p>
    """, unsafe_allow_html=True)

    # LinkedIn avec icône et lien
    st.markdown("<p style='margin-bottom: 0;'><img src='https://img.icons8.com/ios-filled/16/000000/linkedin.png'/> : <a href='https://www.linkedin.com/in/ludovic-simunek/' target='_blank'>Mon LinkedIn</a></p>", unsafe_allow_html=True)

    # GitHub avec icône et lien
    st.markdown("<p style='margin-bottom: 0;'><img src='https://img.icons8.com/ios-glyphs/16/000000/github.png'/> : <a href='https://github.com/simunek-ludovic' target='_blank'>Mon GitHub</a></p>", unsafe_allow_html=True)


st.sidebar.markdown("<br>", unsafe_allow_html=True)

# Titre principal du site avec la taille de police ajustée
st.title("Mon Portfolio de Data Analyst")

# Barre de navigation
page_selection = st.sidebar.radio("Choisissez une thématique :", ["Accueil", "Git / Github", "Python", "PowerBI", "SQL", "Streamlit", "Projets"], index=0)

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
    st.write("Et si besoin, je reste à votre entière disposition.")
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

