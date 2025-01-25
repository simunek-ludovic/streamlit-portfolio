# PAGE geocoding
import pandas as pd
import streamlit as st

# Fichier d'appui si besoin :
# https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/csv/food.csv


st.write("Le géocodage (ou geocoding en anglais) est un processus qui permet de convertir des descriptions d'emplacements (comme des adresses, des noms de lieux ou des coordonnées GPS partielles) en coordonnées géographiques exactes, c'est-à-dire une latitude et une longitude. C'est une étape clé dans de nombreuses applications basées sur la localisation, comme les cartes interactives, les systèmes de navigation ou l'analyse de données géospatiales.")

st.write("""
Exemple :
- Vous entrez une adresse : "177 Alléee Clémentine Deman, 59000 Lille"
- Le géocodage renvoie les coordonnées correspondantes : latitude : 50.6339, longitude : 3.0224.
""")

st.write("Cela peut également être fait dans l'autre sens : Vous entrez les cordoonnées géographiques et il vous renvoi l'adresse")

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

st.write("Pour montrer comment l'utiliser nous allons utiliser un fichier CSV (https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/csv/food.csv)")
st.write("Il contient une trentaine d'adresses de restaurants sur Paris")

with st.expander("Convertir ce fichier CSV en DataFrame 'df_csv'"):
    st.code("""
    import pandas as pd
    url="https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/csv/food.csv"
    resto_paris = pd.read_csv(url)            
    resto_paris
    """, language='python')
    url="https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/csv/food.csv"
    resto_paris = pd.read_csv(url)            

    # Charger le fichier CSV
    resto_paris = pd.read_csv("https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/csv/food.csv")

    # Afficher le DataFrame dans Streamlit
    st.dataframe(resto_paris, use_container_width=True)

with st.expander("Supprimons la colonne 'Unnamed' que nous n'allons pas utiliser"):
    st.code("""
    resto_paris = resto_paris.drop(columns = "Unnamed: 0")
    resto_paris
    """, language='python')
    url="https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/csv/food.csv"
    resto_paris = pd.read_csv(url)            

    resto_paris = resto_paris.drop(columns = "Unnamed: 0")

    # Afficher le DataFrame dans Streamlit
    st.dataframe(resto_paris, use_container_width=True)

with st.expander("Fusionnons les 2 colonnes liées à l'adresse"):
    st.code("""
    resto_paris['adresse_complete'] = resto_paris['adresse'] + ',' + resto_paris['code postal']
    resto_paris
    """, language='python')
    url="https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/csv/food.csv"
    resto_paris = pd.read_csv(url)            

    resto_paris = resto_paris.drop(columns = "Unnamed: 0")

    resto_paris['adresse_complete'] = resto_paris['adresse'] + ',' + resto_paris['code postal']

    # Afficher le DataFrame dans Streamlit
    st.dataframe(resto_paris, use_container_width=True)

with st.expander("Créons une fonction utilisant l'API d'adresse"):
    st.code("""
    import requests

    def API_adresse(adresse_postale):
        URL = 'https://api-adresse.data.gouv.fr/search/?q='
        adresse_formatee = adresse_postale.replace(' ', '+')
        code_postal = adresse_postale.split(',')[-1].split(' ')[0]
        URL_complet = f"{URL}{adresse_formatee}&postcode={code_postal}&limit=1"

        return URL_complet
    """, language='python')
    url="https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/csv/food.csv"
    resto_paris = pd.read_csv(url)            

    resto_paris = resto_paris.drop(columns = "Unnamed: 0")

    resto_paris['adresse_complete'] = resto_paris['adresse'] + ',' + resto_paris['code postal']

    import requests

    def API_adresse(adresse_postale):
        URL = 'https://api-adresse.data.gouv.fr/search/?q='
        adresse_formatee = adresse_postale.replace(' ', '+')
        code_postal = adresse_postale.split(',')[-1].split(' ')[0]
        URL_complet = f"{URL}{adresse_formatee}&postcode={code_postal}&limit=1"

        return URL_complet

with st.expander("Utilisons l'API et récupérons la latitude et la longitude de chaque adresse"):
    st.code("""
    resto_paris['coordonnees'] = resto_paris['adresse_complete'].apply(lambda x : requests.get(API_adresse(x)).json()['features'][0]['geometry']['coordinates'][::-1])
    resto_paris
    """, language='python')
    url="https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/csv/food.csv"
    resto_paris = pd.read_csv(url)            

    resto_paris = resto_paris.drop(columns = "Unnamed: 0")

    resto_paris['adresse_complete'] = resto_paris['adresse'] + ',' + resto_paris['code postal']

    import requests

    def API_adresse(adresse_postale):
        URL = 'https://api-adresse.data.gouv.fr/search/?q='
        adresse_formatee = adresse_postale.replace(' ', '+')
        code_postal = adresse_postale.split(',')[-1].split(' ')[0]
        URL_complet = f"{URL}{adresse_formatee}&postcode={code_postal}&limit=1"

        return URL_complet

    resto_paris['coordonnees'] = resto_paris['adresse_complete'].apply(lambda x : requests.get(API_adresse(x)).json()['features'][0]['geometry']['coordinates'][::-1])

    # Afficher le DataFrame dans Streamlit
    st.dataframe(resto_paris, use_container_width=True)


with st.expander("Pour créer la carte, nous allons utiliser la librairie Folium"):
    st.code("""
    import folium

    carte = folium.Map(location=resto_paris['coordonnees'][0], zoom_start=13)

    for index, row in resto_paris.iterrows():
        folium.Marker(location=row['coordonnees'], popup=row['nom']).add_to(carte)

    carte
    """, language='python')
    url="https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/csv/food.csv"
    resto_paris = pd.read_csv(url)            

    resto_paris = resto_paris.drop(columns = "Unnamed: 0")

    resto_paris['adresse_complete'] = resto_paris['adresse'] + ',' + resto_paris['code postal']

    import requests

    def API_adresse(adresse_postale):
        URL = 'https://api-adresse.data.gouv.fr/search/?q='
        adresse_formatee = adresse_postale.replace(' ', '+')
        code_postal = adresse_postale.split(',')[-1].split(' ')[0]
        URL_complet = f"{URL}{adresse_formatee}&postcode={code_postal}&limit=1"

        return URL_complet

    resto_paris['coordonnees'] = resto_paris['adresse_complete'].apply(lambda x : requests.get(API_adresse(x)).json()['features'][0]['geometry']['coordinates'][::-1])

    import folium
    from streamlit_folium import st_folium
    carte = folium.Map(location=resto_paris['coordonnees'][0], zoom_start=13)
    for index, row in resto_paris.iterrows():
        folium.Marker(location=row['coordonnees'], popup=row['nom']).add_to(carte)
    st_folium(carte, width=1000)


