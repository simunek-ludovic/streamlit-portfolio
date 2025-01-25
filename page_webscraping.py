# PAGE WEBSCRAPING
import streamlit as st
import requests
from bs4 import BeautifulSoup

# Découpe le texte en tokens simples avec split()
st.write("### Principe :")
st.write("""
Le **web scraping** (ou extraction de données web) est une technique qui consiste à extraire automatiquement des informations de sites web. 
Cela se fait généralement à l'aide de programmes ou de scripts qui parcourent les pages web et récupèrent des données spécifiques 
pour les analyser ou les stocker dans un format structuré, comme un fichier CSV ou une base de données.
""")

st.write("Les étapes principales du WebScraping sont :")
st.write("""
- Envoi d'une requête HTTP
- Récupération du contenu HTML
- Analyse du HTML
- Extraction des données
- Stockage des données
""")

st.write("Nous allons travailler sur le site web : http://www.chucknorrisfacts.fr/")

# Trait de séparation
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

st.write("### Principe :")

with st.expander("Afficher/cacher le code :"):
    st.code("""
    import requests  # Importation de la bibliothèque requests pour effectuer des requêtes HTTP

    url = "http://www.chucknorrisfacts.fr/facts/top/1"  # Définition de l'URL qui affiche la page 1 du site Web
    navigator = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)'  # Définition d'un user-agent pour simuler un navigateur (évite que le serveur bloque la requête)
    html = requests.get(url, headers={'User-Agent': navigator})  # Envoi de la requête HTTP GET à l'URL avec un en-tête spécifiant le user-agent
    html
    """, language='python')

import requests
url = "http://www.chucknorrisfacts.fr/facts/top/1"
navigator = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)'
html = requests.get(url, headers={'User-Agent': navigator})
st.write(html)
st.write("La réponse <Response [200]> correspond à une réponse HTTP avec le code de statut 200, qui indique que la requête HTTP a été traitée avec succès.")

# Trait de séparation
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

st.write("### Scrapper sur 1 seule page :")
with st.expander("Afficher/cacher le code :"):
    st.code("""
    from bs4 import BeautifulSoup  # Importation de la bibliothèque BeautifulSoup pour analyser le contenu HTML

    soup = BeautifulSoup(html.text, 'html.parser')  # Création d'un objet BeautifulSoup pour analyser le texte HTML récupéré dans 'html.text'
    titre = soup.find_all('div', {"class" : "card"})  # Recherche de toutes les balises <div> avec la classe "card" (qui contient les blagues)
    print(f"le nombre de blague de la page 1 est de {len(titre)}")  # Affichage du nombre de blagues trouvées, c'est-à-dire du nombre de divs avec la classe "card"
    """, language='python')

from bs4 import BeautifulSoup
soup = BeautifulSoup(html.text, 'html.parser')
titre = soup.find_all('div', {"class" : "card"})
st.write(f"le nombre de blague de la page 1 est de {len(titre)}")

with st.expander("Afficher/cacher le code :"):
    st.code("""  
    # Importation de la bibliothèque BeautifulSoup pour le traitement du HTML
    from bs4 import BeautifulSoup

    # Création d'un dictionnaire vide pour stocker les blagues et leurs notes
    dict = {}

    print("L'ensemble des blagues de la page 1 sont :")

    # Boucle qui itère sur les indices des éléments de la liste 'titre'
    for i in range(len(titre)):
        # Recherche de tous les éléments <p> avec la classe "card-text" dans le code HTML
        blagues = soup.find_all("p", {"class": "card-text"})
        
        # Recherche de tous les éléments <span> ayant un attribut 'id' dans le code HTML
        notes = soup.find_all("span", id=True)
        
        # Récupération du texte de la blague à l'indice 'i'
        blague = blagues[i].get_text()
        
        # Récupération du texte de la note à l'indice 'i'
        note = notes[i].text
        
        # Ajout de la blague et de la note dans le dictionnaire
        dict[blague] = note

    # Affichage du dictionnaire avec les blagues et leurs notes
    print(f"Blague {i+1} : {blague} Note : {note}"))
    """, language='python')


# Importation de la bibliothèque BeautifulSoup pour le traitement du HTML
from bs4 import BeautifulSoup

# Création d'un dictionnaire vide pour stocker les blagues et leurs notes
dict = {}

