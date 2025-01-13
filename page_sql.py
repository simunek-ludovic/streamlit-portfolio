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


st.write("### PowerBI")
st.write("Voici un exemple de code SQL utilisé pour la partie Logistique :")
# Ajouter un expander pour un autre exemple
with st.expander("Afficher/Cacher le code SQL"):
    sql_logistique = """
    SELECT 
        customers.country AS `Pays_client`,
        productLine AS `Catégorie_produit`,
        products.productName AS `Nom_produit`,
        productScale AS `Echelle`,
        DATE_FORMAT(orders.orderDate, "%d/%m/%Y") AS `Date_commande`,
        DATE_FORMAT( orders.shippedDate, "%d/%m/%Y") AS `Date_envoi`,
        DATEDIFF(orders.shippedDate, orders.orderDate) AS `Délai_envoi`
    FROM products
    JOIN orderdetails ON products.productCode = orderdetails.productCode
    JOIN orders ON orderdetails.orderNumber = orders.orderNumber
    JOIN customers ON customers.customerNumber = orders.customerNumber
    WHERE orders.status = "Shipped"
    ;
    """
    st.code(sql_logistique, language="sql")
