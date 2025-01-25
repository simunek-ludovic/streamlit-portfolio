# PAGE REGEX
import pandas as pd
import re
import streamlit as st

# Fichier d'appui si besoin :
# https://raw.githubusercontent.com/murpi/wilddata/master/quests/candidates_df.csv


# Barre de navigation
sous_menu = st.sidebar.radio("Choisissez une partie :", ["Règles de base", "Exemples"])

# Affichage de la description générale
if sous_menu == "Règles de base":

    st.write("""Le Regex (ou REGular EXpression) est une séquence de caractères qui forme un modèle de recherche.. Ce modèle est utilisé pour effectuer des recherches et des manipulations de chaînes de caractères (textes) en utilisant des règles spécifiques. Les expressions régulières permettent de :
    - Rechercher des motifs précis dans une chaîne de texte.
    - Extraire des parties d'une chaîne qui correspondent à un motif.
    - Remplacer ou modifier des éléments dans une chaîne de caractères.
    - Valider des entrées comme des emails, des numéros de téléphone, des formats de date, etc...
    """)

    # Explication générale
    st.write("""Les expressions régulières sont un puissant outil pour manipuler les chaînes de caractères. Voici un guide détaillé pour comprendre les principales syntaxes utilisées dans les regex.""")

    # Section 1 : Caractères de base
    st.write("Caractères de base :")

    # Définition et exemple pour chaque caractère
    st.write("""
    - `.` : Correspond à n'importe quel caractère (sauf un saut de ligne).
    - `\\d` : Correspond à un chiffre (0-9).
    - `\\D` : Correspond à tout caractère qui n'est pas un chiffre.
    - `\\w` : Correspond à un caractère alphanumérique (lettre, chiffre, ou `_`).
    - `\\W` : Correspond à tout caractère non alphanumérique.
    - `\\s` : Correspond à un espace, une tabulation ou un saut de ligne.
    - `\\S` : Correspond à tout caractère qui n'est pas un espace.
    - `\\b` : Correspond à une frontière de mot (espace ou ponctuation avant ou après un mot).
    - `\\B` : Correspond à tout endroit qui n'est pas une frontière de mot.
    """)

    # Section 2 : Quantificateurs
    st.write("Quantificateurs :")

    # Définition et exemple pour chaque quantificateur
    st.write("""
    - `*` : Correspond à zéro ou plusieurs occurrences du caractère précédent.
    - `+` : Correspond à une ou plusieurs occurrences du caractère précédent.
    - `?` : Correspond à zéro ou une occurrence du caractère précédent.
    - `{n}` : Correspond exactement à `n` occurrences du caractère précédent.
    - `{n,}` : Correspond à `n` occurrences ou plus du caractère précédent.
    - `{n,m}` : Correspond entre `n` et `m` occurrences du caractère précédent.
    """)

    # Section 3 : Caractères de groupe et de sélection
    st.write("Caractères de groupe et de sélection :")

    # Définition et exemple pour chaque caractère de groupe
    st.write("""
    - `[]` : Délimite un groupe de caractères. Exemple : `[abc]` correspond à "a", "b" ou "c".
    - `[^]` : Négation d'un groupe. Exemple : `[^abc]` correspond à tout caractère sauf "a", "b" ou "c".
    - `|` : Opérateur ou. Exemple : `abc|def` correspond à "abc" ou "def".
    - `()` : Délimite un groupe de capture. Exemple : `(abc)+` correspond à "abc" une ou plusieurs fois.
    """)

    # Section 4 : Position et ancrage
    st.write("Position et ancrage :")

    # Définition et exemple pour chaque position et ancrage
    st.write("""
    - `^` : Correspond au début d'une chaîne.
    - `$` : Correspond à la fin d'une chaîne.
    - `\\A` : Correspond au début d'une chaîne (indépendant des lignes).
    - `\\Z` : Correspond à la fin d'une chaîne (indépendant des lignes).
    - `\\z` : Correspond à la fin de la chaîne, incluant les sauts de ligne.
    """)

    # Section 5 : Classes de caractères
    st.write("Classes de caractères :")

    # Définition et exemple pour chaque classe de caractères
    st.write("""
    - `[a-z]` : Correspond à une lettre minuscule de `a` à `z`.
    - `[A-Z]` : Correspond à une lettre majuscule de `A` à `Z`.
    - `[0-9]` : Correspond à un chiffre de `0` à `9`.
    - `[a-zA-Z]` : Correspond à une lettre, qu'elle soit minuscule ou majuscule.
    - `[aeiou]` : Correspond à une voyelle en minuscule.
    """)

