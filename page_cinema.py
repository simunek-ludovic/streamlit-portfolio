# PAGE CINEMA
import pandas as pd
import re
import numpy as np
import streamlit as st
import requests
from sklearn.metrics.pairwise import cosine_similarity
from datetime import datetime
import unicodedata
import datetime
import time
import random

# Définir la configuration de la page
st.set_page_config(
    page_title="Système de recommandations",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Lien partie 1
download_url = "https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/csv/df_films.tsv"

# Charger le fichier CSV depuis l'URL de téléchargement direct
def charger_donnees():
    return pd.read_csv(download_url, delimiter="\t")

df = charger_donnees()

# Clé API TMDB
api_key = "ea30a0fce08ca9cc6e21228602a97f1a"

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

# Fonction pour normaliser une chaîne (supprimer les accents et caractères spéciaux)
def normaliser_chaine(chaine):
    chaine_normalisee = unicodedata.normalize("NFD", chaine)
    return "".join(c for c in chaine_normalisee if unicodedata.category(c) != "Mn")

with st.sidebar.expander("Filtrer la base de données", expanded=False):
    st.markdown('<p style="font-size:14px;">Choisissez vos genres</p>', unsafe_allow_html=True)
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
    
    # Slider pour filtrer selon l'année de sortie
    min_year, max_year = int(df["Annee_sortie"].min()), int(df["Annee_sortie"].max())  # Récupérer l'année min et max
    selected_years = st.slider(
        "Année de sortie",
        min_value=min_year,
        max_value=max_year,
        value=(min_year, max_year),
        step=1
    )
    
    # Slider pour filtrer selon la durée du film
    min_duree, max_duree = int(df["Duree_minutes"].min()), int(df["Duree_minutes"].max())  # Durée min et max
    selected_duree = st.slider(
        "Durée en minutes",
        min_value=min_duree,
        max_value=max_duree,
        value=(min_duree, max_duree),
        step=5
    )

    # Slider pour filtrer selon la note moyenne
    min_note, max_note = float(df["Note_moyenne"].min()), float(df["Note_moyenne"].max())  # Note min et max
    selected_note = st.slider(
        "Note moyenne",
        min_value=min_note,
        max_value=max_note,
        value=(min_note, max_note),
        step=0.1
    )

    # Créer un masque pour chaque genre
    masque = []

    if show_action:
        masque.append(df["Action"] != 0)
    if show_aventure:
        masque.append(df["Aventure"] != 0)
    if show_documentaire:
        masque.append(df["Documentaire"] != 0)
    if show_fantaisie:
        masque.append(df["Fantaisie"] != 0)
    if show_romance:
        masque.append(df["Romance"] != 0)    
    if show_animation:
        masque.append(df["Animation"] != 0)
    if show_comedie:
        masque.append(df["Comedie"] != 0)
    if show_famille:
        masque.append(df["Famille"] != 0)
    if show_horreur:
        masque.append(df["Horreur"] != 0)
    if show_thriller:
        masque.append(df["Thriller"] != 0)

    # Appliquer le masque sur les genres
    if masque:
        filtre_genres = masque[0]
        for m in masque[1:]:
            filtre_genres = filtre_genres | m  # Utiliser 'ou' logique pour combiner les filtres

        # Ajouter les filtres sur les années, la durée et la note
        filtre = (
            filtre_genres &
            df["Annee_sortie"].between(selected_years[0], selected_years[1]) &
            df["Duree_minutes"].between(selected_duree[0], selected_duree[1]) &
            df["Note_moyenne"].between(selected_note[0], selected_note[1])
        )

        # Filtrer le dataframe selon le masque combiné
        df_filtre = df[filtre]

        # Créer une liste des titres correspondant aux critères
        liste_titres = df_filtre["Titre_original"].tolist()
    else:
        # Si aucun genre n'est sélectionné, filtrer uniquement par les autres critères
        df_filtre = df[
            df["Annee_sortie"].between(selected_years[0], selected_years[1]) &
            df["Duree_minutes"].between(selected_duree[0], selected_duree[1]) &
            df["Note_moyenne"].between(selected_note[0], selected_note[1])
        ]
        liste_titres = df_filtre["Titre_original"].tolist()

    # Normaliser les titres et créer les catégories de tri
    liste_titres.sort()  # Tri alphabétique de la liste
    lettres_possibles = sorted(set([normaliser_chaine(titre[0].upper()) if titre[0].isalpha() else "0 à 9 (Chiffres)" for titre in liste_titres if titre]))
    lettre_selectionnee = st.selectbox("Premier caractère :", [""] + lettres_possibles)

    if lettre_selectionnee:
        if lettre_selectionnee == "0 à 9 (Chiffres)":
            liste_titres = [titre for titre in liste_titres if not normaliser_chaine(titre[0]).isalpha()]
        else:
            liste_titres = [titre for titre in liste_titres if normaliser_chaine(titre[0].upper()) == lettre_selectionnee]

    # Afficher la liste des titres filtrés avec la longueur en rouge et gras
    st.sidebar.markdown(f"Films dans la base de données : <span style='color:#007bff; font-weight:bold;'>{len(liste_titres)}</span>", unsafe_allow_html=True)

    if len(liste_titres) == 0:
        st.error("Aucun film ne correspond aux filtres actuels.")
        st.stop()  # Arrêter l'exécution si aucun film n'est trouvé

    # Ajouter une option pour sélectionner un film
    liste_titres.insert(0, "")
    
titre_film = st.sidebar.selectbox("**Entrez le titre du film :**", liste_titres)

with st.sidebar.expander("Afficher les éléments du Film choisi", expanded=True):

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

            # Récuépération des éléments dans le DF
            realisateur = df[df["Titre_original"] == titre_film]["Réalisateur"].values[0]
            acteurs = df[df["Titre_original"] == titre_film]["Top_Acteurs"].values[0]
            genres = df[df["Titre_original"] == titre_film]["Genres"].values[0]
            note = df[df["Titre_original"] == titre_film]["Note_moyenne"].values[0]
            durée = df[df["Titre_original"] == titre_film]["Duree_minutes"].values[0]
            votants = df[df["Titre_original"] == titre_film]["Nb_votants"].values[0]
            date_sortie = df[df["Titre_original"] == titre_film]["Date_sortie"].values[0]

            # Affichage des éléments
            st.markdown(f"<p><b><u>Réalisateur</u></b> : {realisateur}</p>", unsafe_allow_html=True)
            st.markdown(f"<p><b><u>Genres</u></b> : {genres}</p>", unsafe_allow_html=True)
            st.markdown(f"<p><b><u>Acteurs principaux</u></b> : {acteurs}</p>", unsafe_allow_html=True)
            st.markdown(f"<p><b><u>Date de sortie</u></b> : {date_sortie}</p>", unsafe_allow_html=True)
            st.markdown(f"<p><b><u>Durée</u></b> : {durée} minutes</p>", unsafe_allow_html=True)
            st.markdown(f"<p><b><u>Note moyenne</u></b> : {note:.1f}/10 (sur {votants:} votes)</p>", unsafe_allow_html=True)


        except IndexError:
            st.error(f"Le film '{titre_film}' n'existe pas dans la base de données.")

    with st.sidebar.expander("Choisissez éléments à afficher", expanded=False):
        # Curseur pour ajuster le nombre de films similaires, avec plage de 1 à 20
        n_similaire = st.slider(
            "Nombre de films similaires souhaités :", 
            min_value=1,  # Valeur minimale
            max_value=10,  # Valeur maximale
            value=3,  # Valeur par défaut
            step=1  # Incrément de 1
        )

        # Calcul de la valeur maximale pour le curseur "n_par_ligne"
        max_films_par_ligne = min(5, n_similaire)

        # Nouveau curseur pour ajuster le nombre de films à afficher par ligne
        n_par_ligne = st.slider(
            "Nombre de films à afficher par ligne :", 
            min_value=1,  # Valeur minimale
            max_value=max_films_par_ligne,  # Valeur maximale
            value=3,  # Valeur par défaut
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
            show_genres = st.checkbox("Genre(s)", value=True)
            show_note = st.checkbox("Note", value=True)
            show_votants = st.checkbox("Votants", value=True)
            show_synopsis = st.checkbox("Synopsis", value=True)
            show_budget = st.checkbox("Budget", value=True)
            show_revenu = st.checkbox("Revenu", value=True)

        n_acteurs = st.slider(
            "Acteurs principaux à afficher :", 
            min_value=0,  # Valeur minimale
            max_value=10,  # Valeur maximale
            value=5,  # Valeur par défaut
            step=1  # Incrément de 1
        )


# Barre latérale pour ajuster les poids
with st.sidebar.expander("Pondération sur les données", expanded=False):
    # Slider pour les colonnes DIR_
    poids_dir = st.slider(
        "Poids pour les réalisateurs",
        min_value=0.0,
        max_value=20.0,
        value=20.0,
        step=1.0
    )

    # Slider pour les colonnes ACT_
    poids_act = st.slider(
        "Poids pour les acteurs",
        min_value=0.0,
        max_value=20.0,
        value=20.0,
        step=1.0
    )

    # Slider pour les genres
    poids_genres = st.slider(
        "Poids pour les genres",
        min_value=0.0,
        max_value=20.0,
        value=3.0,
        step=1.0
    )

    # Slider pour les colonnes se terminant par _norm
    poids_norm = st.slider(
        "Poids pour les autres données",
        min_value=0.0,
        max_value=20.0,
        value=0.0,
        step=1.0
    )

# Section Accessibilité
with st.sidebar.expander("Accessibilité", expanded=False):
    # Titre pour le slider de changement de taille de police

    # Utilisation d'un slider pour ajuster la taille du texte
    st.session_state.taille_texte = st.slider(
        "Taille de la police (par défaut : 16px)",
        min_value=10,  # Taille minimale
        max_value=30,  # Taille maximale
        value=st.session_state.get("taille_texte", 16),  # Taille par défaut ou précédente
        step=2
    )

# Mise à jour des poids selon les choix de l'utilisateur
poids = {
    "Note_moyenne_norm": poids_norm,
    "Nb_votants_norm": poids_norm,
    "Annee_sortie_norm": poids_norm,
    "Duree_minutes_norm": poids_norm,
    "Comedie": poids_genres,
    "Documentaire": poids_genres,
    "Famille": poids_genres,
    "Romance": poids_genres,
    "Action": poids_genres,
    "Thriller": poids_genres,
    "Fantaisie": poids_genres,
    "Horreur": poids_genres,
    "Aventure": poids_genres,
    "Animation": poids_genres,
    "DIR_": poids_dir,
    "ACT_": poids_act
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
    elif col.startswith("DIR_"):  # Pondération des colonnes des réalisateurs
        df[col] = df[col] * poids["DIR_"]
    elif col.startswith("ACT_"):  # Pondération des colonnes des acteurs
        df[col] = df[col] * poids["ACT_"]

# Sélection des colonnes numériques pertinentes pour la similarité
features = df[colonnes_a_ponderer]

# Remplir les NaN par 0 avant de calculer la similarité
features = features.fillna(0)

# Calcul de la similarité cosinus
from sklearn.metrics.pairwise import cosine_similarity
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



# Vérifier si un film a été sélectionné
if titre_film == "":
    st.title("Bienvenue dans mon système de recommandation de films")
    # Taille du texte
    taille_texte = st.session_state.taille_texte  # Récupérer la taille sélectionnée

    # Contenu principal
    st.markdown(f"""<div style="font-size:{taille_texte + 4}px; font-weight:bold; margin-bottom:10px;">Comment a-t-il été construit ?</div>""", unsafe_allow_html=True)
    st.markdown(f"""<div style="font-size:{taille_texte}px; margin-bottom:10px;">
        Je suis parti des bases de données d'IMDB (Internet Movie Database) et TMDB (The Movie Database) afin d'explorer le monde fascinant du cinéma avec notamment :
    </div>""", unsafe_allow_html=True)

    st.markdown(f"""<div style="font-size:{taille_texte}px; margin-bottom:10px;">
        - IMDb qui a une base de données en ligne contenant plusieurs fichiers (souvent au format CSV ou TSV) regroupant des informations détaillées sur les films, séries, acteurs, ...<br>
        - TMDB qui a une base de données collaborative en ligne dédiée aux films et séries, offrant une API ouverte pour les développeurs.
    </div>""", unsafe_allow_html=True)

    st.markdown(f"""<div style="font-size:{taille_texte}px; margin-bottom:10px;">
        Ne disposant pas des ressources techniques suffisantes sur mon PC pour traiter l'intégralité des données, j'ai progressivement filtré les différents éléments au fur et à mesure de l'exploration.
    </div>""", unsafe_allow_html=True)

    st.markdown(f"""<div style="font-size:{taille_texte + 4}px; font-weight:bold; margin-bottom:10px;">Quels critères ont été pris en compte dans ce système de recommandations ?</div>""", unsafe_allow_html=True)
    st.markdown(f"""<div style="font-size:{taille_texte}px; margin-bottom:10px;">
        Les critères sélectionnés sont les suivants :
    </div>""", unsafe_allow_html=True)

    st.markdown(f"""<div style="font-size:{taille_texte}px; margin-bottom:10px;">
        - Films exclusivement français, sortis après 1960 et d'une durée minimale de 45 minutes, ayant obtenue une note moyenne d'au moins 5/10 (avec 500 votants minimum),<br>
        - Et au moins un genre parmi les suivants : Action, Animation, Aventure, Comédie, Documentaire, Famille, Fantastique, Horreur, Romance ou Thriller (ce qui garantit environ 100 films minimum par genre)
    </div>""", unsafe_allow_html=True)

    st.markdown(f"""<div style="font-size:{taille_texte}px; margin-bottom:10px;">
        Les informations collectées pour chaque film : Nom du réalisateur et les 10 acteurs principaux (dont les 3 principaux pour la similarité des films) , affiche, vidéo, synopsis, budget, revenus, slogan, ...
    </div>""", unsafe_allow_html=True)

    st.markdown(f"""<div style="font-size:{taille_texte}px; margin-bottom:10px;">
        Pour suggérer une similarité entre les films, vous pourrez ajuster vous-même l'importance accordée à chaque critère.
    </div>""", unsafe_allow_html=True)

    st.markdown(f"""<div style="font-size:{taille_texte}px; margin-bottom:10px;">
        Cela vous permettra d'influencer le résultat final en fonction de vos préférences (0 : aucune importance, 20 : importance maximale pour ces informations).
    </div>""", unsafe_allow_html=True)

    # Carrousel d'affiches
    # Afficher le message indiquant que les images défilent automatiquement
    st.markdown(f"""<div style="font-size:{taille_texte + 4}px; font-weight:bold; margin-bottom:10px;">Les films présents dans la base de données :</div>""", unsafe_allow_html=True)

    # Fonction pour récupérer les affiches aléatoires
    def get_affiches():
        # Remplacez df["Lien_Affiche"] par votre DataFrame réel
        return df["Lien_Affiche"].sample(5).values  # Sélectionner 5 affiches aléatoires

    # Conteneur vide qui sera mis à jour
    carousel_placeholder = st.empty()

    # Rafraîchissement des affiches toutes les 5 secondes
    while True:
        affiches = get_affiches()

        # Conteneur pour les images avec bordure
        cols = carousel_placeholder.columns(5)  # Créer 5 colonnes pour afficher les affiches

        # Afficher les images dans des colonnes
        for col, affiche in zip(cols, affiches):
            with col:
                st.markdown(
                    f"""
                    <div style="
                        margin: 10px;
                        border: 2px solid #555;  /* Couleur et épaisseur de la bordure */
                        border-radius: 10px;    /* Coins arrondis */
                        overflow: hidden;       /* Empêche le débordement */
                        width: 200px;           /* Largeur fixe pour les images */
                        text-align: center;     /* Centrer l'image */
                    ">
                        <img src="{affiche}" style="width: auto; height: 100%;">
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        # Attendre 5 secondes avant de rafraîchir les affiches
        time.sleep(5)
        carousel_placeholder.empty()  # Vider le conteneur pour le mettre à jour

else:
    film_saisi = df[df["Titre_original"] == titre_film]


if titre_film:
    films_similaires = recommander_films(titre_film, n_similaire)
    if isinstance(films_similaires, str):
        st.error(films_similaires)
    else:
        st.markdown(
            f"<div style='text-align:center; font-size:{st.session_state.taille_texte + 30}px; font-weight:bold;'>Système de recommandations de Films</div>",
            unsafe_allow_html=True
        )

        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    
        # Mise en forme du titre des films similaires
        st.markdown(f"<div style='font-size:{st.session_state.taille_texte + 8}px;'><b>Les {n_similaire} Films les plus similaires à <span style='color:red;'>{titre_film}</b></span> :</div>", unsafe_allow_html=True)
        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

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
                        video_url = film_details["Vidéo"] if "Vidéo" in film_details else None
                        synopsis = film_details["synopsis"]
                        date_sortie = film_details["Date_sortie"]
                        budget = film_details["Budget"]
                        revenus = film_details["Revenus"]
                        slogan = film_details["Slogan"]
                        realisateur = film_details["Réalisateur"]
                        genres = film_details["Genres"]

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

                   # Ajout des informations sur le réalisateur et les genres
                        if realisateur:
                            st.markdown(f"""<div style="font-size:{st.session_state.taille_texte}px; margin-bottom: 10px;"><strong><u>Réalisateur </u> </strong>: {realisateur}</div>""", unsafe_allow_html=True)

                        if genres:
                            st.markdown(f"""<div style="font-size:{st.session_state.taille_texte}px; margin-bottom: 10px;"><strong><u>Genres</u> </strong>: {genres}</div>""", unsafe_allow_html=True)

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
                                <strong><u>Acteurs principaux</u> </strong>: {', '.join(acteurs_affiches)}
                                </div>""",
                                unsafe_allow_html=True
                            )  
                        # Informations supplémentaires
                        if show_date_sortie:
                            st.markdown(f"""<div style="font-size:{st.session_state.taille_texte}px; margin-bottom: 10px;"><strong><u>Date de sortie</u> </strong>: {date_sortie}</div>""", unsafe_allow_html=True)
                        if show_duree:
                            st.markdown(f"""<div style="font-size:{st.session_state.taille_texte}px; margin-bottom: 10px;"><strong><u>Durée</u> </strong>: {duree} minutes</div>""", unsafe_allow_html=True)

                        if show_budget and budget > 0:
                            st.markdown(f"""<div style="font-size:{st.session_state.taille_texte}px; margin-bottom: 10px;"><strong><u>Budget</u> </strong>: {budget:,.0f} $</div>""", unsafe_allow_html=True)
                        if show_revenu and revenus > 0:
                            st.markdown(f"""<div style="font-size:{st.session_state.taille_texte}px; margin-bottom: 10px;"><strong><u>Revenus</u> </strong>: {revenus:,.0f} $</div>""", unsafe_allow_html=True)

                        # Affichage conditionnel de la note et des votants
                        if show_note:
                            if show_votants:  # Affiche le nombre de votants seulement si l'option est activée
                                st.markdown(f"""<div style="font-size:{st.session_state.taille_texte}px; margin-bottom: 10px;"><strong><u>Note moyenne</u> </strong>: {note:.1f}/10 (sur {nb_votants:} votes)</div>""", unsafe_allow_html=True)
                            else:
                                st.markdown(f"""<div style="font-size:{st.session_state.taille_texte}px; margin-bottom: 10px;"><strong><u>Note moyenne</u> </strong>: {note:.1f}/10</div>""", unsafe_allow_html=True)

                        if show_slogan and pd.notna(slogan) and slogan.strip():  # Vérifie que le slogan n'est pas NaN et non vide
                            st.markdown(
                                f"""<div style="font-size:{st.session_state.taille_texte}px; margin-bottom: 10px;">
                                <strong><u>Slogan</u> </strong>: {slogan}
                                </div>""",
                                unsafe_allow_html=True
                            )

                        if show_synopsis:
                            st.markdown(f"""<div style="font-size:{st.session_state.taille_texte}px; margin-bottom: 10px;"><strong><u>Synopsis</u> </strong>: </div>""", unsafe_allow_html=True)
                            st.markdown(f"""
                            <div style="font-size:{st.session_state.taille_texte}px; margin-bottom: 10px; text-align: justify;">
                            {synopsis}
                            </div>
                            """, unsafe_allow_html=True)

            # Ajout d'une bordure entre les lignes (sauf la dernière)
            if i < lignes - 1:
                st.markdown("<div style='border-top: 5px solid black;'></div>", unsafe_allow_html=True)
