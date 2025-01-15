# Liste des bibliothèque à importer :
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os
import duckdb
import datetime
from datetime import datetime, timedelta
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st


# Définir la configuration de la page
st.set_page_config(
    page_title="Système de recommandations",
    page_icon="🎬",
    layout="wide",  # Mettre "wide" pour étendre la page
    initial_sidebar_state="expanded"  # La sidebar sera toujours affichée au départ
)

# Charger le fichier TSV dans un DataFrame
url = "https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/csv/df_films.tsv"
df = pd.read_csv(url, sep="\t")  # On indique que les colonnes sont séparées par une tabulation

# Variables
nb_acteurs = 5  # Nombre d'acteurs à récupérer
film_id = "tt1064932"  # ID du film à filtrer

# Filtrer le DataFrame par ID_Film et récupérer les X premiers acteurs
filtre_acteurs = df.loc[df['ID_film'] == film_id, 'Top_Acteurs'] \
                    .str.split(', ').str[:nb_acteurs].str.join(', ').values

# Résultat final
result = filtre_acteurs[0] if len(filtre_acteurs) > 0 else "Film non trouvé"
st.write(result)

# Pondération des colonnes
poids = {
    "Note_moyenne_norm": 0.5, "Nb_votants_norm": 0.5, "Annee_sortie_norm": 0.5, "Duree_minutes_norm": 0.5,
    "Comedie": 3, "Documentaire": 3, "Famille": 3, "Romance": 3, "Action": 3, "Thriller": 3,
    "Fantaisie": 3, "Horreur": 3, "Aventure": 3, "Animation": 3,
    "DIR_": 30, "ACT_": 35  # Poids pour les colonnes des directeurs et acteurs
}

# Filtrer les colonnes basées sur le dictionnaire de poids
colonnes_utiles = [
    col for col in df.columns
    if col in poids or col.startswith("DIR_") or col.startswith("ACT_")
]

# Appliquer les pondérations
for col in colonnes_utiles:
    if col in poids:  # Pondération des colonnes générales
        df[col] = df[col] * poids[col]
    elif col.startswith("DIR_"):  # Pondération des colonnes des directeurs
        df[col] = df[col] * poids["DIR_"]
    elif col.startswith("ACT_"):  # Pondération des colonnes des acteurs
        df[col] = df[col] * poids["ACT_"]

# Filtrer le DataFrame pour ne garder que les colonnes utiles
df_filtre = df[colonnes_utiles]

# Calcul de la similarité cosinus
cos_sim = cosine_similarity(df_filtre)

# Fonction de recommandation
def recommander_films(titre, n):
    try:
        # Récupérer l'index du film
        film_index = df[df["Titre_original"] == titre].index[0]

        # Obtenir les similarités cosinus et trier
        similarites = cos_sim[film_index]
        indices_similaires = np.argsort(similarites)[-n-1:-1][::-1]  # Top-n films similaires

        # Retourner les titres et les liens
        return [
            (df.iloc[i]["Titre_original"], df.iloc[i]["Lien_Affiche"]) for i in indices_similaires
        ]
    except IndexError:
        return f"Le film '{titre}' est introuvable dans le DataFrame."

# Exemple d'utilisation
titre_film = "Taxi 2"
n_similaire = 5

films_similaires = recommander_films(titre_film, n_similaire)

#################################

