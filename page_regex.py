import pandas as pd
import re

# Fichier d'appui si besoin :
# https://raw.githubusercontent.com/murpi/wilddata/master/quests/candidates_df.csv


st.write("""Le Regex (ou REGular EXpression) est une séquence de caractères qui forme un modèle de recherche.. Ce modèle est utilisé pour effectuer des recherches et des manipulations de chaînes de caractères (textes) en utilisant des règles spécifiques. Les expressions régulières permettent de :
- Rechercher des motifs précis dans une chaîne de texte.
- Extraire des parties d'une chaîne qui correspondent à un motif.
- Remplacer ou modifier des éléments dans une chaîne de caractères.
- Valider des entrées comme des emails, des numéros de téléphone, des formats de date, etc...
""")

st.write("Nous allons travailler avec ce fichier [CSV](https://raw.githubusercontent.com/ludovic-simunek/portfolio/refs/heads/main/csv/candidates_df.csv) qui contient environ 260 lignes et 8 colonnes.")

with st.expander("Convertir ce fichier CSV en DataFrame 'df_csv'"):
    st.code("""
    import pandas as pd
    url="https://raw.githubusercontent.com/ludovic-simunek/portfolio/refs/heads/main/csv/candidates_df.csv"
    df_csv = pd.read_csv(url)            
    df_csv
    """, language='python')
    url="https://raw.githubusercontent.com/ludovic-simunek/portfolio/refs/heads/main/csv/candidates_df.csv"
    df_csv = pd.read_csv(url)            

# Charger le fichier CSV
df = pd.read_csv("https://raw.githubusercontent.com/ludovic-simunek/portfolio/refs/heads/main/csv/candidates_df.csv")

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
