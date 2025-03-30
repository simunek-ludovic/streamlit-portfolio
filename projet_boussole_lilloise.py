import streamlit as st

# Titre principal (optionnel car il pourrait déjà être dans la structure principale de votre app)
# st.title("La Boussole Lilloise")

# Contenu selon le choix du sous-menu
st.header("Présentation")

st.markdown("""
**La Boussole Lilloise** est une solution intelligente de mobilité urbaine permettant aux usagers de consulter en temps réel et de manière prévisionnelle les conditions météorologiques ainsi que l'ensemble des services de transport disponibles dans la Métropole Lilloise.
""")

st.header("Fonctionnalités clés")

st.markdown("""
Notre application intègre plusieurs sources de données pour vous offrir une expérience complète :
""")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Données météorologiques")
    st.markdown("""
    Accédez à des prévisions précises et des relevés en temps réel, actualisés toutes les 15 minutes, couvrant les 24 heures à venir.
    """)

with col2:
    st.subheader("Écosystème de mobilité")
    st.markdown("""
    Consultez l'état des services de transport de la Métropole Lilloise :
    """)
    
    # Utilisation de markdown pour créer une liste à puces
    st.markdown("""
    * Vélos en libre-service (V'Lille)
    * Réseau de bus
    * Lignes de métro
    * Réseau de tramway
    * Informations trafic routier en temps réel
    * Disponibilité des parkings-relais
    * État des aires de covoiturage
    """)

# Ajout d'un séparateur pour une meilleure organisation visuelle
st.divider()

# Section valeur ajoutée
st.header("Notre valeur ajoutée")

st.markdown("""
La Boussole Lilloise vous permet d'optimiser vos déplacements en vous proposant le mode de transport le plus adapté en fonction des conditions météorologiques et de l'état du réseau, vous faisant ainsi gagner un temps précieux au quotidien.
""")

# Informations techniques sur les sources de données (adapté de votre texte original)
st.header("Sources de données")
st.markdown("""
Plusieurs API ont été intégrées pour la réalisation de cette application :
* API météo pour les prévisions et données en temps réel
* API transport pour les informations sur les différents modes de transport
* Techniques de webscraping pour récupérer les informations de trafic en temps réel
""")

# Section découverte avec encadrement spécial
st.header("Découvrez notre plateforme")

# Création d'un encadré spécial pour le lien
st.info("""
Pour bénéficier de tous les avantages de La Boussole Lilloise, visitez notre application en ligne : [https://lsimunek.pythonanywhere.com/](https://lsimunek.pythonanywhere.com/)
""")

# Ajout d'une note de bas de page ou d'information supplémentaire
st.caption("© 2025 La Boussole Lilloise - Tous droits réservés")