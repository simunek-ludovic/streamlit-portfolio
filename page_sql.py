# Titre de la page
st.header("SQL")

# Présentation de SQL
st.write("""SQL (**S**tructured **Q**uery **L**anguage) est un langage standardisé utilisé pour interagir avec les bases de données relationnelles.""")

# Exemple de fonctionnement
st.write("""
Les fonctionnalités principales de SQL sont :
1. **Création de bases de données et de tables**
2. **Insertion de données**
3. **Récupération de données**
4. **Mise à jour ou suppression** de données
5. **Gestion des relations** entre les tables
""")

st.write("Même si le projet Toys & Models vous permettra de naviguer dans l'univers SQL, je vous présente quelques fonctionnalités :")

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

# Ajouter un expander pour un autre exemple
with st.expander("Créer une base de données 'demo'"):
    create_database = """
    CREATE DATABASE demo;
    """
    st.code(create_database, language="sql")



