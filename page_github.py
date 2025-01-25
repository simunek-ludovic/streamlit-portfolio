# PAGE github
# Titre de la page
st.header("Github / Git")

st.write("GitHub est une plateforme en ligne qui permet de stocker et de partager des projets Git. Les fonctionnalités principales de GitHub sont :")
st.write("""
- Hébergement des dépôts : GitHub stocke vos projets Git dans le cloud, accessibles depuis n’importe où.
- Travail collaboratif : Les équipes peuvent travailler ensemble sur des projets en utilisant des outils comme les "pull requests" et les "issues".
- Partage public ou privé : Les projets peuvent être publics (visibles par tout le monde) ou privés (accès restreint).
""")

st.write("")

st.write("Git est un logiciel open-source qui permet de gérer les différentes versions d’un projet (code, documents, etc...). Les fonctionnalités principales de Git sont :")
st.write("""
- Suivi des modifications : Git garde un historique complet de toutes les modifications apportées aux fichiers d’un projet. Chaque modification est enregistrée comme une "version" ou "commit".
- Travail collaboratif : Plusieurs développeurs peuvent travailler sur un même projet sans écraser le travail des autres.
- Branchements (branches) : Permet de créer des "branches" pour travailler sur différentes fonctionnalités ou corrections de bugs en parallèle, sans affecter le projet principal.
""")

st.write("")

st.write("Je travaille sur une copie locale du site web. En ayant tous les fichiers sur mon PC, je peux apporter des changements et les tester en environnement local avant de les publier sur GitHub à l'aide des commandes Git.")

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

st.write("Voici quelques commandes (les principales) à utiliser sur Git.")

# Code
with st.expander("Initialiser le dépot Git"):
    st.code("""
    git init
    """, language="bash")

# Code
with st.expander("Ajoute un fichier spécifique au suivi de version"):
    st.code("""
    git add nom_fichier
    """, language="bash")

# Code
with st.expander("Ajoute tous les fichiers au suivi de version"):
    st.code("""
    git add .
    """, language="bash")

# Code
with st.expander("Enregistrer une modification (commit)"):
    st.code("""
    git commit -m "Message du commit"
    """, language="bash")

# Code
with st.expander("Vérifier l'état du dépôt"):
    st.code("""
    git status
    """, language="bash")

# Code
with st.expander("Afficher l’historique des commits"):
    st.code("""
    git log
    """, language="bash")

# Code
with st.expander("Relier un dépôt local à GitHub"):
    st.code("""
    git remote add origin https://github.com/username/nom_du_depot.git
    """, language="bash")

# Code
with st.expander("Envoyer des modifications vers GitHub"):
    st.code("""
    git push -u origin main
    """, language="bash")

# Code
with st.expander("Récupérer les modifications depuis GitHub"):
    st.code("""
    git pull origin main
    """, language="bash")

# Code
with st.expander("Crée une nouvelle branche pour travailler sur une nouvelle fonctionnalité ou un correctif"):
    st.code("""
    git branch nom_branche
    """, language="bash")

# Code
with st.expander("Changer de branche"):
    st.code("""
    git checkout nom_branche
    """, language="bash")

# Code
with st.expander("Fusionner une branche dans la branche courante"):
    st.code("""
    git merge nom_branche
    """, language="bash")

# Code
with st.expander("Cloner un dépôt existant"):
    st.code("""
    git clone https://github.com/username/nom_du_depot.git
    """, language="bash")

# Code
with st.expander("Supprime un fichier du suivi de version Git"):
    st.code("""
    git rm nom_fichier
    """, language="bash")

# Code
with st.expander("Annuler des modifications"):
    st.code("""
    git checkout -- nom_fichier
    """, language="bash")
