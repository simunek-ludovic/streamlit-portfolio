# PAGE ml
# fichier d'appui si besoin :
# 

st.header("Machine Learning")

# Contenu en fonction du choix dans le sous-menu
sous_menu = st.sidebar.radio("Naviguez dans la découverte du Machine Learning :", ["Présentation", "Régression", "Classification", "Clustering"])


# Contenu en fonction du choix dans le sous-menu
if sous_menu == "Présentation":
    st.write("### Présentation")
    st.write("Le ***Machine Learning*** est un sous-ensemble de l'intelligence artificielle (IA).")
    st.write("Cette technologie vise à apprendre aux machines à tirer des enseignements des données et à s'améliorer avec l'expérience, au lieu d'être explicitement programmées pour le faire.")
    st.write("Dans le Machine Learning, les algorithmes sont entraînés à trouver des patterns et des corrélations dans de grands ensembles de données, ainsi qu'à prendre les meilleures décisions et à émettre les meilleures prévisions en s'appuyant sur leur analyse. ")

    st.write("Le projet Recommandations de films vous permettra de naviguer dans l'univers du Machine Learning. N'hésitez pas également à aller voir les sous menus (apprentissage supervisé et apprentissage non supervisé)")

    st.write("**-------------------------------------------------------------------------------------------**")
    st.write("**Apprentissage supervisé**")
    st.write("**-------------------------------------------------------------------------------------------**")
    st.write("L'apprentissage supervisé est un type d'apprentissage automatique où nous disposons d'exemples de données labellisées.")
    st.write("Cela signifie que chaque exemple de données est associé à une étiquette ou à une classe connue.")
    st.write("L'objectif de l'apprentissage supervisé est d'apprendre à partir de ces exemples afin de pouvoir prédire ou classer correctement de nouvelles données non labellisées.")
    st.write("Prenons un exemple concret : supposons que nous ayons un ensemble de données contenant des images d'animaux où chaque observation est labellisée avec la nome de l'animal en question correspondant.")
    st.write("Dans l'apprentissage supervisé, nous utiliserions ces exemples pour former un modèle capable de reconnaître et de prédire le nom de l'animal dans de nouvelles observations (images) non labellisées.")

    st.write("**-------------------------------------------------------------------------------------------**")
    st.write("**Apprentissage non supervisé**")
    st.write("**-------------------------------------------------------------------------------------------**")
    st.write("L'apprentissage non supervisé est utilisé lorsque nous avons des données non étiquetées, c'est-à-dire des données sans informations sur les classes ou les étiquettes correspondantes.")
    st.write("L'objectif principal de l'apprentissage non supervisé est de découvrir des modèles, des structures ou des regroupements intrinsèques dans les données.")

