# PAGE powerbi
# Titre de la page
st.header("PowerBI")

# Introduction
st.write("""
Power BI est une solution de **Business Intelligence (BI)** développée par Microsoft.  
Il permet de :
- **Collecter** des données provenant de différentes sources.
- **Transformer et nettoyer** les données pour les rendre exploitables.
- **Créer des visualisations interactives** pour raconter une histoire basée sur les données.
""")

st.write("Le projet Toys & Models vous permettra de naviguer dans l'univers PowerBI, je vous présente une Business Case")

# Créer un trait de séparation
st.markdown("""
    <style>
        hr {
            border: 1px solid #000000;  /* couleur du trait */
            margin: 1px 0;             /* espace avant et après le trait */
            height: 5px;                /* hauteur du trait */
        }
    </style>
    <hr>
    """, unsafe_allow_html=True)

st.write("Cette business Case est sur les métiers de la Data dans le monde (Temps imparti : 1/2 journée)")
st.write("Chaque slide est pilotable via les différents menus déroulants sur la gauche (Exemples : Année / Expérience / (...) afin de rendre interactif les différents tableaux de bords présents")

st.write("")
st.write("")
st.write("Cette slide présente l'évolution des métiers de la data depuis 2020 :")

# Afficher l'image avec une bordure noire fine
st.markdown("""
    <style>
        .image-container img {
            border: 1px solid black;  /* Bordure noire très fine */
            padding: 2px;  /* Un petit espace autour de l'image */
        }
    </style>
    <div class="image-container">
        <img src="https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/images/PowerBI_01.jpg">
    </div>
""", unsafe_allow_html=True)

st.write("")
st.write("")
st.write("Cette slide présente la répartition des salariés à travers leur type de contrat, la taille de l'entreprise, leur mode de travail et leur expérience professionnelle :")
# Afficher l'image avec une bordure noire fine
st.markdown("""
    <style>
        .image-container img {
            border: 1px solid black;  /* Bordure noire très fine */
            padding: 2px;  /* Un petit espace autour de l'image */
        }
    </style>
    <div class="image-container">
        <img src="https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/images/PowerBI_02.jpg">
    </div>
""", unsafe_allow_html=True)

st.write("")
st.write("")
st.write("Cette slide présente la répartition des salariés dans le monde avec notamment les 5 pays avec le plus de profesionnels :")
# Afficher l'image avec une bordure noire fine1
st.markdown("""
    <style>
        .image-container img {
            border: 1px solid black;  /* Bordure noire très fine */
            padding: 2px;  /* Un petit espace autour de l'image */
        }
    </style>
    <div class="image-container">
        <img src="https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/images/PowerBI_03.jpg">
    </div>
""", unsafe_allow_html=True)

st.write("")
st.write("")
st.write("Cette slide présente la répartition des 10 métiers les plus dominants (nombre de salariés et salaire moyen) par métier et par expérience (durant l'année 2020) :")
# Afficher l'image avec une bordure noire fine
st.markdown("""
    <style>
        .image-container img {
            border: 1px solid black;  /* Bordure noire très fine */
            padding: 2px;  /* Un petit espace autour de l'image */
        }
    </style>
    <div class="image-container">
        <img src="https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/images/PowerBI_04.jpg">
    </div>
""", unsafe_allow_html=True)

st.write("")
st.write("")
st.write("Cette slide présente la répartition des salariés à travers leur type de contrat, la taille de l'entreprise, leur mode de travail et leur expérience professionnelle (durant l'année 2024) :")
# Afficher l'image avec une bordure noire fine
st.markdown("""
    <style>
        .image-container img {
            border: 1px solid black;  /* Bordure noire très fine */
            padding: 2px;  /* Un petit espace autour de l'image */
        }
    </style>
    <div class="image-container">
        <img src="https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/images/PowerBI_05.jpg">
    </div>
""", unsafe_allow_html=True)
