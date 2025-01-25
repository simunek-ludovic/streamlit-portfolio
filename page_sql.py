# PAGE SQL
import streamlit as st

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

st.write("Même si le projet Toys & Models vous permettra de naviguer dans l'univers SQL, je vous présente quelques fonctionnalités :")

# Ajouter un expander pour un autre exemple
with st.expander("Supprimer une base de données 'test'"):
    drop_database = """
    DROP DATABASE test;
    """
    st.code(drop_database, language="sql")

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

st.write("Créons une première table appelée 'auteur', avec trois colonnes : 'id_auteur', 'nom' et 'prenom'.")
st.write("La colonne 'id_auteur' sera définie comme clé primaire, avec une valeur unique générée automatiquement par autoincrémentation.")
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

st.write("Ajoutons des valeurs dans cette table 'auteur'. Comme la colonne 'id_auteur' est autoincrémentée il n'est pas utile de la renseigner.")
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

st.write("On va créé une nouvelle table 'livre'. Cette table contiendra également 'id_auteur' créé dans la table 'auteur' mais nous n'indiquons pas que cette colonne est autoincrémentée.")
# Ajouter un expander pour un autre exemple
with st.expander("Création une table 'livre'"):
    create_table_livre = """
    CREATE TABLE livre (
        id_livre 		INT		PRIMARY KEY 	AUTO_INCREMENT,
        id_auteur 		INT,
        titre			VARCHAR(255),
        annee 			INT
    );
    """
    st.code(create_table_livre, language="sql")

st.write("Ajoutons des valeurs dans cette table 'livre'. Comme la colonne 'id_auteur' n'est plus autoincrémentée il est donc utile de la renseigner.")
# Ajouter un expander pour un autre exemple
with st.expander("Ajouter des données dans la table 'livre' pour mise à jour par exemple"):
    insert_into_livre = """
    INSERT INTO livre (id_auteur, titre, annee)
    VALUES
    (3, "Melusine", 1392),
    (6, "Gargantua", 1534),
    (7, "Discours de la servitude volontaire", 1576),
    (9, "Les Essais", 1595),
    (9, "Le Cid", 1637),
    (2, "Dom Juan", 1665),
    (19, "Le Misanthrope", 1666),
    (2, "Berenice", 1670),
    (8, "Pensees", 1670),
    (2, "Phedre", 1677),
    (9, "Fables", 1694)
    ;
    """
    st.code(insert_into_livre, language="sql")

# Ajouter un expander pour un autre exemple
with st.expander("Cette commande retourne les enregistrements lorsqu’il y a au moins une ligne dans chaque colonne qui correspond à la condition. Ici on donne l'ensemble des livres et auteurs dont l'id_auteur est commun au 2 tables."):
    inner_join = """
    SELECT *
    FROM livre
    INNER JOIN auteur ON auteur.id_auteur = livre.id_auteur;
    """
    st.code(inner_join, language="sql")


# Ajouter un expander pour un autre exemple
with st.expander("Cette commande permet de lister tous les résultats de la table 'livre' même s’il n’y a pas de correspondance dans la table 'auteur'."):
    left_join = """
    SELECT *
    FROM livre
    LEFT JOIN auteur ON livre.id_auteur = auteur.id_auteur;
    """
    st.code(left_join, language="sql")