elif sous_menu == "Régression":
    st.write("### Régression")
    st.write("La régression en apprentissage supervisé est utilisée pour prédire une valeur continue (comme le prix d'une maison) en fonction d'autres variables (caractéristiques de la maison).")
    st.write("Le modèle de régression apprend à partir d'exemples d'entraînement pour trouver une relation mathématique entre les variables d'entrée et la variable de sortie, ce qui permet ensuite de faire des prédictions sur de nouvelles données.")

    st.write("**-------------------------------------------------------------------------------------------**")
    st.write("**Régression linéaire, univariée et multivariée**")
    st.write("**-------------------------------------------------------------------------------------------**")
    st.write("La régression linéaire est une méthode d'apprentissage supervisé utilisée pour prédire une valeur numérique continue en fonction d'un ensemble de variables d'entrée.")
    st.write("Elle cherche à établir une relation linéaire entre les variables d'entrée et la variable de sortie.")
    st.write("Le but est de trouver la meilleure ligne droite qui minimise l'écart entre les valeurs prédites et les valeurs réelles.")
    st.write("Cette méthode est souvent utilisée pour résoudre des problèmes de régression, tels que la prédiction du prix d'une maison en fonction de ses caractéristiques.")

    import pandas as pd
    import streamlit as st

    # Lire le fichier CSV avec le bon séparateur et l'encodage approprié
    url = "https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/csv/winequality-white.csv"
    data = pd.read_csv(url, sep=';', encoding='utf-8')

    # Vérifier les colonnes du DataFrame
    st.write("Colonnes du DataFrame :")
    st.write(data.columns)

    # Afficher un aperçu du DataFrame
    st.dataframe(data.head(), use_container_width=True)

    # Vérifier si les colonnes spécifiques existent avant d'y accéder
    required_columns = ['density', 'residual sugar', 'total sulfur dioxide']
    missing_columns = [col for col in required_columns if col not in data.columns]

    if missing_columns:
        st.warning(f"Les colonnes suivantes sont manquantes : {', '.join(missing_columns)}")
    else:
        st.success("Toutes les colonnes sont présentes.")


    # Définir les X et les y
    X = data[['density','residual sugar', 'total sulfur dioxide']]
    y = data['alcohol']

    # Train Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

    # Créer le modèle de regression linéaire
    regression_model = LinearRegression()

    # Entrainement
    regression_model.fit(X_train.values, y_train.values)


    with st.expander("Machine Learning : Prédire la colonne 'alcohol' en tenant compte des colonnes 'density', 'residual sugar' & 'total sulfur dioxide'"):
        st.code("""
            # Définir les X et les y
            X = data[['density','residual sugar', 'total sulfur dioxide']]
            y = data['alcohol']

            # Train Test Split (avec répartition des données en 80% d'entrainements et 20% de tests)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

            # Créer le modèle de regression linéaire
            regression_model = LinearRegression()

            # Entrainement
            regression_model.fit(X_train.values, y_train.values) 
        """, language='python')


    ## Prédire sur les valeurs des données de test
    y_pred = regression_model.predict(X_test)
    y_pred


    with st.expander("Prédire sur les valeurs des données de test"):
        st.code("""
            y_pred = regression_model.predict(X_test)
            y_pred
        """, language='python')

    # Calculer le coefficient de détermination
    score = round(r2_score(y_test, y_pred),2)
    score

    with st.expander("Calculer le coefficient de détermination linéaire. C'est une mesure de la qualité de la prédiction d'une régression linéaire."):
        st.code("""
            score = round(r2_score(y_test, y_pred),2)
            score
        """, language='python')

    st.write("Score : ", score)
    st.write("Le R² étant de 0,79 signifie que 79 % de la variance des données est expliquée. Cela indique une forte corrélation entre les 3 variables explicatives (density, residual sugar & total sulfur dioxide) et la variable expliquée (alcohol) ")

    with st.expander("Afficher le coefficient de régression (a) & l'intercept (b) => y = aX+b"):
        st.code("""
            print(f"Régression linéaire - Prédiction de l'alcool en fonction de la densité, du sucre résiduel et dioxyde de souffre :")
            print(f"Coefficients de régression : {[round(coef, 2) for coef in regression_model.coef_]}")
            print(f"Intercept : {round(regression_model.intercept_, 2)}")
        """, language='python')
    
    coefficients_arrondis = [round(coef, 2) for coef in regression_model.coef_]
    st.write("Coefficients de régression : ", coefficients_arrondis)
    st.write("Intercept : ", round(regression_model.intercept_, 2))

    with st.expander("Prédisons 'alcohol' en donnant les valeurs de density (0.99), residual sugar (2.5) & total sulfur dioxide (30)"):
        st.code("""
        # prediction sur des Nouvelles données
        new_data = [[0.99, 2.5, 30]]

        prediction = regression_model.predict(new_data)
        print(prediction)
        """, language='python')
    
    new_data = [[0.99, 2.5, 30]]
    prediction = regression_model.predict(new_data)

    # Arrondir la prédiction à 2 décimales
    rounded_prediction = round(prediction[0], 1)

    # Affichage de la prédiction avec Streamlit
    st.code(f"Prédiction : {rounded_prediction}")

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

    st.write("**-------------------------------------------------------------------------------------------**")
    st.write("**Arbres de décision**")
    st.write("**-------------------------------------------------------------------------------------------**")
    st.write("Les arbres de décision sont des algorithmes d'apprentissage automatique supervisé utilisés pour résoudre des problèmes de classification et de régression.")
    st.write("Ils sont basés sur une structure d'arbre où chaque nœud représente une caractéristique (ou une variable) et chaque branche représente une décision basée sur cette caractéristique.")

    with st.expander("Convertir ce fichier CSV en DataFrame et importation des bibliothèques nécessaires"):
        st.code("""
            from sklearn.model_selection import train_test_split
            from sklearn.tree import DecisionTreeRegressor
            from sklearn.metrics import mean_squared_error

            import pandas as pd
            from sklearn.datasets import fetch_california_housing # "https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/csv/datasets_california_housing.csv"

            # Charger l'ensemble de données California Housing
            data = fetch_california_housing()
            df = pd.DataFrame(data.data, columns=data.feature_names)
            df.sample(3)
        """, language='python')

    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeRegressor
    from sklearn.metrics import mean_squared_error

    import numpy as np
    import pandas as pd

    from sklearn.datasets import fetch_california_housing # "https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/csv/datasets_california_housing.csv"

    # Charger l'ensemble de données California Housing
    data = fetch_california_housing()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    # Afficher le DataFrame dans Streamlit
    st.dataframe(df, use_container_width=True)



    with st.expander("Calcul des métriques MSE et RMSE "):
        st.code("""
            # Définition des données (features et target)
            X = data.data  # Variables explicatives (caractéristiques des maisons)
            y = data.target  # Valeur médiane des maisons en centaines de milliers de dollars

            # Diviser les données en ensembles d'entraînement (80%) et de test (20%)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            # `test_size=0.2` signifie que 20% des données sont utilisées pour le test et 80% pour l'entraînement
            # `random_state=42` permet de fixer la répartition pour obtenir les mêmes résultats à chaque exécution

            # Création d'un modèle d'arbre de décision pour la régression
            tree_regressor = DecisionTreeRegressor()

            # Entraînement du modèle sur les données d'entraînement
            tree_regressor.fit(X_train, y_train)
            # L'arbre de décision apprend à partir des données pour établir des règles de décision et prédire la valeur cible

            # Prédiction des valeurs de sortie sur l'ensemble de test
            y_pred = tree_regressor.predict(X_test)
            # Le modèle applique ce qu'il a appris pour estimer la valeur cible des données de test

            # Calcul de l'erreur quadratique moyenne (MSE - Mean Squared Error)
            mse = mean_squared_error(y_test, y_pred)
            # Le MSE représente la moyenne des erreurs au carré entre les valeurs réelles et les valeurs prédites
            print("MSE :", round(mse, 3))

            # Calcul de l'erreur quadratique moyenne (RMSE - Root Mean Squared Error)
            rmse = np.sqrt(mse)
            # Le RMSE est la racine carrée du MSE, ce qui permet d'avoir une erreur exprimée dans la même unité que la cible
            print("RMSE :", round(rmse, 3))
        """, language='python')


    # Définition des données (features et target)
    X = data.data  # Variables explicatives (caractéristiques des maisons)
    y = data.target  # Valeur médiane des maisons en centaines de milliers de dollars

    # Diviser les données en ensembles d'entraînement (80%) et de test (20%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # `test_size=0.2` signifie que 20% des données sont utilisées pour le test et 80% pour l'entraînement
    # `random_state=42` permet de fixer la répartition pour obtenir les mêmes résultats à chaque exécution

    # Création d'un modèle d'arbre de décision pour la régression
    tree_regressor = DecisionTreeRegressor()

    # Entraînement du modèle sur les données d'entraînement
    tree_regressor.fit(X_train, y_train)
    # L'arbre de décision apprend à partir des données pour établir des règles de décision et prédire la valeur cible

    # Prédiction des valeurs de sortie sur l'ensemble de test
    y_pred = tree_regressor.predict(X_test)
    # Le modèle applique ce qu'il a appris pour estimer la valeur cible des données de test

    # Calcul de l'erreur quadratique moyenne (MSE - Mean Squared Error)
    mse = mean_squared_error(y_test, y_pred)
    # Le MSE représente la moyenne des erreurs au carré entre les valeurs réelles et les valeurs prédites
    st.write("MSE :", round(mse, 3))

    # Calcul de l'erreur quadratique moyenne (RMSE - Root Mean Squared Error)
    rmse = np.sqrt(mse)
    # Le RMSE est la racine carrée du MSE, ce qui permet d'avoir une erreur exprimée dans la même unité que la cible
    st.write("RMSE :", round(rmse, 3))

    with st.expander("Prédisons la valeur d'une maison avec un nouveau jeu de données"):
        st.code("""
            # prediction sur des Nouvelles données
            new_data = [[3.2, 36.0, 6.984127, 1.022, 250.0, 2.8, 37.88, -121.23]]

            prediction = tree_regressor.predict(new_data)
            print(prediction * 100000)
        """, language='python')

    # prediction sur des Nouvelles données
    new_data = [[3.2, 36.0, 6.984127, 1.022, 250.0, 2.8, 37.88, -121.23]]

    # Prédiction avec le modèle tree_regressor (par exemple un arbre de décision)
    prediction = tree_regressor.predict(new_data)

    # Accès à la première valeur de la prédiction et conversion en float pour l'affichage
    predicted_price = round(float(prediction[0]) * 100000, 0)

    # Affichage du prix estimé formaté
    st.write(f"Valeur médiane estimée de la maison : {predicted_price:,.0f} $")


    st.write("**-------------------------------------------------------------------------------------------**")
    st.write("**KNN (nearest neighbors) regressor**")
    st.write("**-------------------------------------------------------------------------------------------**")
    st.write("L'idée principale de cet algorithme est de prédire la valeur d'une variable cible en se basant sur les valeurs des k échantillons les plus proches dans l'espace des caractéristiques.")
    st.write("Le KNN Regressor est relativement simple à comprendre et à mettre en œuvre. Cependant, il est important de noter qu'il peut être sensible à l'échelle des caractéristiques, donc il est souvent recommandé de normaliser les données avant d'appliquer l'algorithme.")
    st.write("N'oubliez pas que le choix approprié de k peut avoir un impact significatif sur les performances de prédiction du modèle. Une valeur trop petite de k peut rendre le modèle sensible au bruit, tandis qu'une valeur trop grande peut rendre le modèle trop généralisé.")

    
    with st.expander("Convertir ce fichier CSV en DataFrame et importation des bibliothèques nécessaires"):
        st.code("""
            # Importation du modèle KNeighborsRegressor pour la régression par k plus proches voisins
            from sklearn.neighbors import KNeighborsRegressor

            # Importation du dataset California Housing de Scikit-Learn
            # Ce dataset contient des informations sur les logements en Californie,
            # avec 8 variables explicatives et la valeur médiane des maisons.
            from sklearn.datasets import fetch_california_housing

            # Chargement du dataset
            data = fetch_california_housing()

            # Séparation des données en variables explicatives (X) et variable cible (y)
            X = data.data  # Caractéristiques des maisons (ex: latitude, longitude, taille, nombre de pièces...)
            y = data.target  # Valeur médiane des maisons (en centaines de milliers de dollars)

            # Affichage des dimensions des données
            print(f"Dimensions des données X : {X.shape}")  # Nombre d'échantillons et de caractéristiques
            print(f"Dimensions de la cible y : {y.shape}")  # Nombre de valeurs cibles
        """, language='python')

    from sklearn.neighbors import KNeighborsRegressor

    from sklearn.datasets import fetch_california_housing # "https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/csv/datasets_california_housing.csv"

    # Load the dataset
    data = fetch_california_housing()
    X = data.data # Variables explicatives (caractéristiques des maisons)
    y = data.target # Valeur médiane des maisons en centaines de milliers de dollars

    with st.expander("Calculer le score en utilisant k = 3"):
        st.code("""
        # Importation des bibliothèques nécessaires
        from sklearn.model_selection import train_test_split  # Pour diviser les données en ensembles d'entraînement et de test
        from sklearn.neighbors import KNeighborsRegressor  # Modèle de régression KNN
        from sklearn.metrics import mean_squared_error  # Pour évaluer la performance du modèle
        import numpy as np  # Pour calculer la racine carrée du MSE

        # Division du dataset en ensembles d'entraînement (80%) et de test (20%)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Vérification des dimensions des ensembles
        print(f"Entraînement : {X_train.shape[0]} échantillons, {X_train.shape[1]} caractéristiques")
        print(f"Test : {X_test.shape[0]} échantillons, {X_test.shape[1]} caractéristiques")

        # Application de la régression KNN avec k=3 voisins
        knn_regressor = KNeighborsRegressor(n_neighbors=3)  # On choisit 3 voisins
        knn_regressor.fit(X_train, y_train)  # Entraînement du modèle sur les données d'entraînement

        # Prédiction sur l'ensemble de test
        predictions = knn_regressor.predict(X_test)
        """, language='python')

    # Importation des bibliothèques nécessaires
    from sklearn.model_selection import train_test_split  # Pour diviser les données en ensembles d'entraînement et de test
    from sklearn.neighbors import KNeighborsRegressor  # Modèle de régression KNN
    from sklearn.metrics import mean_squared_error  # Pour évaluer la performance du modèle
    import numpy as np  # Pour calculer la racine carrée du MSE

    # Division du dataset en ensembles d'entraînement (80%) et de test (20%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Vérification des dimensions des ensembles
    print(f"Entraînement : {X_train.shape[0]} échantillons, {X_train.shape[1]} caractéristiques")
    print(f"Test : {X_test.shape[0]} échantillons, {X_test.shape[1]} caractéristiques")

    # Application de la régression KNN avec k=3 voisins
    knn_regressor = KNeighborsRegressor(n_neighbors=3)  # On choisit 3 voisins
    knn_regressor.fit(X_train, y_train)  # Entraînement du modèle sur les données d'entraînement

    # Prédiction sur l'ensemble de test
    predictions = knn_regressor.predict(X_test)

   
    with st.expander("Prédisons la valeur d'une maison avec un nouveau jeu de données"):
        st.code("""
            # prediction sur des Nouvelles données
            new_data = [[3.2, 36.0, 6.984127, 1.022, 250.0, 2.8, 37.88, -121.23]]

            prediction = knn_regressor.predict(new_data)
            print(prediction * 100000)
        """, language='python')

    # prediction sur des Nouvelles données
    new_data = [[3.2, 36.0, 6.984127, 1.022, 250.0, 2.8, 37.88, -121.23]]

    # Prédiction avec le modèle KNN
    prediction = knn_regressor.predict(new_data)

    # Conversion en float pour éviter les bugs et mise en forme du résultat
    predicted_price = round(float(prediction[0]) * 100000, 0)

    # Affichage du prix estimé
    st.write(f"Valeur médiane estimée de la maison : {predicted_price:,.0f} $")



