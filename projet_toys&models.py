# PAGE TOYS & MODELS
# Sous-navigation pour le Projet
sous_menu = st.sidebar.radio("Naviguez dans le Projet Toys & Models :", ["Présentation", "Requêtes SQL", "PowerBI", "Conclusion"])

# Contenu en fonction du choix dans le sous-menu
if sous_menu == "Présentation":
    st.write("### Présentation")
    st.write("Vous êtes mandaté par l'entreprise Toys & Models qui vend des modèles et des maquettes.")
    st.write("L'entreprise possède déjà une base de données qui répertorie les employés, les produits, les commandes et bien plus encore.")
    st.write("Vous êtes invité à explorer et découvrir cette base de données.")
    st.write("**Le directeur de l’entreprise souhaite avoir un tableau de bord qu’il pourrait actualiser chaque matin pour obtenir les dernières informations afin de gérer l’entreprise.**")

    st.write("### Objectif & Enjeux :")
    st.write("Votre tableau de bord doit s’articuler autour de ces 4 sujets principaux : ventes, finances, logistique, et ressources humaines. Voici les indicateurs obligatoires qui doivent figurer dans votre tableau de bord. Il est recommandé de créer des KPI supplémentaires. Cette partie est très importante pour développer vos compétences/créativité en tant que data analyst")

    st.write("""
    - Ventes : Le Nombre de produits vendus par catégorie et par mois, avec comparaison et taux de variation par rapport au même mois de l'année précédente.
    - Finances : Le chiffre d'affaires des commandes des deux derniers mois par pays.
    - Finances : Les commandes qui n'ont pas encore été payées.
    - Logistique : Le stock des 5 produits les plus commandés.
    - Ressources Humaines : Chaque mois, les 2 vendeurs ayant réalisé le plus de chiffres d'affaires
    """)

    st.write("Il arrive parfois que certains indicateurs ne soient pas réalisables techniquement. C'est à vous d'expliquer pourquoi et de proposer vos propres idées pour répondre aux besoins métiers")

    st.write("### Ressources :")
    # Expander pour afficher l'image
    with st.expander("Voir le schéma de la base de données"):
        st.image("https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/images/Toys%26models_00.png", use_container_width=True)

    st.write("### Outils :")
    st.write("Le directeur ne souhaite pas travailler avec SQL mais veut accéder aux données automatiquement et graphiquement.")
    st.write("Vous pouvez proposer l’outil de votre choix (Power BI, Tableau, etc.), tant que le tableau de bord est pertinent.")
    st.write("Base de données SQL : Vous avez le choix entre vous connecter au serveur cloud ou déployer le script localement. Les données sont identiques dans les deux cas.")

    st.write("### Livrable attendu :")
    st.write("Vous donnerez une courte présentation de votre tableau de bord (demandez à votre formateur la durée).")
    st.write("La présentation doit inclure : Vue d’ensemble du contexte, présentation de l’équipe et des outils utilisés.")
    st.write("Démonstration de votre tableau de bord, et interprétation des KPI métiers.")
    st.write("Difficultés rencontrées et perspectives d’évolution.")
    st.write("N’hésitez pas à créer des KPI supplémentaires !")

