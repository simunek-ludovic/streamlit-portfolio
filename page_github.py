# Titre de la page
st.header("Git / Github")

st.write("Git est un logiciel open-source qui permet de gérer les différentes versions d’un projet (code, documents, etc...).")
st.write("""
- Suivi des modifications : Git garde un historique complet de toutes les modifications apportées aux fichiers d’un projet. Chaque modification est enregistrée comme une "version" ou "commit".
- Travail collaboratif : Plusieurs développeurs peuvent travailler sur un même projet sans écraser le travail des autres.
- Branchements (branches) : Permet de créer des "branches" pour travailler sur différentes fonctionnalités ou corrections de bugs en parallèle, sans affecter le projet principal.
""")


st.write("GitHub est une plateforme en ligne qui permet de stocker et de partager des projets Git.")

# Code
with st.expander("Initialiser le dépot Git"):
    st.code("""
    git init
    """, language="bash")