elif sous_menu == "Classification":
    st.write("### Classification")
    st.write("La classification supervisée utilise des données d'entraînement labellisées avec des catégories connues pour apprendre à prédire correctement la classe d'un nouvel échantillon.")
    st.write("L'algorithme est entrainé pour faire correspondre les caractéristiques d'un échantillon à une classe prédéfinie.")

    st.write("**-------------------------------------------------------------------------------------------**")
    st.write("**KNN (Nearest Neighbors)**")
    st.write("**-------------------------------------------------------------------------------------------**")
    st.write("K-NN peut être utilisé pour résoudre à la fois les problèmes de classification et de régression.")
    st.write("k fait référence au nombre de voisins les plus proches des données que nous essayons de classer.")

    with st.expander("Convertir ce fichier CSV en DataFrame et importation des bibliothèques nécessaires"):
        st.code("""
        import pandas as pd

        df_pokemon = pd.read_csv('https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/csv/pokemon.csv')
        df_pokemon.head(3)
        """, language='python')

    import pandas as pd

    df_pokemon = pd.read_csv('https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/csv/pokemon.csv')
    df_pokemon.head(3)
    # Afficher le DataFrame dans Streamlit
    st.dataframe(df_pokemon, use_container_width=True)


    with st.expander("Netoyage du DataFrame"):
        st.code("""
        # data preprocessing: on elimine les pokemons legendaires car nous cherchons les pokemon non legendaire, les plus similaires à des legendaires
        df = df_pokemon.copy()
        df.drop("Type 2", axis= 1, inplace = True)
        df_no_legendary = df[df["Legendary"] == False]

        X_gen = df_no_legendary.select_dtypes('number').drop(columns = ["#"]) 
        """, language='python')

    # data preprocessing: on elimine les pokemons legendaires car nous cherchons les pokemon non legendaire, les plus similaires à des legendaires
    df = df_pokemon.copy()
    df.drop("Type 2", axis= 1, inplace = True)
    df_no_legendary = df[df["Legendary"] == False]

    X_gen = df_no_legendary.select_dtypes('number').drop(columns = ["#"]) # on ne selectionne que les features numériques,
                                                                        # on supprime l'index qui n'apporte aucune information pertinente



    with st.expander("Affichage des pokemons non légendaires les plus proches de quelques pokemons légendaires"):
        st.code("""        
            # on initialise le model
            from sklearn.neighbors import NearestNeighbors

            model_KNN_gen = NearestNeighbors(n_neighbors=5).fit(X_gen)

            # on definie liste de pokemons legandaires cible
            poke_list = ["Mewtwo", "Lugia", "Rayquaza", "Giratina Altered Forme"]

            for pokemon in poke_list:
                neighbors_gen = model_KNN_gen.kneighbors(df.loc[df['Name'] == pokemon, X_gen.columns])

                print(f"Recommandations for Pokemon {pokemon} :")

                closest_pok_ind = neighbors_gen[1][0]
                closest_pok = df_no_legendary['Name'].iloc[closest_pok_ind]
                print("Closest Pokemons : ", list(closest_pok))
                print("Respectives distances : ", neighbors_gen[0][0])
                print()
    """, language='python')

    # on initialise le model
    from sklearn.neighbors import NearestNeighbors

    model_KNN_gen = NearestNeighbors(n_neighbors=5).fit(X_gen)

    # on definie liste de pokemons legandaires cible
    poke_list = ["Mewtwo", "Lugia", "Rayquaza", "Giratina Altered Forme"]

    # Boucle pour afficher les résultats pour chaque Pokémon légendaire
    for pokemon in poke_list:
        neighbors_gen = model_KNN_gen.kneighbors(df.loc[df['Name'] == pokemon, X_gen.columns])

        st.write(f"Recommandations pour le Pokémon : {pokemon}")
        
        closest_pok_ind = neighbors_gen[1][0]
        closest_pok = df.loc[closest_pok_ind, "Name"]
        closest_pok_distances = neighbors_gen[0][0]

        # Créer un dataframe pour afficher les résultats de manière structurée
        recommendations_df = pd.DataFrame({
            "Pokémon proche": closest_pok,
            "Distance": closest_pok_distances
        })

        # Afficher le dataframe sur Streamlit avec un meilleur format
        st.dataframe(recommendations_df)


    st.write("**-------------------------------------------------------------------------------------------**")
    st.write("**Regression Logistique**")
    st.write("**-------------------------------------------------------------------------------------------**")
    st.write("La régression logistique est une technique utilisée en apprentissage automatique pour résoudre des problèmes de classification binaire, c'est-à-dire lorsque nous voulons prédire une variable de sortie qui peut prendre seulement deux valeurs, par exemple 'oui' ou 'non', 'vrai' ou 'faux', 'spam' ou 'non-spam', etc.")

    with st.expander("Convertir ce fichier CSV en DataFrame et importation des bibliothèques nécessaires"):
        st.code("""
            import numpy as np
            import seaborn as sns
            import matplotlib.pyplot as plt

            import pandas as pd

            link = "https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/csv/titanic.csv"
            df_titanic = pd.read_csv(link)

            # quick preprocessing
            df_titanic['Survived_label'] = df_titanic['Survived'].apply(lambda x: "Survived" if x == 1 else "Dead")
            df_titanic['Sex_facto'] = df_titanic['Sex'].factorize()[0]

            df_titanic.sample(3)
        """, language='python')


    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt

    import pandas as pd

    link = "https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/csv/titanic.csv"
    df_titanic = pd.read_csv(link)

    # quick preprocessing
    df_titanic['Survived_label'] = df_titanic['Survived'].apply(lambda x: "Survived" if x == 1 else "Dead")
    df_titanic['Sex_facto'] = df_titanic['Sex'].factorize()[0]

    # Afficher le DataFrame dans Streamlit
    st.dataframe(df_titanic, use_container_width=True)



    with st.expander("Paramètrer le train test split et Initalisation du modèle"):
        st.code("""
            # train test split
            from sklearn.model_selection import train_test_split

            X = df_titanic.drop(columns=['Survived_label', "Name", "Sex", "Survived"])  # garde toutes les colonnes numerique excepté "survived" que l'on cherche à predire
            y = df_titanic['Survived_label']

            X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 36, train_size= 0.7)

            # initialisation du modèle
            from sklearn.linear_model import LogisticRegression

            log_model = LogisticRegression().fit(X_train.values, y_train.values)

            # Affichage avec 2 chiffres après la virgule
            print('Accuracy score on train set:', round(log_model.score(X_train.values, y_train.values), 2))
            print('Accuracy score on test set:', round(log_model.score(X_test.values, y_test.values), 2))

        """, language='python')

    # train test split
    from sklearn.model_selection import train_test_split

    X = df_titanic.drop(columns=['Survived_label', "Name", "Sex", "Survived"])  # garde toutes les colonnes numerique excepté "survived" que l'on cherche à predire
    y = df_titanic['Survived_label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 36, train_size= 0.7)

    # initialisation du modèle
    from sklearn.linear_model import LogisticRegression

    log_model = LogisticRegression().fit(X_train.values, y_train.values)

    # Affichage avec 2 chiffres après la virgule
    st.write('Accuracy score on train set:', round(log_model.score(X_train.values, y_train.values), 2))
    st.write('Accuracy score on test set:', round(log_model.score(X_test.values, y_test.values), 2))







    with st.expander("Affichage de la matrice de confusion"):
        st.code("""
            # Importation de la fonction confusion_matrix depuis sklearn.metrics
            from sklearn.metrics import confusion_matrix

            # Création de la matrice de confusion en utilisant les vraies valeurs et les prédictions
            pd.DataFrame(
                # On passe la matrice de confusion générée par confusion_matrix()
                data = confusion_matrix(y_true = y_test, y_pred = log_model.predict(X_test.values)),
                
                # Personnalisation des indices (lignes) avec les classes du modèle + le suffixe "(valeur actuelle)"
                # Cela représente les vraies classes (réellement observées) dans les données de test
                index = log_model.classes_ + " (valeur actuelle)",
                
                # Personnalisation des colonnes avec les classes du modèle + le suffixe "(valeur prédite)"
                # Cela représente les classes prédites par le modèle sur les données de test
                columns = log_model.classes_ + " (valeur prédite)"
            )
        """, language='python')


    import streamlit as st
    import pandas as pd
    from sklearn.metrics import confusion_matrix

    # Calcul de la matrice de confusion
    conf_matrix = confusion_matrix(y_true = y_test, y_pred = log_model.predict(X_test.values))

    # Création du DataFrame avec personnalisation des indices et colonnes
    conf_matrix_df = pd.DataFrame(
        data = conf_matrix,
        index = log_model.classes_ + " (valeur actuelle)",
        columns = log_model.classes_ + " (valeur prédite)"
    )

    # Affichage de la matrice de confusion dans Streamlit
    st.dataframe(conf_matrix_df, use_container_width=True)

    st.write("138 vrais positifs (réel : décédé / prévision : décédé)")
    st.write("76 vrais négatifs (réel : survivant / prévision : survivant)")
    st.write("23 faux positifs (réel : décédé / prévision : survivant)")
    st.write("30 faux négatifs (réel : surivant / prévision : décédé)")


elif sous_menu == "Clustering":
    st.write("### Clustering")
    st.write("Le clustering est généralement considéré comme une technique de classification non supervisée.")
    st.write("La classification non supervisée fait référence à des méthodes où les données ne sont pas étiquetées et où l'objectif est de regrouper les données similaires en fonction de leurs caractéristiques communes.")

    st.write("**-------------------------------------------------------------------------------------------**")
    st.write("**K-Means**")
    st.write("**-------------------------------------------------------------------------------------------**")
    st.write("L'utilité principale du K-means pour les data analysts est de fournir des informations sur la similarité entre les points de données.")
    st.write("En regroupant les données en clusters, le K-means permet d'identifier des sous-groupes au sein de l'ensemble de données et de comprendre comment les points de données se regroupent en fonction de leurs caractéristiques.")
    st.write("Le K-means est souvent utilisé pour effectuer des analyses exploratoires de données, identifier des tendances ou des schémas cachés, segmenter les clients en groupes basés sur leur comportement d'achat, regrouper des documents similaires dans le traitement du langage naturel, ou encore prétraiter les données avant d'appliquer d'autres techniques d'apprentissage automatique.")

    with st.expander("Convertir ce fichier CSV en DataFrame et importation des bibliothèques nécessaires"):
        st.code("""

            # Importe la classe KMeans du module sklearn.cluster pour effectuer des analyses de clustering.
            from sklearn.cluster import KMeans

            # Importe la bibliothèque pandas pour la manipulation et l'analyse des données.
            import pandas as pd

            # Importe la fonction fetch_california_housing du module sklearn.datasets pour récupérer le jeu de données sur le logement en Californie.
            from sklearn.datasets import fetch_california_housing

            # Charge un jeu de données à partir d'une URL GitHub contenant des informations sur les fleurs d'iris, et le stocke dans un DataFrame pandas.
            df = pd.read_csv("https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/csv/iris.csv")

            # Affiche les trois premières lignes du DataFrame pour avoir un aperçu des données.
            df.head(3)

        """, language='python')

    import streamlit as st
    from sklearn.cluster import KMeans
    import pandas as pd
    from sklearn.datasets import fetch_california_housing

    # Charger le jeu de données Iris depuis un URL GitHub
    df = pd.read_csv("https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/csv/iris.csv")

    # Afficher le DataFrame dans Streamlit
    st.dataframe(df, use_container_width=True)


    with st.expander("Créer un modèle Kmeans"):
        st.code("""
            # Crée un modèle KMeans avec 3 clusters et utilise l'option 'auto' pour déterminer automatiquement le nombre d'initialisations.
            modelKM = KMeans(n_clusters=3, n_init="auto")

            # Ajuste le modèle KMeans aux données du DataFrame, en excluant la dernière colonne (qui est généralement la colonne cible ou d'étiquettes).
            modelKM.fit(df.iloc[:, :-1])

            modelKM.labels_ # a chaque observation son cluster identifié, c'est avec cet information que vous créerez votre colonne de labelisation
        """, language='python')




    # Créer un modèle KMeans avec 3 clusters et n_init="auto" pour déterminer automatiquement le nombre d'initialisations
    modelKM = KMeans(n_clusters=3, n_init="auto")

    # Ajuster le modèle KMeans aux données du DataFrame, en excluant la dernière colonne (généralement la colonne cible ou d'étiquettes)
    modelKM.fit(df.iloc[:, :-1])

    # Ajouter les labels de clusters au DataFrame
    df['Cluster'] = modelKM.labels_

    # Afficher les résultats des clusters
    st.write("Résultats du clustering (avec labels de clusters - 3 clusters de 0 à 2) :")
    st.dataframe(df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'Cluster']], use_container_width=True)


    with st.expander(" Accèdr aux coordonnées des centres des clusters déterminés par le modèle KMeans."):
        st.code("""
            # Chaque centre est représenté par un tableau de valeurs, correspondant à la moyenne des points assignés à ce cluster.
            # L'ordre des colonnes est conservé, ce qui signifie que les valeurs des centres de clusters sont alignées avec les colonnes du DataFrame d'origine.
            modelKM.cluster_centers_

        """, language='python')


    # Afficher les centres des clusters
    st.write("Centres des clusters :")
    st.write(modelKM.cluster_centers_)




    with st.expander(" Faire de la visualisation"):
        st.code("""
            # Importe les bibliothèques seaborn et matplotlib pour la visualisation des données.
            import seaborn as sns
            import matplotlib.pyplot as plt

            # Crée une figure avec deux sous-graphes côte à côte, partageant le même axe y.
            fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 5), sharey=True)

            # Graphe de gauche : visualisation des clusters avec les centres de clusters en vert.
            sns.scatterplot(ax=ax[0],                     # Spécifie le sous-graphe de gauche.
                            x=df['sepal_length'],         # Utilise la longueur des sépales comme axe x.
                            y=df['petal_width'],          # Utilise la largeur des pétales comme axe y.
                            hue=modelKM.labels_)          # Colore les points selon les clusters attribués.

            # Ajoute les centres des clusters au graphe de gauche, marqués par des croix vertes.
            ax[0].scatter(x=modelKM.cluster_centers_[:, 0],  # Longueur des sépales des centres de clusters.
                        y=modelKM.cluster_centers_[:, 3],  # Largeur des pétales des centres de clusters.
                        s=400, c='limegreen',            # Taille et couleur des marqueurs.
                        marker="X")                      # Forme des marqueurs.

            ax[0].set_title("3 clusters")  # Définit le titre du graphe de gauche.

            # Graphe de droite : visualisation des espèces originales.
            sns.scatterplot(ax=ax[1],                     # Spécifie le sous-graphe de droite.
                            x=df['sepal_length'],         # Utilise la longueur des sépales comme axe x.
                            y=df['petal_width'],          # Utilise la largeur des pétales comme axe y.
                            hue=df['species'])            # Colore les points selon les espèces d'origine.

            ax[1].set_title("3 original species")  # Définit le titre du graphe de droite.

            # Affiche les graphes.
            plt.show()

        """, language='python')


    import seaborn as sns
    import matplotlib.pyplot as plt
    import streamlit as st

    # Crée une figure avec deux sous-graphes côte à côte, partageant le même axe y.
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 5), sharey=True)

    # Graphe de gauche : visualisation des clusters avec les centres de clusters en vert.
    sns.scatterplot(ax=ax[0],                     # Spécifie le sous-graphe de gauche.
                    x=df['sepal_length'],         # Utilise la longueur des sépales comme axe x.
                    y=df['petal_width'],          # Utilise la largeur des pétales comme axe y.
                    hue=modelKM.labels_)          # Colore les points selon les clusters attribués.

    # Ajoute les centres des clusters au graphe de gauche, marqués par des croix vertes.
    ax[0].scatter(x=modelKM.cluster_centers_[:, 0],  # Longueur des sépales des centres de clusters.
                y=modelKM.cluster_centers_[:, 3],  # Largeur des pétales des centres de clusters.
                s=400, c='limegreen',            # Taille et couleur des marqueurs.
                marker="X")                      # Forme des marqueurs.

    ax[0].set_title("3 clusters")  # Définit le titre du graphe de gauche.

    # Graphe de droite : visualisation des espèces originales.
    sns.scatterplot(ax=ax[1],                     # Spécifie le sous-graphe de droite.
                    x=df['sepal_length'],         # Utilise la longueur des sépales comme axe x.
                    y=df['petal_width'],          # Utilise la largeur des pétales comme axe y.
                    hue=df['species'])            # Colore les points selon les espèces d'origine.

    ax[1].set_title("3 original species")  # Définit le titre du graphe de droite.

    # Affiche les graphes sur Streamlit.
    st.pyplot(fig)







