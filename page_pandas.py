# PAGE pandas
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# fichier d'appui si besoin :
# https://raw.githubusercontent.com/WCSLeadData/Html/main/online_store_customer_data.csv

# Sous-navigation pour le Projet
sous_menu = st.sidebar.radio("Naviguez dans la découverte de Pandas :", ["Présentation et collecte", "Pré-traitement", "Nettoyage", "Analyse", "Visualisation"])

# Contenu en fonction du choix dans le sous-menu
if sous_menu == "Présentation et collecte":
    st.write("***Pandas*** est une bibliothèque Python très populaire pour la manipulation et l'analyse de données. Elle permet de traiter efficacement des données sous forme de tableaux (similaires aux feuilles de calcul Excel ou aux bases de données SQL")
    st.write("Nous allons travailler avec ce fichier [CSV](https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/csv/online_store_customer_data.csv) qui contient environ 2500 lignes et 11 colonnes.")
    import pandas as pd
    
    with st.expander("Convertir ce fichier CSV en DataFrame 'df_csv'"):
        st.code("""
        import pandas as pd
        url="https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/csv/online_store_customer_data.csv"
        df_csv = pd.read_csv(url)            
        df_csv
        """, language='python')
        url="https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/csv/online_store_customer_data.csv"
        df_csv = pd.read_csv(url)            

    # Charger le fichier CSV
    df = pd.read_csv("https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/csv/online_store_customer_data.csv")

    # Afficher le DataFrame dans Streamlit
    st.dataframe(df, use_container_width=True)


elif sous_menu == "Pré-traitement":
    # Charger le fichier CSV
    df_csv = pd.read_csv("https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/csv/online_store_customer_data.csv")

    # Code
    st.write("Nous allons parcourir quelques exemples d'utilisation du **Pré-traitement des données** :")

    with st.expander("Afficher les 4 premières lignes"):
        st.code("""
        df_csv.head(4)
        """, language='python')
        st.dataframe(df_csv.head(4), use_container_width=True)

    # Code
    with st.expander("Afficher les 6 dernières lignes"):
        st.code("""
        df_csv.tail(6)
        """, language='python')
        st.dataframe(df_csv.tail(6), use_container_width=True)

    # Code
    with st.expander("Afficher 3 lignes aléatoires"):
        st.code("""
        df_csv.sample(3)
        """, language='python')
        st.dataframe(df_csv.sample(3), use_container_width=True)

    # Code
    with st.expander("Afficher les types de données de chaque colonne"):
        st.code("""
        df_csv.dtypes
        """, language='python')
        st.dataframe(df_csv.dtypes, use_container_width=True)

    # Code
    with st.expander("Compter le nombre de types de données dans le DataFrame"):
        st.code("""
        df_csv.dtypes.value_counts()
        """, language='python')
        st.dataframe(df_csv.dtypes.value_counts(), use_container_width=True)

    # Code
    with st.expander("Afficher 6 lignes aléatoires avec uniquement les colonnes Age, Transaction_date et Gender"):
        st.code("""
        df_csv[["Age", "Transaction_date", "Gender"]].sample(6)
        """, language='python')
        st.dataframe(df_csv[["Age", "Transaction_date", "Gender"]].sample(6), use_container_width=True)

    # Code
    with st.expander("Afficher les 3 premières lignes des colonnes Transaction_ID, State_names, Employees_status, Payment_method and Amount_spent"):
        st.code("""
        df_csv.loc[0:2, ["Transaction_ID", "State_names", "Employees_status", "Payment_method", "Amount_spent"]]
        """, language='python')
        st.dataframe(df_csv.loc[0:2, ["Transaction_ID", "State_names", "Employees_status", "Payment_method", "Amount_spent"]], use_container_width=True)

    # Code
    with st.expander("Filtrer le DataFrame pour afficher seulement les lignes où Marital_status = 'Married'"):
        st.code("""
        df_csv = df_csv[df_csv["Marital_status"] == "Married"]
        df_csv
        """, language='python')
        st.dataframe(df_csv[df_csv["Marital_status"] == "Married"], use_container_width=True)
    
    # Code
    with st.expander("Autres codes possibles"):
        st.code("""
        df_csv.shape  # Affiche la forme du DataFrame (nombre de lignes et de colonnes)
        df_csv.info()  # Affiche un résumé des informations du DataFrame (types de données, valeurs non nulles, etc...)
        df_csv.columns  # Affiche les noms des colonnes du DataFrame
        """, language='python')


