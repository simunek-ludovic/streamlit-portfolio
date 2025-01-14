import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# fichier d'appui si besoin :
# https://raw.githubusercontent.com/WCSLeadData/Html/main/online_store_customer_data.csv

# Sous-navigation pour le Projet
sous_menu = st.sidebar.radio("Naviguez dans la découverte de Pandas :", ["Présentation", "1", "2"])

# Contenu en fonction du choix dans le sous-menu
if sous_menu == "Présentation":
    st.write("Le ***Machine Learning*** est une branche de l'intelligence artificielle qui permet à un ordinateur d'apprendre à partir de données, sans être explicitement programmé pour chaque tâche.")
    st.write("Il utilise des algorithmes pour identifier des modèles ou des structures dans les données et effectuer des prédictions ou des décisions basées sur ces informations.")
    st.write("En résumé, c'est l'art de faire apprendre une machine à partir d'exemples pour qu'elle puisse prendre des décisions ou effectuer des tâches par elle-même.")

elif sous_menu == "1":
    st.write("partie 1")

elif sous_menu == "2":
    st.write("partie 2")