# Boucle qui itère sur les indices des éléments de la liste 'titre'
st.write("L'ensemble des blagues de la page 1 sont :")
for i in range(len(titre)):
    # Recherche de tous les éléments <p> avec la classe "card-text" dans le code HTML
    blagues = soup.find_all("p", {"class": "card-text"})
    
    # Recherche de tous les éléments <span> ayant un attribut 'id' dans le code HTML
    notes = soup.find_all("span", id=True)
    
    # Récupération du texte de la blague à l'indice 'i'
    blague = blagues[i].get_text()
    
    # Récupération du texte de la note à l'indice 'i'
    note = notes[i].text
    
    # Ajout de la blague et de la note dans le dictionnaire
    dict[blague] = note
    
    # Affichage de la blague et de la note à chaque itération (1 ligne par itération)
    st.write(f"Blague {i+1} : {blague} Note : {note}")

# Trait de séparation
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

st.write("### Scrapper sur plusieurs pages du même site :")
st.write("URL page 1 : http://www.chucknorrisfacts.fr/facts/top/1")
st.write("URL page 2 : http://www.chucknorrisfacts.fr/facts/top/2")
st.write("URL page 3 : http://www.chucknorrisfacts.fr/facts/top/3")
st.write("etc...")

with st.expander("Afficher/cacher le code :"):
    st.code("""
    import requests  # Importation de la bibliothèque requests pour effectuer des requêtes HTTP.
    from bs4 import BeautifulSoup  # Importation de BeautifulSoup pour l'analyse du HTML.
    import pandas as pd  # Importation de pandas pour manipuler les données sous forme de DataFrame.
    import random  # Importation de random pour générer des nombres aléatoires.

    base_url = "http://www.chucknorrisfacts.fr/facts/top/"  # URL de base pour accéder aux pages contenant des blagues.

    # Génère une liste de 5 URLs aléatoires parmi les 500 premières pages.
    urls = [f"{base_url}{random.randint(1, 500)}" for index in range(5)]

    data = []  # Liste pour stocker les blagues et leurs notes.

    # Parcourt chaque URL générée aléatoirement pour récupérer les blagues et notes.
    for url in urls:
        html = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})  # Envoie une requête HTTP avec un User-Agent pour simuler un navigateur.
        soup = BeautifulSoup(html.text, "html.parser")  # Analyse le contenu HTML de la page avec BeautifulSoup.

        blagues = soup.find_all("p", {"class": "card-text"})  # Trouve toutes les balises <p> avec la classe "card-text" (les blagues).
        notes = soup.find_all("span", id=True)  # Trouve toutes les balises <span> avec un attribut "id" (les notes).

        # Parcourt chaque blague et sa note correspondante pour les ajouter à la liste "data".
        for i in range(len(blagues)):
            blague = blagues[i].get_text(strip=True)  # Récupère le texte de la blague et supprime les espaces superflus.
            note = notes[i].text.strip()  # Récupère la note associée et supprime les espaces superflus.
            data.append((blague, note))  # Ajoute la paire (blague, note) à la liste "data".

    # Crée un DataFrame pandas avec les données collectées, en définissant les colonnes "blague" et "note".
    df = pd.DataFrame(data, columns=["blague", "note"])

    # Trie le DataFrame par la colonne "note" de manière décroissante.
    df = df.sort_values(by="note", ascending=False)

    # Affiche le DataFrame final.
    df

    """, language='python')

import requests
from bs4 import BeautifulSoup
import pandas as pd
import random

base_url = "http://www.chucknorrisfacts.fr/facts/top/"

# plutot que les 5 premiers pages, il choisit 5 pages parmi les 500 premiers pages
urls = [f"{base_url}{random.randint(1, 500)}" for index in range(5)]

data = []

for url in urls:
    html = requests.get(url, headers={"User-Agent": navigator})
    soup = BeautifulSoup(html.text, "html.parser")

    blagues = soup.find_all("p", {"class": "card-text"})
    notes = soup.find_all("span", id=True)

    for i in range(len(blagues)):
        blague = blagues[i].get_text(strip=True)
        note = notes[i].text.strip()
        data.append((blague, note))

df = pd.DataFrame(data, columns=["blague", "note"])
df = df.sort_values(by="note", ascending=False)
st.dataframe(df, use_container_width=True)