elif sous_menu == "Nettoyage":
    # Charger le fichier CSV
    df_csv = pd.read_csv("https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/csv/online_store_customer_data.csv")

    # Code
    st.write("Nous allons parcourir quelques exemples du **Nettoyage des données** :")

    st.write("Avant de commencer, nous allons faire une copie du DataFrame 'df_csv' que l'on nommera 'df' afin de ne pas toucher au DataFrame initial")

    # Code
    with st.expander("Copier un DataFrame"):
        st.code("""
        df = df_csv.copy()
        df
        """, language='python')
        df = df_csv.copy()
        st.dataframe(df, use_container_width=True)

    # Code
    with st.expander("Renommer les colonnes du DataFrame"):
        st.code("""
        df = df.rename(columns={
            "Transaction_date" : "Date",
            "Transaction_ID" : "ID",
            "Gender" : "Sexe",
            "Marital_status" : "Statut_marital",
            "State_names" : "Ville",
            "Employees_status" : "Statut_employé",
            "Segment" : "Abonnement",
            "Payment_method" : "Méthode_paiement",
            "Referal" : "Référence",
            "Amount_spent" : "Montant_dépensé"
            })

        df.sample(2)
        """, language='python')

        df = df.rename(columns={
            "Transaction_date" : "Date",
            "Transaction_ID" : "ID",
            "Gender" : "Sexe",
            "Marital_status" : "Statut_marital",
            "State_names" : "Ville",
            "Employees_status" : "Statut_employé",
            "Segment" : "Abonnement",
            "Payment_method" : "Méthode_paiement",
            "Referal" : "Référence",
            "Amount_spent" : "Montant_dépensé"
            })
        st.dataframe(df.sample(2), use_container_width=True)

    # Code
    with st.expander("Ajouter une nouvelle colonne 'new_col' qui sera égale à 'Montant_dépensé' * 10"):
        st.code("""
        df["new_col"] = df["Montant_dépensé"] * 10
        df.head(3)
        """, language='python')
        df["new_col"] = df["Montant_dépensé"] * 10
        df.head(3)
        st.dataframe(df.head(3), use_container_width=True)

    # Code
    with st.expander("Supprimer la colonne 'new_col' et 'Référence'"):
        st.code("""
        df.drop(columns=["Référence", "new_col"], inplace=True)
        df.head(3)
        """, language='python')
        df.drop(columns=["Référence", "new_col"], inplace=True)
        st.dataframe(df.head(3), use_container_width=True)

    # Code
    with st.expander("Dans les colonnes Sexe & Statut_marital , mettre les termes Français"):
        st.code("""
        df.loc[df["Sexe"] == "Male", "Sexe"] = "Homme"
        df.loc[df["Sexe"] == "Female", "Sexe"] = "Femme"
        df["Statut_marital"] = df["Statut_marital"].replace({"Single": "Célibataire", "Married": "Marié"})
        """, language='python')
        df.loc[df["Sexe"] == "Male", "Sexe"] = "Homme"
        df.loc[df["Sexe"] == "Female", "Sexe"] = "Femme"
        df["Statut_marital"] = df["Statut_marital"].replace({"Single": "Célibataire", "Married": "Marié"})

        df.head(3)
        st.dataframe(df.sample(3), use_container_width = True)

    # Code
    with st.expander("Vérifier s'il existe des Doublons dans les enregistrements"):
        st.code("""
        ligne_dupliquee = df[["Date", "ID"]].value_counts()
        ligne_dupliquee = ligne_dupliquee[ligne_dupliquee > 1]
        ligne_dupliquee.sample(3)
        """, language='python')
        ligne_dupliquee = df[["Date", "ID"]].value_counts()
        ligne_dupliquee = ligne_dupliquee[ligne_dupliquee > 1]
        st.dataframe(ligne_dupliquee.sample(3), use_container_width=True)

    # Code
    with st.expander("Afficher une partie des doublons"):
        st.code("""
        doublon = df.duplicated(keep=False)
        df_doublons = df.loc[doublon, :].sort_values(by="ID")
        df_doublons.head(8)
        """, language="python")            
        doublon = df.duplicated(keep=False)
        df_doublons = df.loc[doublon, :].sort_values(by="ID")
        st.dataframe(df_doublons.head(8), use_container_width=True)

    # Code
    with st.expander("Supprimer les doublons"):
        st.code("""
        df = df.drop_duplicates()
        df.head(8)
        """, language="python")            
        df = df.drop_duplicates()
        st.dataframe(df.head(8), use_container_width=True)

    # Code
    with st.expander("Avant traitement : Controler le nombre de valeurs manquantes par colonne"):
        st.code("""
        df.isnull().sum() # ou
        df.isna().sum()  # Calcule le nombre de valeurs manquantes (NaN) pour chaque colonne du dataframe.
        """, language="python")            
        st.dataframe(df.isnull().sum(), use_container_width=True)

    # Code
    with st.expander("Gestion des valeurs manquantes : Supprimer les lignes où figurent des valeurs manquantes dans la colonne 'Statut_employé'"):
        st.code("""
        df.dropna(subset=["Statut_employé"], inplace=True)
        df.head(8)
        """, language="python")
        df.dropna(subset=["Statut_employé"], inplace=True)
        st.dataframe(df.head(8), use_container_width=True)

    # Code
    with st.expander("Gestion des valeurs manquantes : Imputer 'Inconnu' pour toutes les valeurs manquantes de la colonne 'Sexe'"):
        st.code("""
        df["Sexe"] = df["Sexe"].fillna("Inconnu")
        df.head(5)
        """, language="python")
        
        df["Sexe"] = df["Sexe"].fillna("Inconnu")
        st.dataframe(df.head(5), use_container_width=True)

    # Code
    with st.expander("Compter les valeurs de la colonne 'Sexe'"):
        st.code("""
        df.Sexe.value_counts()
        """, language="python")            
        st.dataframe(df.Sexe.value_counts(), use_container_width=True)

    # Code
    with st.expander("Gestion des valeurs manquantes : Imputer la moyenne dans la colonne 'Montant_depensé', la médiane dans la colonne 'Age'"):
        st.code("""
        df["Montant_dépensé"].fillna(df["Montant_dépensé"].mean(), inplace = True)
        df["Age"].fillna(df["Age"].median(), inplace = True)
        df.head(5)
        """, language="python")
        df["Montant_dépensé"].fillna(df["Montant_dépensé"].mean(), inplace = True)
        df["Age"].fillna(df["Age"].median(), inplace = True)
        st.dataframe(df.head(5), use_container_width=True)

    # Code
    with st.expander("Après traitement : Controler le nombre de valeurs manquantes par colonne"):
        st.code("""
        df.isnull().sum()
        """, language="python")            
        st.dataframe(df.isnull().sum(), use_container_width=True)

    # Code
    with st.expander("Convertir le type de chaque colonne afin de le faire correspondre à la réalité"):
        st.code("""
        df["Date"] = pd.to_datetime(df["Date"]).dt.date
        df["Age"] = df["Age"].astype("int64")
        df.dtypes
        """, language="python")            
        
        # Convertir la colonne Date au format datetime et garder seulement la date (sans l'heure)
        df["Date"] = pd.to_datetime(df["Date"]).dt.date
        
        # Convertir la colonne Age en int64
        df["Age"] = df["Age"].astype("int64")
        
        # Afficher les types de données des colonnes
        st.dataframe(df.dtypes, use_container_width=True)