with st.sidebar.expander("Choisissez vos genres", expanded=False):
# Paramétrer la largeur bloquante de la sidebar
    st.markdown(
        """
        <style>
            section[data-testid="stSidebar"] {
                width: 350px !important; 
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Créer deux colonnes dans l'expander pour afficher les checkboxes
    col1, col2 = st.columns(2)

    # Afficher les checkboxes dans les colonnes
    with col1:
        show_action = st.checkbox("Action", value=True)
        show_animation = st.checkbox("Animation", value=True)
        show_documentaire = st.checkbox("Documentaire", value=True)        
        show_fantaisie = st.checkbox("Fantaisie", value=True)
        show_romance = st.checkbox("Romance", value=True)
    with col2:        
        show_aventure = st.checkbox("Aventure", value=True)
        show_comedie = st.checkbox("Comédie", value=True)    
        show_famille = st.checkbox("Famille", value=True)
        show_horreur = st.checkbox("Horreur", value=True)
        show_thriller = st.checkbox("Thriller", value=True)

    # Créer un masque pour chaque genre
    masque = []
    if show_action:
        masque.append(df["Action"] !=0)
    if show_animation:
        masque.append(df["Animation"] !=0)
    if show_famille:
        masque.append(df["Documentaire"] !=0)
    if show_fantaisie:
        masque.append(df["Fantaisie"] !=0)
    if show_romance:
        masque.append(df["Romance"] !=0)
    if show_aventure:
        masque.append(df["Aventure"] !=0)
    if show_comedie:
        masque.append(df["Comedie"] !=0)
    if show_documentaire:
        masque.append(df["Famille"] !=0)
    if show_horreur:
        masque.append(df["Horreur"] !=0)
    if show_thriller:
        masque.append(df["Thriller"] !=0)

    # Appliquer le masque sur le dataframe : cela signifie que l'on filtre les lignes qui correspondent à l'un des genres sélectionnés
    if masque:
        filtre = masque[0]
        for m in masque[1:]:
            filtre = filtre | m  # Utiliser 'ou' logique pour combiner les filtres

        # Filtrer le dataframe selon le masque combiné
        df_filtre = df[filtre]

        # Créer une liste des titres correspondant au genre sélectionné
        liste_titres = df_filtre["Titre_original"].tolist()
    else:
        liste_titres = []  # Si aucun genre n'est sélectionné, la liste est vide

# Afficher la liste des titres filtrés
st.write(f"Films dans la base de données : {len(liste_titres)}")

liste_titres.sort()  # Tri alphabétique de la liste
# Vérifier le nombre de films dans la liste
if len(liste_titres) == 0:
    st.error("Aucun film ne correspond aux filtres actuels.")
    st.stop()  # Arrêter l'exécution si aucun film n'est trouvé

else:
    liste_titres.sort()  # Tri alphabétique de la liste
    # Sélectionner un film sans valeur par défaut
if len(liste_titres) == 0:
    st.stop()  # Arrêter l'exécution si aucun film n'est dans la liste

liste_titres.insert(0, "")
titre_film = st.selectbox("**Entrez le titre du film :**", liste_titres)

# Vérifier si un film a été sélectionné
if titre_film == "":
    st.stop()  # Arrêter l'exécution si aucun film n'est sélectionné
else:
    film_saisi = df[df["Titre_original"] == titre_film]
    with st.expander("Affiche du Film choisi", expanded=True):

        # Affichage de l'image du film (colonne 'lien' contenant l'URL de l'image)
        if titre_film:
            try:
                image_url = df[df["Titre_original"] == titre_film]["Lien"].values[0]
                st.markdown(f"<div style='text-align:center; font-size:{st.session_state.taille_texte}px;'></div>", unsafe_allow_html=True)
                st.markdown(f"""
                    <style>
                    .image-container {{
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100%;
                    }}
                    .image-bordure {{
                        border: 1px solid #000000;  /* Bordure de 1px de couleur noire */
                        padding: 0px;  /* Espacement interne pour que la bordure ne touche pas l'image */
                        border-radius: 10px;  /* Coins arrondis pour un effet plus doux */
                        max-height: 350px;  /* Hauteur maximale de l'image */
                        object-fit: cover;  /* L'image se redimensionne tout en conservant ses proportions */
                        margin-bottom: 10px;  /* Espace de 20px sous l'image */
                    }}
                    </style>
                    <div class="image-container">
                        <img src="{image_url}" class="image-bordure">
                    </div>
                """, unsafe_allow_html=True)
            except IndexError:
                st.error(f"Le film '{titre_film}' n'existe pas dans la base de données.")

    with st.sidebar.expander("Choisissez éléments TMDB dans résultats", expanded=False):
        # Curseur pour ajuster le nombre de films similaires, avec plage de 1 à 20
        n_similaire = st.slider(
            "Nombre de films similaires souhaités :", 
            min_value=1,  # Valeur minimale
            max_value=10,  # Valeur maximale
            value=5,  # Valeur par défaut
            step=1  # Incrément de 1
        )
        # Nouveau curseur pour ajuster le nombre de films à afficher par ligne
        n_par_ligne = st.slider(
            "Nombre de films à afficher par ligne :", 
            min_value=1,  # Valeur minimale
            max_value=5,  # Valeur maximale
            value=5,  # Valeur par défaut
            step=1  # Incrément de 1
        )

        # Créer deux colonnes dans l'expander pour afficher les checkboxes
        col1, col2 = st.columns(2)

        # Afficher les checkboxes dans les colonnes
        with col1:
            show_image = st.checkbox("Affiche", value=True)
            show_video = st.checkbox("Vidéo", value=True)
            show_realisateur = st.checkbox("Réalisateur", value=True)
            show_date_sortie = st.checkbox("Sortie", value=True)
            show_duree = st.checkbox("Durée", value=True)
            show_acteurs = st.checkbox("Acteurs", value=True)
        with col2:
            show_genres = st.checkbox("Genre", value=True)
            show_note = st.checkbox("Note", value=True)
            show_synopsis = st.checkbox("Synopsis", value=True)
            show_budget = st.checkbox("Budget", value=True)
            show_revenu = st.checkbox("Revenu", value=True)

        # n_acteurs = st.slider(
        #     "Acteurs à afficher :", 
        #     min_value=1,  # Valeur minimale
        #     max_value=10,  # Valeur maximale
        #     value=2,  # Valeur par défaut
        #     step=1  # Incrément de 1
        # )

            
    # Afficher la taille actuelle en pixels
    with st.sidebar.expander("Accessibilité", expanded=False):
            # Utilisation de checkbox pour simuler un toggle
        mode_sombre = st.checkbox("Mode sombre", value=True)

        st.markdown(f"""<div style="text-align: center; font-size: {st.session_state.taille_texte}px;">
        <strong>Taille actuelle : {st.session_state.taille_texte}px</strong>
        </div>""", unsafe_allow_html=True)

        # Titre pour les boutons de changement de taille de police
        st.markdown("<h3 style='font-size: 13px; font-weight: normal;'>Changer la taille de la police</h3>", unsafe_allow_html=True)
        # Utilisation de st.columns pour centrer les boutons "Agrandir", "Réduire" et "Défaut"
        col1, col2, col3 = st.columns([1, 1, 1])  # Crée trois colonnes avec un ratio égal
        with col1:
            if st.button("Moins"):
                st.session_state.taille_texte -= 2
        with col2:
            if st.button("Défaut"):  # Bouton pour réinitialiser la taille
                st.session_state.taille_texte = 16
        with col3:
            if st.button("Plus"):
                st.session_state.taille_texte += 2

        # Limiter la taille du texte pour éviter des valeurs trop petites ou trop grandes
        st.session_state.taille_texte = max(10, min(st.session_state.taille_texte, 30))  # Plage de 10 à 30





# Afficher les résultats
for film, lien in films_similaires:
    st.write(f"{film} : {lien}")