elif sous_menu == "Requêtes SQL":
    st.write("### PowerBI")
    st.write("Je vous montre 4 requêtes utilisées (1 par partie) dans ce projet.")

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

    st.write("Voici un exemple de code SQL utilisé pour la partie Finances :")
    # Ajouter un autre expander pour un autre code SQL
    with st.expander("Afficher/Cacher le code SQL"):
        sql_finances = """
        SELECT 
            `Année`,
                CASE
                WHEN `Mois` = 1 THEN "01"
                WHEN `Mois` = 2 THEN "02"
                WHEN `Mois` = 3 THEN "03"
                WHEN `Mois` = 4 THEN "04"
                WHEN `Mois` = 5 THEN "05"
                WHEN `Mois` = 6 THEN "06"
                WHEN `Mois` = 7 THEN "07"
                WHEN `Mois` = 8 THEN "08"
                WHEN `Mois` = 9 THEN "09"
                WHEN `Mois` = 10 THEN "10"
                WHEN `Mois` = 11 THEN "11"
                WHEN `Mois` = 12 THEN "12"
            END as `Mois`,
            CASE
                WHEN `Mois` = 1 THEN "01-Janvier"
                WHEN `Mois` = 2 THEN "02-Février"
                WHEN `Mois` = 3 THEN "03-Mars"
                WHEN `Mois` = 4 THEN "04-Avril"
                WHEN `Mois` = 5 THEN "05-Mai"
                WHEN `Mois` = 6 THEN "06-Juin"
                WHEN `Mois` = 7 THEN "07-Juillet"
                WHEN `Mois` = 8 THEN "08-Aout"
                WHEN `Mois` = 9 THEN "09-Septembre"
                WHEN `Mois` = 10 THEN "10-Octobre"
                WHEN `Mois` = 11 THEN "11-Novembre"
                WHEN `Mois` = 12 THEN "12-Décembre"
            END as `Libellé_Mois`,
                `Pays_Client`,
                `Nom_client`,
                `Catégorie`,
                SUM(`Total_ventes`) AS `CA`
        FROM
        (
            SELECT
                    orders.orderNumber AS `Numéro_commande`,
                    YEAR(orders.orderDate) AS `Année`,
                    MONTH(orders.orderDate) AS `Mois`,
                    customers.country AS `Pays_client`,
                    customers.customerName AS `Nom_client`,
                    products.productLine AS `Catégorie`,
                    SUM((orderdetails.quantityOrdered * orderdetails.priceEach)) AS `Total_ventes`
                FROM products
                JOIN orderdetails ON products.productCode = orderdetails.productCode
                JOIN orders ON orderdetails.orderNumber = orders.orderNumber
                JOIN customers ON customers.customerNumber = orders.customerNumber
                WHERE orders.status != "Cancelled"
                GROUP BY `Numéro_commande`, `Catégorie`
        ) AS `R1`
        GROUP BY `Pays_Client`, `Nom_client`, `Catégorie`, `Année`, `Mois`
        ORDER BY `Année` DESC, `Mois` DESC, `Pays_client`ASC
        ;          
        """
        st.code(sql_finances, language="sql")
    
    st.write("Voici un exemple de code SQL utilisé pour la partie Ressources Humaines :")
    # Ajouter un expander pour afficher le code SQL
    with st.expander("Afficher/Cacher le code SQL"):
        sql_rh = """           
        WITH `Ventes` AS 
        (
            SELECT 
                `Num_client`,
                `Num_vendeur`,
                SUM(`CA_facture`) AS `CA_client`,
                SUM(`Nb_commande`) AS `Nb_commandes_client`
            FROM
            (
                SELECT 
                    orderdetails.orderNumber AS `Num_commande`,
                    customers.customerNumber AS `Num_client`,
                    customers.salesRepEmployeeNumber AS `Num_vendeur`,
                    COUNT(orders.orderNumber) AS `Nb_commande`,
                    SUM(orderdetails.quantityOrdered * orderdetails.priceEach) AS `CA_facture`
                FROM orderdetails
                JOIN orders ON orders.orderNumber = orderdetails.orderNumber
                JOIN customers ON customers.customerNumber = orders.customerNumber
                WHERE orders.status != "Cancelled"
                GROUP BY `Num_commande`, `Num_client`, `Num_vendeur`
            ) AS `R1`
            GROUP BY `Num_client`, `Num_vendeur`
        ),
        `Vendeurs` AS
        (
            SELECT 
                offices.country AS `Pays_bureau`,
                offices.city AS `Ville_bureau`,
                employees.employeeNumber AS `Num_vendeur`,
                employees.firstName AS `Nom_vendeur`,
                employees.lastName AS `Prénom_vendeur`
            FROM employees
            JOIN offices ON offices.officeCode = employees.officeCode
            WHERE employees.jobTitle = "Sales Rep"
        )
        SELECT 
            `Pays_bureau`,
            `Ville_bureau`,
            CONCAT(`Nom_vendeur`, " ", `Prénom_vendeur`) AS `Employé`,
            COUNT(`Num_client`) AS `Nb_client`,
            SUM(`CA_client`) AS `CA_vendeur`,
            SUM(`CA_client`) / COUNT(`Num_client`) AS `CA_par_client`,
            SUM(`Nb_commandes_client`) AS `Nb_commandes`,
            SUM(`CA_client`) / SUM(`Nb_commandes_client`) AS `CA_par_commande`   
            
        FROM `Vendeurs`
        LEFT JOIN `Ventes` ON Ventes.Num_vendeur = Vendeurs.Num_vendeur
        GROUP BY `Pays_bureau`, `Ville_bureau`, `Employé`
        ;
        """
        st.code(sql_rh, language="sql")

    st.write("Voici un exemple de code SQL utilisé pour la partie Ventes :")
    # Ajouter un expander pour afficher/cacher le code SQL
    with st.expander("Afficher/Cacher le code SQL"):
        sql_ventes = """
        SELECT 
            `Bureau`,
            `Catégorie_produit`,
            `Année`,
            CASE
                WHEN `Mois` = 1 THEN "01"
                WHEN `Mois` = 2 THEN "02"
                WHEN `Mois` = 3 THEN "03"
                WHEN `Mois` = 4 THEN "04"
                WHEN `Mois` = 5 THEN "05"
                WHEN `Mois` = 6 THEN "06"
                WHEN `Mois` = 7 THEN "07"
                WHEN `Mois` = 8 THEN "08"
                WHEN `Mois` = 9 THEN "09"
                WHEN `Mois` = 10 THEN "10"
                WHEN `Mois` = 11 THEN "11"
                WHEN `Mois` = 12 THEN "12"
            END as `Mois`,
            CASE
                WHEN `Mois` = 1 THEN "01-Janvier"
                WHEN `Mois` = 2 THEN "02-Février"
                WHEN `Mois` = 3 THEN "03-Mars"
                WHEN `Mois` = 4 THEN "04-Avril"
                WHEN `Mois` = 5 THEN "05-Mai"
                WHEN `Mois` = 6 THEN "06-Juin"
                WHEN `Mois` = 7 THEN "07-Juillet"
                WHEN `Mois` = 8 THEN "08-Aout"
                WHEN `Mois` = 9 THEN "09-Septembre"
                WHEN `Mois` = 10 THEN "10-Octobre"
                WHEN `Mois` = 11 THEN "11-Novembre"
                WHEN `Mois` = 12 THEN "12-Décembre"
            END as `Libellé_Mois`,
            `Qté_commandée_année_N`,
            `Qté_commandée_année_N-1`,
            ROUND((`Qté_commandée_année_N`-`Qté_commandée_année_N-1`) / `Qté_commandée_année_N-1`, 4)  AS `Variation`
        FROM (
            SELECT 
                offices.country AS `Bureau`,
                productlines.productLine AS `Catégorie_produit`,
                YEAR(orders.orderdate) AS `Année`,    
                MONTH(orders.orderdate) AS `Mois`,
                LAG(SUM(orderdetails.quantityOrdered))
                    OVER (PARTITION BY productlines.productLine, MONTH(orders.orderdate)
                    ORDER BY productlines.productLine, MONTH(orders.orderdate), YEAR(orders.orderdate))
                AS `Qté_commandée_année_N-1`,
                SUM(orderdetails.quantityOrdered) AS `Qté_commandée_année_N`
            FROM productlines
            JOIN products ON productlines.productline = products.productline
            JOIN orderdetails ON products.productCode = orderdetails.productCode
            JOIN orders ON orders.orderNumber = orderdetails.orderNumber
            JOIN customers ON customers.customerNumber = orders.customerNumber
            JOIN employees ON employees.employeeNumber = customers.salesRepEmployeeNumber
            JOIN offices ON offices.officeCode = employees.officeCode
            WHERE orders.status != "Cancelled"
            GROUP BY
                `Bureau`,
                `Catégorie_produit`,
                `Année`,
                `Mois`
        ) AS `R1`
        ORDER BY `Année` DESC, `Mois` DESC, `Bureau` ASC;
        """
        st.code(sql_ventes, language="sql")

