import pandas as pd
import re
import numpy as np
import streamlit as st
import requests
from sklearn.metrics.pairwise import cosine_similarity
from datetime import datetime

# Définir la configuration de la page
st.set_page_config(
    page_title="Système de recommandations",
    page_icon="🎬",
    layout="wide",  # Mettre "wide" pour étendre la page
    initial_sidebar_state="expanded"  # La sidebar sera toujours affichée au départ
)

# Lien partie 1
download_url = "https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/csv/df_films.tsv"

# Charger le fichier CSV depuis l'URL de téléchargement direct
def charger_donnees():
    return pd.read_csv(download_url, delimiter="\t")

df = charger_donnees()

# Clé API TMDB
api_key = "ea30a0fce08ca9cc6e21228602a97f1a"

# Pondération des colonnes
poids = {
    "Note_moyenne_norm": 0.5, "Nb_votants_norm": 0.5, "Annee_sortie_norm": 0.5, "Duree_minutes_norm": 0.5,
    "Comedie": 3, "Documentaire": 3, "Famille": 3, "Romance": 3, "Action": 3, "Thriller": 3,
    "Fantaisie": 3, "Horreur": 3, "Aventure": 3, "Animation": 3,
    "DIR_": 40, "ACT_": 45  # Poids pour les colonnes des directeurs et acteurs
}

# Filtrer les colonnes pertinentes pour la pondération
colonnes_a_ponderer = [
    col for col in df.columns 
    if col in poids or any(col.startswith(prefix) for prefix in ["DIR_", "ACT_"])
]

# Appliquer les pondérations uniquement sur les colonnes pertinentes
for col in colonnes_a_ponderer:
    if col in poids:  # Pondération des colonnes générales
        df[col] = df[col] * poids[col]
    elif col.startswith("DIR_"):  # Pondération des colonnes des directeurs
        df[col] = df[col] * poids["DIR_"]
    elif col.startswith("ACT_"):  # Pondération des colonnes des acteurs
        df[col] = df[col] * poids["ACT_"]

# Sélection des colonnes numériques pertinentes pour la similarité
features = df[colonnes_a_ponderer]

# Calcul de la similarité cosinus
cos_sim = cosine_similarity(features)

# Fonction de recommandation
def recommander_films(titre, n):
    try:
        # Récupérer l'index du film
        film_index = df[df["Titre_original"] == titre].index[0]

        # Obtenir les similarités cosinus et trier
        similarites = cos_sim[film_index]
        indices_similaires = np.argsort(similarites)[-n-1:-1][::-1]  # Top-n films similaires

        # Retourner les titres et les distances
        return [
            (df.iloc[i]["Titre_original"], df.iloc[i]["Lien_Affiche"], df.iloc[i]["ID_film"]) for i in indices_similaires
        ]
    except IndexError:
        return f"Corrige le titre de ton film !"

# Initialisation de la taille du texte avec un état par défaut
if "taille_texte" not in st.session_state:
    st.session_state.taille_texte = 16  # Valeur par défaut