elif sous_menu == "Analyse":
    # Charger le fichier CSV
    df_csv = pd.read_csv("https://raw.githubusercontent.com/simunek-ludovic/streamlit-portfolio/refs/heads/main/csv/online_store_customer_data.csv")
    
    df = df_csv.copy()
    
    df = df.rename(columns={
        "Transaction_date" : "Date",
        "Transaction_ID" : "ID",
        "Gender" : "Sexe",
        "Marital_status" : "Statut_marital",
        "State_names" : "Ville",
        "Employees_status" : "Statut_employé",
        "Segment" : "Abonnement",
        "Payment_method" : "Méthode_paiement",
        "Referal" : "Référence",
        "Amount_spent" : "Montant_dépensé"
        })
    
    df["new_col"] = df["Montant_dépensé"] * 10
    
    df.drop(columns=["Référence", "new_col"], inplace=True)
   
    df.loc[df["Sexe"] == "Male", "Sexe"] = "Homme"
    df.loc[df["Sexe"] == "Female", "Sexe"] = "Femme"
    df["Statut_marital"] = df["Statut_marital"].replace({"Single": "Célibataire", "Married": "Marié"})

    ligne_dupliquee = df[["Date", "ID"]].value_counts()
    ligne_dupliquee = ligne_dupliquee[ligne_dupliquee > 1]

    doublon = df.duplicated(keep=False)
    df_doublons = df.loc[doublon, :].sort_values(by="ID")

    df = df.drop_duplicates()

    df.dropna(subset=["Statut_employé"], inplace=True)
    df["Sexe"] = df["Sexe"].fillna("Inconnu")

    df["Montant_dépensé"].fillna(df["Montant_dépensé"].mean(), inplace = True)
    df["Age"].fillna(df["Age"].median(), inplace = True)
    
    df["Date"] = pd.to_datetime(df["Date"]).dt.date
    df["Age"] = df["Age"].astype("int64")

    # Code
    st.write("Nous allons parcourir quelques exemples de l' **Analyse des données** :")
    # Code
    with st.expander("Calculer les mesures statistiques de base des colonnes numériques"):
        st.code("""
        df.describe()
        """, language="python")            
        st.dataframe(df.describe(), use_container_width=True)

    # Code
    with st.expander("Afficher le nombre de valeur unique dans la colonne 'Statut_employé'"):
        st.code("""
        df["Statut_employé"].nunique()
        """, language="python")            
        st.write("La colonne 'Statut_employé' ne contient que ", df["Statut_employé"].nunique(), "valeurs uniques")

    # Code
    with st.expander("Afficher les valeurs uniques de la colonne 'Statut_employé'"):
        st.code("""
        df["Statut_employé"].unique()
        """, language="python")
        st.write(df["Statut_employé"].unique())

    # Code
    with st.expander("Compter le nombre de valeurs et calculer le pourcentage des valeurs uniques dans la colonne 'Ville'"):
        # Afficher le code
        st.code("""
        Nombre = df["Ville"].value_counts()
        Pourcentage = (df["Ville"].value_counts(normalize=True) * 100).round(2)
        resultat = pd.DataFrame({"Nombre": Nombre, "Pourcentage": Pourcentage})
        """, language="python")
        
        Nombre = df["Ville"].value_counts()
        Pourcentage = (df["Ville"].value_counts(normalize=True) * 100).round(2)
        resultat = pd.DataFrame({'Nombre': Nombre, 'Pourcentage': Pourcentage})
        st.dataframe(resultat, use_container_width=True)

    # Code
    with st.expander("Trier la colonne 'Montant_dépensé' par ordre décroissant et indiquer les 10 meilleurs valeurs"):
        st.code("""
        df.sort_values(by="Montant_dépensé", ascending=False).head(10)
        """, language="python")            
        st.dataframe(df.sort_values(by="Montant_dépensé", ascending=False).head(10), use_container_width=True)

    # Code
    with st.expander("Afficher les lignes où la colonne 'Sexe' est 'Inconnu', avec un 'Abonnement' à 'Gold' et avec un 'Age' supérieur à 30 ans"):
        st.code("""
        sexe_inconnu = df.Sexe == "Inconnu"
        age_superieur_30 = df.Age > 30
        Abonnement = df.Abonnement == "Gold"
        df[sexe_inconnu & age_superieur_30 & Abonnement]
        """, language="python")           
        sexe_inconnu = df.Sexe == "Inconnu"
        age_superieur_30 = df.Age > 30
        Abonnement = df.Abonnement == "Gold"
        st.dataframe(df[sexe_inconnu & age_superieur_30 & Abonnement], use_container_width=True)

    # Code
    with st.expander("Par sexe, rechercher le nombre, la moyenne, et valeur maximale des colonnes 'Age' et 'Montant_dépensé'"):
        st.code("""
        df[["Age","Sexe","Montant_dépensé"]].groupby(["Sexe"]).agg(["count", "mean", "max"])
        """, language="python")           
        st.dataframe(df[["Age","Sexe","Montant_dépensé"]].groupby(["Sexe"]).agg(["count", "mean", "max"]), use_container_width=True)

    # Code
    with st.expander("Regrouper des éléments par colonnes multiples ('Ville', 'Sexe' et 'Méthode_paiement')"):
        st.code("""
        df[["Ville", "Sexe", "Méthode_paiement", "Montant_dépensé"]].groupby(["Ville", "Sexe", "Méthode_paiement"]).agg(["count", "min", "max"])
        """, language="python")           
        st.dataframe(df[["Ville", "Sexe", "Méthode_paiement", "Montant_dépensé"]].groupby(["Ville", "Sexe", "Méthode_paiement"]).agg(["count", "min", "max"]), use_container_width=True)

    # Code
    with st.expander("Créér un tableau Croisé Dynamique (Crosstab) avec les colonnes 'Statut_marital' et 'Méthode_paiement'"):
        st.code("""
        pd.crosstab(df.Statut_marital, df.Méthode_paiement, margins=True, margins_name="Total")
        """, language="python")           
        st.dataframe(pd.crosstab(df.Statut_marital, df.Méthode_paiement, margins=True, margins_name="Total"), use_container_width=True)

