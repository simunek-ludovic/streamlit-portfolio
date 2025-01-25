# PAGE python
st.header("Python")

# Barre de navigation
page_selection = st.sidebar.selectbox("Choisissez une des bibliothèques :", ["Python", "Geocodage", "Machine Learning", "NLP", "Pandas", "Regex", "Webscraping"], index=0)

# Affichage de la description générale de Python, sauf si la page Pandas ou Matplotlib est sélectionnée
if page_selection == "Python":
    st.write("### Présentation")
    st.write("Python est un langage de programmation populaire et polyvalent, utilisé dans de nombreux domaines, tels que la science des données, le développement web, l'automatisation, et bien plus encore.")
    st.write("Il est connu pour sa syntaxe claire et lisible, ce qui en fait un excellent choix pour les débutants. A ce jour, c'est le language informatique le plus utilisé dans le monde.")
    st.write("Python est facile d'apprentissage avec une syntaxe simple, proche du langage humain, ce qui permet aux débutants de se concentrer sur la logique plutôt que sur des détails complexes.")
    st.write("Il existe de nombreuses bibliothèques et frameworks pour étendre les capacités de Python, tels que :")

    st.write("""
    - Pandas pour l'analyse de données,
    - Matplotlib pour créer des visualisations graphiques sous forme de figures et d'axes. (graphiques en 2D, tels que des histogrammes, des courbes, ...)
    - Seaborn (construite sur Matplotlib) simplifie grandement la création de visualisations complexes,
    - Scikit-learn pour l'apprentissage automatique (machine learning),
    - NLTK pour le traitement du langage naturel,
    - BeautifulSoup pour l'extraction de données depuis des pages web.
    """)

    st.write("Je vous propose de découvrir ces bibliothèques en naviguant dans celle de votre choix")

# Affichage de la page sélectionnée
elif page_selection == "Geocodage":
    st.write("### Geocodage")
    # Exécuter le code du fichier python en utilisant exec()
    with open("page_geocodage.py", "r", encoding="utf-8") as f:
        content = f.read()
    exec(content)

# Affichage de la page sélectionnée
elif page_selection == "Machine Learning":
    st.write("### Machine Learning")
    # Exécuter le code du fichier python en utilisant exec()
    with open("page_machine_learning.py", "r", encoding="utf-8") as f:
        content = f.read()
    exec(content)

# Affichage de la page sélectionnée
elif page_selection == "NLP":
    st.write("### NLP")
    # Exécuter le code du fichier python en utilisant exec()
    with open("page_nlp.py", "r", encoding="utf-8") as f:
        content = f.read()
    exec(content)

# Affichage de la page sélectionnée
elif page_selection == "Pandas":
    st.write("### Pandas")
    # Exécuter le code du fichier python en utilisant exec()
    with open("page_pandas.py", "r", encoding="utf-8") as f:
        content = f.read()
    exec(content)

# Affichage de la page sélectionnée
elif page_selection == "Regex":
    st.write("### Regex")
    # Exécuter le code du fichier python en utilisant exec()
    with open("page_regex.py", "r", encoding="utf-8") as f:
        content = f.read()
    exec(content)

# Affichage de la page sélectionnée
elif page_selection == "Webscraping":
    st.write("### Webscraping")
    # Exécuter le code du fichier python en utilisant exec()
    with open("page_webscraping.py", "r", encoding="utf-8") as f:
        content = f.read()
    exec(content)