# Barre de navigation à gauche avec modification du style de la barre de recherche
with st.sidebar:
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

    with st.sidebar.expander("Choisissez vos genres", expanded=False):
        # Créer deux colonnes dans l'expander pour afficher les checkboxes
        col1, col2 = st.columns(2)

        # Afficher les checkboxes dans les colonnes
        with col1:
            show_action = st.checkbox("Action", value=True)
            show_aventure = st.checkbox("Aventure", value=True)
            show_documentaire = st.checkbox("Documentaire", value=True)
            show_fantaisie = st.checkbox("Fantaisie", value=True)
            show_romance = st.checkbox("Romance", value=True)
        with col2:
            show_animation = st.checkbox("Animation", value=True)
            show_comedie = st.checkbox("Comédie", value=True)
            show_famille = st.checkbox("Famille", value=True)
            show_horreur = st.checkbox("Horreur", value=True)
            show_thriller = st.checkbox("Thriller", value=True)
        
        # Créer un masque pour chaque genre
        masque = []

        if show_action:
            masque.append(df["Action"] !=0)
        if show_aventure:
            masque.append(df["Aventure"] !=0)
        if show_documentaire:
            masque.append(df["Documentaire"] !=0)
        if show_fantaisie:
            masque.append(df["Fantaisie"] !=0)
        if show_romance:
            masque.append(df["Romance"] !=0)    
        if show_animation:
            masque.append(df["Animation"] !=0)
        if show_comedie:
            masque.append(df["Comedie"] !=0)
        if show_famille:
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
                    image_url = df[df["Titre_original"] == titre_film]["Lien_Affiche"].values[0]
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

        with st.sidebar.expander("Choisissez éléments à afficher", expanded=False):
            # Nouveau curseur pour ajuster le nombre de films à afficher par ligne
            n_par_ligne = st.slider(
                "Nombre de films à afficher par ligne :", 
                min_value=1,  # Valeur minimale
                max_value=5,  # Valeur maximale
                value=3,  # Valeur par défaut
                step=1  # Incrément de 1
            )

            # Curseur pour ajuster le nombre de films similaires, avec plage de 1 à 20
            n_similaire = st.slider(
                "Nombre de films similaires souhaités :", 
                min_value=1,  # Valeur minimale
                max_value=10,  # Valeur maximale
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
                show_slogan = st.checkbox("Slogan", value=True)
                
            with col2:
                show_genres = st.checkbox("Genre", value=True)
                show_note = st.checkbox("Note", value=True)
                show_votants = st.checkbox("Votants", value=True)
                show_synopsis = st.checkbox("Synopsis", value=True)
                show_budget = st.checkbox("Budget", value=True)
                show_revenu = st.checkbox("Revenu", value=True)

            n_acteurs = st.slider(
                "Acteurs à afficher :", 
                min_value=0,  # Valeur minimale
                max_value=10,  # Valeur maximale
                value=5,  # Valeur par défaut
                step=1  # Incrément de 1
            )
                
        # Afficher la taille actuelle en pixels
        with st.sidebar.expander("Accessibilité", expanded=False):
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

if titre_film:
    films_similaires = recommander_films(titre_film, n_similaire)
    if isinstance(films_similaires, str):
        st.error(films_similaires)
    else:
        st.markdown(
            """
            <h1 style="text-align: center; flex-grow: 1;">Système de recommandations de Films</h1>
            <div style="height: 20px;"></div>  <!-- Espace après le bloc -->
            """,
            unsafe_allow_html=True
        )

        # Mise en forme du titre des films similaires
        st.markdown(f"<div style='font-size:{st.session_state.taille_texte + 8}px;'><b>Les {n_similaire} Films les plus similaires à <span style='color:red;'>{titre_film}</b></span> :</div>", unsafe_allow_html=True)
        st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

        # Calcul du nombre de lignes nécessaires
        lignes = (n_similaire // n_par_ligne) + (1 if n_similaire % n_par_ligne != 0 else 0)

        # Affichage des films similaires
        for i in range(lignes):
            cols = st.columns(n_par_ligne)

            for j in range(n_par_ligne):
                index = i * n_par_ligne + j
                if index < n_similaire:  # Vérifie qu'il reste des films à afficher
                    film_titre, film_image, film_id = films_similaires[index]

                    with cols[j]:
                        # Récupérer les détails du film depuis le DataFrame
                        film_details = df[df["ID_film"] == film_id].iloc[0]
                        note = film_details["Note_moyenne"]
                        nb_votants = film_details["Nb_votants"]
                        duree = film_details["Duree_minutes"]
                        
                        # Vérifie si la colonne "Video" existe dans le DataFrame
                        video_url = film_details["Vidéo"] if "Vidéo" in film_details else None

                        synopsis = film_details["synopsis"]
                        date_sortie = film_details["Date_sortie"]
                        budget = film_details["Budget"]
                        revenus = film_details["Revenus"]
                        slogan = film_details["Slogan"]

                        st.markdown(f"<div style='font-size:{st.session_state.taille_texte + 4}px; text-align: center; font-weight: bold;'>{film_titre}</div>", unsafe_allow_html=True)

                        # Affichage de l'image du film
                        if show_image:
                            st.markdown(
                                f"""
                                <div style="display: flex; justify-content: center; align-items: center; 
                                            width: 100%; margin: auto;">
                                    <img src="{film_image}" style="max-height: 400px; border: 1px solid black; border-radius: 8px; object-fit: cover;">
                                </div>
                                """, 
                                unsafe_allow_html=True
                            )

                        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

                        # Affichage conditionnel de la vidéo YouTube (si l'URL vidéo est valide)
                        if show_video and isinstance(video_url, str) and video_url.strip():
                            st.video(video_url)
                        elif show_video:
                            st.warning("Aucune vidéo disponible pour ce film.")

                        # Informations supplémentaires
                        if show_date_sortie:
                            st.markdown(f"""<div style="font-size:{st.session_state.taille_texte}px; margin-bottom: 10px;"><strong><u>Date de sortie :</u> </strong>{date_sortie}</div>""", unsafe_allow_html=True)
                        if show_duree:
                            st.markdown(f"""<div style="font-size:{st.session_state.taille_texte}px; margin-bottom: 10px;"><strong><u>Durée :</u> </strong>{duree} minutes</div>""", unsafe_allow_html=True)

                        # Extraire les acteurs depuis la colonne "Top_Acteurs" du DataFrame
                        acteurs = film_details["Top_Acteurs"]  # Cela récupère la liste d'acteurs pour ce film
                        
                        # Si la colonne Top_Acteurs est une chaîne de caractères, la convertir en liste
                        if isinstance(acteurs, str):
                            acteurs = acteurs.split(",")  # Séparer la chaîne par la virgule
                        
                        # Afficher les acteurs seulement si n_acteurs > 0 et s'il y a des acteurs dans la liste
                        if n_acteurs > 0 and acteurs:  # Vérifie si la liste acteurs n'est pas vide
                            acteurs_affiches = acteurs[:n_acteurs]  # Limite à n_acteurs
                            st.markdown(
                                f"""<div style="font-size:{st.session_state.taille_texte}px; margin-bottom: 10px;">
                                <strong><u>Acteurs principaux :</u> </strong>{', '.join(acteurs_affiches)}
                                </div>""",
                                unsafe_allow_html=True
                            )

                        # Affichage conditionnel de la note et des votants
                        if show_note:
                            if show_votants:  # Affiche le nombre de votants seulement si l'option est activée
                                st.markdown(f"""<div style="font-size:{st.session_state.taille_texte}px; margin-bottom: 10px;"><strong><u>Note moyenne :</u> </strong>{note:.1f}/10 (sur {nb_votants:,} votes)</div>""", unsafe_allow_html=True)
                            else:
                                st.markdown(f"""<div style="font-size:{st.session_state.taille_texte}px; margin-bottom: 10px;"><strong><u>Note moyenne :</u> </strong>{note:.1f}/10</div>""", unsafe_allow_html=True)

                        if show_budget and budget > 0:
                            st.markdown(f"""<div style="font-size:{st.session_state.taille_texte}px; margin-bottom: 10px;"><strong><u>Budget :</u> </strong>{budget:,.0f} $</div>""", unsafe_allow_html=True)
                        if show_revenu and revenus > 0:
                            st.markdown(f"""<div style="font-size:{st.session_state.taille_texte}px; margin-bottom: 10px;"><strong><u>Revenus :</u> </strong>{revenus:,.0f} $</div>""", unsafe_allow_html=True)

                        if show_slogan and pd.notna(slogan) and slogan.strip():  # Vérifie que le slogan n'est pas NaN et non vide
                            st.markdown(
                                f"""<div style="font-size:{st.session_state.taille_texte}px; margin-bottom: 10px;">
                                <strong><u>Slogan :</u> </strong>{slogan}
                                </div>""",
                                unsafe_allow_html=True
                            )

                        if show_synopsis:
                            st.markdown(f"""<div style="font-size:{st.session_state.taille_texte}px; margin-bottom: 10px;"><strong><u>Synopsis :</u> </strong></div>""", unsafe_allow_html=True)
                            st.markdown(f"""
                            <div style="font-size:{st.session_state.taille_texte}px; margin-bottom: 10px; text-align: justify;">
                            {synopsis}
                            </div>
                            """, unsafe_allow_html=True)

            # Ajout d'une bordure entre les lignes (sauf la dernière)
            if i < lignes - 1:
                st.markdown("<div style='border-top: 5px solid black;'></div>", unsafe_allow_html=True)
