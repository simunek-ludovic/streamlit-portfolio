# PAGE RECOMMANDATION DE FILMS
# Contenu en fonction du choix dans le sous-menu
if sous_menu == "Présentation":
    st.write("### Présentation")

    st.write("« Netflix est un service de diffusion en streaming qui permet à ses membres de regarder une grande variété de séries TV, films, documentaires, etc. sur des milliers d’appareils connectés à Internet.» Créé en 1998, Netflix pèse aujourd’hui plus de 20 milliards de dollars de chiffre d’affaires et consomme 12,6% de la bande passante Internet mondiale. Lorsqu’on accède au service Netflix, le système de recommandations aide l’utilisateur à trouver aussi facilement que possible les séries TV ou films qu’il pourrait apprécier, grâce à un système de recommandation. Netflix calcule ainsi la probabilité que l’utilisateur regarde un titre donné du catalogue de Netflix, et peut ainsi optimiser ces partenariats ou plus globalement sa stratégie marketing. Netflix est l’archétype de la société data-driven. Votre client n’est pas Netflix, mais il a de grandes ambitions !")

    st.write("### Objectif & Enjeux :")
    st.write("Vous êtes un Data Analyst freelance. Un cinéma en perte de vitesse vous contacte. Il a décidé de passer le cap du digital en créant un site Internet taillé pour les locaux. Pour aller encore plus loin, il vous demande de créer un moteur de recommandations de films qui à terme, enverra des notifications aux clients via Internet. Pour l’instant, aucun client n’a renseigné ses préférences, vous êtes dans une situation de cold start. Mais heureusement, le client vous donne une base de données de films basée sur la plateforme IMDb.")
    st.write("Après cette étape, vous utiliserez des algorithmes de machine learning pour recommander des films en fonction de films qui ont été appréciés par le spectateur. Le client vous fournit également une base de données complémentaires venant de TMDB, contenant des données sur les pays des boîtes de production, le budget, les recettes et également un chemin vers les posters des films. Il vous est demandé de récupérer les images des films pour les afficher dans votre interface de recommandation. Attention ! L’objectif n’est pas de diffuser dans le cinéma les films recommandés. L’objectif final est d’avoir une application du système de recommandation avec une zone de saisie de nom de film pour l’utilisateur. Cette application sera mise à disposition des clients du cinéma afin de leur proposer un service supplémentaire, en ligne, en plus du cinéma classique.")

    st.write("### Ressources :")
    st.write("Les données sont disponibles sur le site IMDb, réparties en plusieurs tables (films, acteurs, réalisateurs, notes, etc...)")
    st.write("Datasets IMDb : https://datasets.imdbws.com/")
    st.write("Dataset complémentaire TMDB avec possibilité d'utiliser l'API du site")

    st.write("### Missions et Livrables Attendus :")
    st.write("Créer un système de recommandation de film en utilisant des algorithmes de machine learning et faire une démonstration de ces recommandations sur des films proposés en séance par le client.")

    # Affichage d'un lien cliquable vers votre application Streamlit
    st.markdown("Visitez mon système de recommandation de films : https://simunek-ludovic-cinema.streamlit.app/ pour découvrir la finalité de ce projets.")