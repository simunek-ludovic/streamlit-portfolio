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

# Ajouter un expander pour un autre exemple
with st.expander("Utiliser la base de données 'demo'"):
    use = """
    USE demo;
    """
    st.code(use, language="sql")

# Ajouter un expander pour un autre exemple
with st.expander("Création une table 'auteur'"):
    create_table_auteur = """
    CREATE TABLE auteur (
    id_auteur 	INT 		PRIMARY KEY		AUTO_INCREMENT,
    nom 		VARCHAR(50),
    prenom 		VARCHAR(50)
    );
    """
    st.code(create_table_auteur, language="sql")

# Ajouter un expander pour un autre exemple
with st.expander("Ajouter des données dans la table 'auteur' pour mise à jour par exemple"):
    insert_into_auteur = """
    INSERT INTO auteur (prenom, nom)
    VALUES
    ('Alain','Amalric'),
    ('Brigitte','Delon'),
    ('Catherine','Belmondo'),
    ('Gerard','Cassel'),
    ('Isabelle','Cotillard'),
    ('Jean','Bardot'),
    ('Jean-Paul','Deneuve'),
    ('Lea','Depardieu'),
    ('Marion','Gabin'),
    ('Mathieu','Huppert'),
    ('Omar','Kiberlain'),
    ('Sandrine','Seydoux'),
    ('Vincent','Sy')
    ;
    """
    st.code(insert_into_auteur, language="sql")

# Ajouter un expander pour un autre exemple
with st.expander("Afficher tout le contenu (toutes les colonnes et lignes) de la table 'auteur'"):
    select_all = """
    SELECT *
    FROM auteur;
    """
    st.code(select_all, language="sql")

# Ajouter un expander pour un autre exemple
with st.expander("Afficher tout le contenu (toutes les colonnes et lignes) de la table 'auteur' quand la colonne prenom = 'Alain'"):
    select_prenom = """
    SELECT *
    FROM auteur
    WHERE prenom = "Alain";
    """
    st.code(select_prenom, language="sql")

# Ajouter un expander pour un autre exemple
with st.expander("Afficher tout le contenu (toutes les colonnes et lignes) de la table 'auteur' quand la colonne prenom contient 'Jean'"):
    select_prenom = """
    SELECT *
    FROM auteur
    WHERE prenom LIKE "%Jean%"
    ;
    """
    st.code(select_prenom, language="sql")

# Ajouter un expander pour un autre exemple
with st.expander("Trier par ordre croissant la colonne 'nom' de la table 'auteur' et afficher uniquement la colonne 'nom'"):
    tri_nom = """
    SELECT nom
    FROM auteur
    ORDER BY nom ASC
    ;
    """
    st.code(tri_nom, language="sql")