elif sous_menu == "Visualisation":
    st.write("Nous allons parcourir quelques exemples de la **Visualisation des données** :")

    # Code
    with st.expander("Afficher un diagramme à barres (Bar plot) sur la répartition des occurrences de la colonne 'Statut_employé'"):
        st.code("""
        df["Statut_employé"].value_counts().plot(kind="barh");
        """, language="python")   
        # Code HTML et CSS pour centrer l'image
        html_code = f"""
        <div style="text-align: center;">
            <img src="https://i72.servimg.com/u/f72/20/11/38/84/barepl10.png" width="600">
        </div>
        """
        st.markdown(html_code, unsafe_allow_html=True)

        # Code
    with st.expander("Afficher un diagramme circulaire (Pie plot) sur la répartition des occurrences de la colonne 'Abonnement'"):
        st.code("""
        df["Segment"].value_counts().plot(kind="pie");
        """, language="python")
        # Code HTML et CSS pour centrer l'image
        html_code = f"""
        <div style="text-align: center;">
            <img src="https://i72.servimg.com/u/f72/20/11/38/84/pieplo10.png" width="600">
        </div>
        """
        st.markdown(html_code, unsafe_allow_html=True)

        # Code
    with st.expander("Afficher un graphique en boite (Box Plot) du 'Montant_dépensé' par 'Statut' ainsi que les valeurs descriptives"):
        st.code("""
        df_col_copy.boxplot(by ="Statut_employé", column =["Montant_dépensé"],ax=ax, grid = False);
        """, language="python")
        # Code HTML et CSS pour centrer l'image
        html_code = f"""
        <div style="text-align: center;">
            <img src="https://i72.servimg.com/u/f72/20/11/38/84/boxplo10.png" width="600">
        </div>
        """
        st.markdown(html_code, unsafe_allow_html=True)