elif sous_menu == "PowerBI":
    st.write("### PowerBI")
    st.write("Difficile pour moi de vous donner le paramètrage dans PowerBI, j'ai opté pour la visualisation du Dashboard.")
    st.write("N'hésitez pas à naviguer à travers les différentes captures d'écran.")
    # Liste des images pour la navigation avec flèches
    images = [
        "https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/images/Toys%26models_01.png",
        "https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/images/Toys%26models_02.png",
        "https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/images/Toys%26models_03.png",
        "https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/images/Toys%26models_04.png",
        "https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/images/Toys%26models_05.png",
        "https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/images/Toys%26models_06.png",
        "https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/images/Toys%26models_07.png",
        "https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/images/Toys%26models_08.png",
        "https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/images/Toys%26models_09.png",
        "https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/images/Toys%26models_10.png",
        "https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/images/Toys%26models_11.png",
        "https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/images/Toys%26models_12.png",
        "https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/images/Toys%26models_13.png",
        "https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/images/Toys%26models_14.png",
        "https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/images/Toys%26models_15.png",
        "https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/images/Toys%26models_16.png",
        "https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/images/Toys%26models_17.png",
        "https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/images/Toys%26models_18.png"
    ]

    # Fonction pour changer l'image
    def next_image():
        if st.session_state.image_index < len(images) - 1:
            st.session_state.image_index += 1

    def prev_image():
        if st.session_state.image_index > 0:
            st.session_state.image_index -= 1

    # Ajouter les boutons pour naviguer
    col1, col2, col3 = st.columns([1, 4, 1])  # Répartition de l'espace avec une colonne vide pour "Suivante"
    
    # Le bouton "Précédente" reste à gauche
    with col1:
        if st.button("⬅ Précédente"):
            prev_image()

    # Le bouton "Suivante" est à droite
    with col3:
        if st.button("Suivante ➡"):
            next_image()

    # Index de l'image actuellement affichée
    if 'image_index' not in st.session_state:
        st.session_state.image_index = 0

    # Affichage de l'image actuelle (réduite et cliquable pour voir en grand)
    image_url = images[st.session_state.image_index]
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center;">
        <a href="{image_url}" target="_blank">
            <img src="{image_url}">
        </a>
        """,
        unsafe_allow_html=True
    )

elif sous_menu == "Conclusion":
    st.write("### Conclusion")
    st.write("Lors de mon analyse des différentes dimensions de la base de données, j’ai pu identifier des points forts ainsi que des axes d’amélioration pour chacun des domaines. Ces observations révèlent des opportunités concrètes pour améliorer nos performances globales et renforcer notre organisation.")

    st.write("**1. Domaine RH :**")
    st.write("J’ai constaté une inégalité dans la répartition des clients et du chiffre d’affaires par vendeur. Certains vendeurs n’ont aucun client rattaché (et n’ont donc pas déclenché 1 seule vente), ce qui rend difficile l’évaluation équitable de leurs performances.")
    st.write("*Recommandations :* Nous devrions enrichir la base de données avec des informations supplémentaires, telles que les temps de travail, les dates d’entrée et de sortie. À terme, cela nous permettra de mieux comparer les performances des vendeurs et de détecter les éventuelles inefficacités.")

    st.write("**2. Domaine Ventes :**")
    st.write("Mon analyse a montré qu’un client sur cinq n’est pas rattaché à un vendeur, ce qui limite le suivi et l’accompagnement des clients. En Allemagne particulièrement, un nombre significatif de clients semble non attribué, ce qui peut refléter un déséquilibre dans la répartition des vendeurs au niveau international. J’ai également identifié un produit en stock qui n’a généré aucune vente, mettant en évidence une opportunité commerciale non exploitée.")
    st.write("*Recommandations :* Nous devons mettre en place un rattachement systématique de chaque client à un vendeur dès son enregistrement. Cela renforcera le suivi client et optimisera la relation commerciale. En parallèle, il serait pertinent de revoir la répartition de nos équipes commerciales, notamment pour couvrir des territoires géographiques et stratégiques comme l’Allemagne. Enfin, il serait utile de signaler aux équipes commerciales les produits ayant des difficultés de vente pour envisager des promotions ou des offres groupées adaptées.")

    st.write("**3. Domaine Finances :**")
    st.write("J’ai observé une croissance encourageante de 33 % du chiffre d’affaires entre 2022 et 2023. Cependant, certains crédits accordés à nos clients semblent excessifs par rapport à leur chiffre d’affaires cumulé, ce qui constitue un risque financier. En parallèle, j’ai relevé des écarts dans les paiements, notamment des impayés ou des trop-perçus, qui impactent directement notre trésorerie.")
    st.write("*Recommandations :* Nous devons ajuster les crédits accordés pour qu’ils soient alignés avec le chiffre d’affaires réel de chaque client. Il est essentiel de surveiller les écarts de paiements et d’intégrer des contrôles rigoureux pour éviter les erreurs, comme des paiements sur des commandes annulées. Dans ce cas, il est crucial d’informer le client concerné pour régulariser la situation rapidement en déclenchant une nouvelle vente par exemple.")

    st.write("**4. Domaine Logistique :**")
    st.write("J’ai constaté que le stock moyen par produit est actuellement de 15 mois, un niveau bien supérieur à nos besoins. De plus, certaines commandes restent non expédiées, ce qui pourrait refléter des erreurs dans notre système de gestion des statuts de commande.")
    st.write("*Recommandations :* J’ai constaté que le stock moyen par produit est actuellement de 15 mois, un niveau bien supérieur à nos besoins. De plus, certaines commandes restent non expédiées, ce qui pourrait refléter des erreurs dans notre système de gestion des statuts de commande.")

    st.write("**Conclusion générale :**")
    st.write("Nos résultats, et notamment la forte croissance du chiffre d’affaires en 2023, sont très encourageants. Cependant, des efforts sont nécessaires pour structurer davantage nos processus internes et limiter les risques liés à la finance, à la logistique et aux ventes.")
    st.write("*Recommandations :* Nous devons consolider notre croissance en optimisant nos processus. Cela implique une meilleure gestion des ressources humaines, une relation client renforcée, un suivi rigoureux de la trésorerie, et une gestion plus efficace des stocks. En adoptant ces mesures, nous serons en mesure de renforcer la santé financière de l’entreprise et de maintenir une dynamique de croissance pérenne.")

