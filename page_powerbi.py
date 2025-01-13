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


st.image("https://i72.servimg.com/u/f72/20/11/38/84/2025_013.jpg")



st.write("Cette business Case est sur les métiers de la Data (Temps imparti : 1/2 journée)")
# Liste des images pour la navigation avec flèches
images = [
    "https://i72.servimg.com/u/f72/20/11/38/84/2025_013.jpg",
    "https://i72.servimg.com/u/f72/20/11/38/84/2025_010.jpg",
    "https://i72.servimg.com/u/f72/20/11/38/84/2025_014.jpg",
    "https://i72.servimg.com/u/f72/20/11/38/84/2025_017.jpg",
    "https://i72.servimg.com/u/f72/20/11/38/84/2025_016.jpg"
    ]

# Fonction pour changer l'image
def next_image():
    if st.session_state.image_index < len(images) - 1:
        st.session_state.image_index += 1

def prev_image():
    if st.session_state.image_index > 0:
        st.session_state.image_index -= 1

# Ajouter les boutons pour naviguer
col1, col2, col3 = st.columns([1, 4, 1])  # Répartition de l'espace avec une colonne vide pour "Suivante"

# Le bouton "Précédente" reste à gauche
with col1:
    if st.button("⬅ Précédente"):
        prev_image()

# Le bouton "Suivante" est à droite
with col3:
    if st.button("Suivante ➡"):
        next_image()

# Index de l'image actuellement affichée
if 'image_index' not in st.session_state:
    st.session_state.image_index = 0

# Affichage de l'image actuelle (réduite et cliquable pour voir en grand)
image_url = images[st.session_state.image_index]
st.markdown(
    f"""
    <div style="display: flex; justify-content: center;">
    <a href="{image_url}" target="_blank">
        <img src="{image_url}">
    </a>
    """,
    unsafe_allow_html=True
)