elif sous_menu == "Exemples":

    # Exemple pour tester les caractères de base
    st.write("### Exemple de recherche de caractères")
    with st.expander("Code Regex"):
        st.code("""
        user_input = st.text_input("Entrez une chaîne (...) pour rechercher les chiffres :")
        chiffres = re.findall(r"\d+", user_input)
        """, language='python')

    user_input = st.text_input("Entrez une chaîne (peu importe chiffres, lettres (minuscules et/ou majuscules), caractères spéciaux, ...) pour rechercher les chiffres (et taper entrée) :")

    if user_input:
        # Exemple de recherche de chiffres
        chiffres = re.findall(r"\d+", user_input)
        st.write(f"Les chiffres extraits sont : {chiffres}")

    # Exemple interactif pour tester une classe de caractères
    with st.expander("Code Regex"):
        st.code("""
        user_input2 = st.text_input("Entrez une chaîne pour rechercher les voyelles écrites en minuscules :")
        voyelles = re.findall(r"[aeiou]", user_input2)
        """, language='python')

    user_input2 = st.text_input("Entrez une chaîne pour rechercher les voyelles écrites en minuscules (et taper entrée):")
    if user_input2:
        voyelles = re.findall(r"[aeiou]", user_input2)
        st.write(f"Les voyelles extraites sont : {voyelles}")

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

    st.write("### Exemple de recherche dans un fichier")
    st.write("Nous allons travailler avec ce fichier [CSV](https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/csv/candidates_df.csv) qui contient environ 260 lignes et 8 colonnes.")

    with st.expander("Convertir ce fichier CSV en DataFrame 'df_csv'"):
        st.code("""
        import pandas as pd
        url="https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/csv/candidates_df.csv"
        df_csv = pd.read_csv(url)            
        df_csv
        """, language='python')
        url="https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/csv/candidates_df.csv"
        df_csv = pd.read_csv(url)            

    # Charger le fichier CSV
    df = pd.read_csv("https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/csv/candidates_df.csv")

    # Afficher le DataFrame dans Streamlit
    st.dataframe(df, use_container_width=True)

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


    st.write("### Consignes 1 :")
    st.write("Décompresser les informations sur l'email avec RegEx")
    st.write("Nous aimerions avoir une colonne pour le prénom, une colonne pour le nom et une colonne pour le fournisseur d'email")

    df_2 = df.copy()  # Crée une copie du DataFrame "df" afin de ne pas modifier l'original.

    # Utilise une expression régulière pour extraire le prénom (avant le premier point) à partir de l'adresse e-mail.
    df_2["firstname"] = df_2["candidate_email_address"].apply(lambda x: re.search("\w+", x).group(0))

    # Utilise une expression régulière pour extraire le nom de famille (après le premier point) et enlève le point.
    df_2["lastname"] = df_2["candidate_email_address"].apply(lambda x: re.sub(r'\.', '', re.search("\.\w+", x).group(0)))

    # Utilise une expression régulière pour extraire le service de messagerie (le domaine avant le "@" dans l'adresse e-mail).
    df_2["email_service"] = df_2["candidate_email_address"].apply(lambda x: re.sub("@", "", re.search("\@\w+", x).group(0)))

    with st.expander("Afficher/cacher le code :"):
        st.code("""
        df_2 = df.copy()  # Crée une copie du DataFrame "df" afin de ne pas modifier l'original.

        # Utilise une expression régulière pour extraire le prénom (avant le premier point) à partir de l'adresse e-mail.
        df_2["firstname"] = df_2["candidate_email_address"].apply(lambda x: re.search("\w+", x).group(0)) 

        # Utilise une expression régulière pour extraire le nom de famille (après le premier point) et enlève le point.
        df_2["lastname"] = df_2["candidate_email_address"].apply(lambda x: re.sub(r'\.', '', re.search("\.\w+", x).group(0)))

        # Utilise une expression régulière pour extraire le service de messagerie (le domaine avant le "@" dans l'adresse e-mail)
        df_2["email_service"] = df_2["candidate_email_address"].apply(lambda x: re.sub("@", "", re.search("\@\w+", x).group(0)))

        # Affiche le DataFrame avec les nouvelles colonnes
        df_2
        """, language='python')

    # Afficher le DataFrame dans Streamlit
    st.dataframe(df_2, use_container_width=True)

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

    st.write("### Consignes 2 :")
    st.write("Décompresser les infos URL avec RegEx")
    st.write("Nous aimerions avoir une colonne pour le titre du poste, une colonne pour la société et une colonne pour le lieu du poste.")

    with st.expander("Afficher/cacher le code :"):
        st.code("""
        df_3 = df_2.copy()  # Crée une copie du DataFrame "df_2" pour ne pas modifier l'original.

        # Extrait la partie après le dernier underscore dans la colonne "applied_for" pour obtenir le titre du poste.
        df_3["job_title"] = df_3['applied_for'].str.extract(r"/jobs/([\w-]+)_")

        # Remplace les tirets par des espaces dans la colonne "job_title" pour améliorer la lisibilité.
        df_3["job_title"] = df_3["job_title"].str.replace("-", " ", regex=True)

        # Extrait le nom de l'entreprise de la colonne "applied_for" entre "/companies/" et "/".
        df_3["compagny"] = df_3['applied_for'].str.extract(r"/companies/([\w-]+)/")

        # Remplace les tirets par des espaces dans la colonne "compagny" pour améliorer la lisibilité.
        df_3["compagny"] = df_3["compagny"].str.replace("-", " ", regex=True)

        # Extrait la localisation du poste de la colonne "applied_for", après le dernier underscore.
        df_3["job_location"] = df_3['applied_for'].str.extract(r"_([\w-]+)$")

        # Remplace les tirets par des espaces dans la colonne "job_location" pour améliorer la lisibilité.
        df_3["job_location"] = df_3["job_location"].str.replace("-", " ", regex=True)

        # Supprime la colonne "candidate_email_address" car elle n'est plus nécessaire.
        df_3 = df_3.drop("candidate_email_address", axis = 1)

        # Supprime la colonne "applied_for" car elle n'est plus nécessaire après avoir extrait les informations pertinentes.
        df_3 = df_3.drop("applied_for", axis = 1)
        """, language='python')

    df_3 = df_2.copy()  # Crée une copie du DataFrame "df_2" pour ne pas modifier l'original.

    # Extrait la partie après le dernier underscore dans la colonne "applied_for" pour obtenir le titre du poste.
    df_3["job_title"] = df_3['applied_for'].str.extract(r"/jobs/([\w-]+)_")

    # Remplace les tirets par des espaces dans la colonne "job_title" pour améliorer la lisibilité.
    df_3["job_title"] = df_3["job_title"].str.replace("-", " ", regex=True)

    # Extrait le nom de l'entreprise de la colonne "applied_for" entre "/companies/" et "/".
    df_3["compagny"] = df_3['applied_for'].str.extract(r"/companies/([\w-]+)/")

    # Remplace les tirets par des espaces dans la colonne "compagny" pour améliorer la lisibilité.
    df_3["compagny"] = df_3["compagny"].str.replace("-", " ", regex=True)

    # Extrait la localisation du poste de la colonne "applied_for", après le dernier underscore.
    df_3["job_location"] = df_3['applied_for'].str.extract(r"_([\w-]+)$")

    # Remplace les tirets par des espaces dans la colonne "job_location" pour améliorer la lisibilité.
    df_3["job_location"] = df_3["job_location"].str.replace("-", " ", regex=True)

    # Affiche le DataFrame final avec les nouvelles colonnes.
    df_3

    # Afficher le DataFrame dans Streamlit
    st.dataframe(df_3, use_container_width=True)


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

    st.write("### Consignes 3 :")
    st.write("Version final du fichier :")


    with st.expander("Afficher/cacher le code :"):
        st.code("""
        # Supprime les colonnes "candidate_email_address" et "applied_for" car elles ne sont plus nécessaires.
        df_3 = df_3.drop(["candidate_email_address", "applied_for"], axis=1)
        df_3
        """, language='python')


    # Supprime les colonnes "candidate_email_address" et "applied_for" car elles ne sont plus nécessaires.
    df_3 = df_3.drop(["candidate_email_address", "applied_for"], axis=1)

    # Afficher le DataFrame dans Streamlit
    st.dataframe(df_3, use_container_width=True)