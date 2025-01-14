# Titre de la page
st.header("Git / Github")

st.write("Git est un logiciel open-source qui permet de gérer les différentes versions d’un projet (code, documents, etc...).")
st.write("GitHub est une plateforme en ligne qui permet de stocker et de partager des projets Git.")

# Code
with st.expander("Initialiser le dépot Git"):
    st.code("""
    git init
    """, language="bash")


