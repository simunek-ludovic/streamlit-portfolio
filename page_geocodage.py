# PAGE geocoding
import pandas as pd
import streamlit as st
import requests
import folium
from streamlit_folium import st_folium

st.write("Le géocodage (ou geocoding en anglais) est un processus qui permet de convertir des descriptions d'emplacements (comme des adresses, des noms de lieux ou des coordonnées GPS partielles) en coordonnées géographiques exactes, c'est-à-dire une latitude et une longitude. C'est une étape clé dans de nombreuses applications basées sur la localisation, comme les cartes interactives, les systèmes de navigation ou l'analyse de données géospatiales.")

st.write("""
Exemple :
- Vous entrez une adresse : "177 Allée Clémentine Deman, 59000 Lille"
- Le géocodage renvoie les coordonnées correspondantes : latitude : 50.6339, longitude : 3.0224.
""")

st.write("Cela peut également être fait dans l'autre sens : Vous entrez les coordonnées géographiques et il vous renvoi l'adresse")

# Créer un trait de séparation
st.markdown("""
    <style>
        hr {
            border: 1px solid #000000;
            margin: 1px 0;
            height: 5px;
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
    url = "https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/csv/food.csv"
    resto_paris = pd.read_csv(url)
    st.dataframe(resto_paris, use_container_width=True)

with st.expander("Supprimons la colonne 'Unnamed' que nous n'allons pas utiliser"):
    st.code("""
    resto_paris = resto_paris.drop(columns="Unnamed: 0")
    resto_paris
    """, language='python')
    resto_paris = resto_paris.drop(columns="Unnamed: 0")
    st.dataframe(resto_paris, use_container_width=True)

with st.expander("Fusionnons les 2 colonnes liées à l'adresse"):
    st.code("""
    resto_paris['adresse_complete'] = resto_paris['adresse'] + ',' + resto_paris['code postal']
    resto_paris
    """, language='python')
    resto_paris['adresse_complete'] = resto_paris['adresse'] + ',' + resto_paris['code postal']
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

    def API_adresse(adresse_postale):
        URL = 'https://api-adresse.data.gouv.fr/search/?q='
        adresse_formatee = adresse_postale.replace(' ', '+')
        code_postal = adresse_postale.split(',')[-1].split(' ')[0]
        URL_complet = f"{URL}{adresse_formatee}&postcode={code_postal}&limit=1"
        return URL_complet

with st.expander("Utilisons l'API et récupérons la latitude et la longitude de chaque adresse"):
    st.code("""
    def get_coordinates(adresse_postale):
        try:
            response = requests.get(API_adresse(adresse_postale)).json()
            if response['features']:
                return response['features'][0]['geometry']['coordinates'][::-1]
            else:
                return None
        except Exception as e:
            st.error(f"Erreur pour l'adresse {adresse_postale}: {e}")
            return None

    resto_paris['coordonnees'] = resto_paris['adresse_complete'].apply(get_coordinates)
    resto_paris
    """, language='python')

    def get_coordinates(adresse_postale):
        try:
            response = requests.get(API_adresse(adresse_postale)).json()
            if response['features']:
                return response['features'][0]['geometry']['coordinates'][::-1]
            else:
                return None
        except Exception as e:
            st.error(f"Erreur pour l'adresse {adresse_postale}: {e}")
            return None

    resto_paris['coordonnees'] = resto_paris['adresse_complete'].apply(get_coordinates)
    st.dataframe(resto_paris, use_container_width=True)

with st.expander("Pour créer la carte, nous allons utiliser la librairie Folium"):
    st.code("""
    import folium
    from streamlit_folium import st_folium

    carte = folium.Map(location=resto_paris['coordonnees'].iloc[0], zoom_start=13)
    for index, row in resto_paris.iterrows():
        if row['coordonnees'] is not None:
            folium.Marker(location=row['coordonnees'], popup=row['nom']).add_to(carte)

    st_folium(carte, width=1000, height=600)
    """, language='python')

    carte = folium.Map(location=resto_paris['coordonnees'].iloc[0], zoom_start=13)
    for index, row in resto_paris.iterrows():
        if row['coordonnees'] is not None:
            folium.Marker(location=row['coordonnees'], popup=row['nom']).add_to(carte)

    st_folium(carte, width=1000, height=600)



import folium
from streamlit_folium import st_folium

carte = folium.Map(location=resto_paris['coordonnees'].iloc[0], zoom_start=13)
for index, row in resto_paris.iterrows():
    if row['coordonnees'] is not None:
        folium.Marker(location=row['coordonnees'], popup=row['nom']).add_to(carte)

st_folium(carte, width=1000, height=600)
