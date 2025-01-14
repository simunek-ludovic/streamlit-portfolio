# Titre de la page
st.header("Git / Github")

st.write("Git est un logiciel open-source qui permet de gérer les différentes versions d’un projet (code, documents, etc...). Les fonctionnalités principales de Git sont :")
st.write("""
- Suivi des modifications : Git garde un historique complet de toutes les modifications apportées aux fichiers d’un projet. Chaque modification est enregistrée comme une "version" ou "commit".
- Travail collaboratif : Plusieurs développeurs peuvent travailler sur un même projet sans écraser le travail des autres.
- Branchements (branches) : Permet de créer des "branches" pour travailler sur différentes fonctionnalités ou corrections de bugs en parallèle, sans affecter le projet principal.
""")





# Code
with st.expander("Initialiser le dépot Git"):
    st.code("""
    git init
    """, language="bash")









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

st.write("GitHub est une plateforme en ligne qui permet de stocker et de partager des projets Git. Les fonctionnalités principales de GitHub sont :")
st.write("""
- Hébergement des dépôts : GitHub stocke vos projets Git dans le cloud, accessibles depuis n’importe où.
Travail collaboratif : Les équipes peuvent travailler ensemble sur des projets en utilisant des outils comme les "pull requests" et les "issues".
Partage public ou privé : Les projets peuvent être publics (visibles par tout le monde) ou privés (accès restreint).
""")




