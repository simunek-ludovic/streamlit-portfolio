# PAGE nlp
import streamlit as st
import re
from collections import Counter
import pandas as pd
import nltk
from nltk.corpus import stopwords
import nltk
nltk.download('movie_reviews')
nltk.download('wordnet')
nltk.download('omw')


from textblob import Word

st.write("""Le NLP ou (Natural Language Processing) est une discipline qui porte essentiellement sur :
- la compréhension,
- la manipulation,
- la génération du langage naturel par les machines.
Ainsi, le NLP est réellement à l’interface entre la science informatique et la linguistique. Il porte donc sur la capacité de la machine à interagir directement avec l’humain.
""")

st.write("Travaillons le NLP sur un texte")
st.write('<p style="color:red;">Nous allons suivre les statistiques des mots "tree" qui est écrit 5 fois et de "trees" qui est écrit 3 fois</p>', unsafe_allow_html=True)

# Texte enregistré dans une variable
texte = """
The Adventure of Timmy and the Magic Forest
Once upon a time, there was a young boy named Timmy. He lived in a small village surrounded by tall trees and colorful flowers. Every day, Timmy would play outside, running through the fields and exploring the woods nearby. He loved nature and always dreamed of having an adventure. One morning, as he walked near the forest, he noticed something unusual. A bright, glowing light seemed to come from deep inside the trees. Curious, Timmy decided to follow the light.
Timmy walked through the forest, carefully stepping over fallen branches and ducking under the thick vines. As he went deeper, he saw strange animals that he had never seen before. Some were big, like the red fox with shiny fur, and others were small, like the green frogs that jumped around. The light led him to a giant tree. The tree was much larger than any tree he had ever seen, and it had a door in its trunk. Timmy felt nervous but excited. He knocked on the door.
To his surprise, the door opened by itself, revealing a friendly-looking woman. She wore a green dress and a crown made of leaves. "Hello, Timmy," she said with a smile. "I have been waiting for you." Timmy was shocked. How did she know his name? "Come in," she invited him. "I have something special to show you."
Timmy stepped inside the tree. It was warm and cozy, and there were shelves filled with books, jars of glowing dust, and sparkling crystals. The woman explained that she was the Guardian of the Magic Forest. "This forest is full of wonders," she said, "but only those who are brave and kind can discover its secrets."
Timmy was amazed. "What kind of secrets?" he asked. The Guardian smiled. "Well, there are many secrets. There are animals that can talk, plants that move, and even flowers that change color depending on your mood. But there is one secret that is the most important. It is a treasure hidden deep in the forest. If you find it, you will have the power to protect the forest forever."
Timmy was thrilled. "I want to find the treasure!" he exclaimed. "But how do I begin?" The Guardian handed him a map and said, "Follow the path of the golden leaves. It will lead you to the treasure, but be careful. There are challenges along the way."
Timmy thanked the Guardian and began his journey. The path was not easy. He climbed hills, crossed rivers, and navigated through dark caves. Along the way, he met different creatures. Some were helpful, like the wise owl who gave him advice, while others, like the mischievous raccoon, tried to trick him.
After a long day of traveling, Timmy found a quiet spot to rest. He lay down on a soft bed of moss and looked up at the stars. He thought about the journey ahead. The next day, he continued on his adventure, feeling more determined than ever to find the treasure and save the forest.
As Timmy walked further into the forest, the golden leaves became brighter and brighter. He was getting closer to the treasure. Suddenly, he heard a rustling sound behind him. He turned around and saw a huge bear standing in his way. "Who goes there?" the bear growled. Timmy was scared, but he remembered the words of the Guardian: "Be brave and kind."
Timmy stepped forward. "I am Timmy, and I am on a quest to find the treasure of the Magic Forest," he said. The bear looked at him for a moment, then nodded. "You are brave, little one," the bear said. "You may pass, but remember, the treasure is not what you expect." With that, the bear moved aside, and Timmy continued on his journey.
Finally, after many more hours of walking, Timmy arrived at a clearing where a large stone chest stood. The golden leaves surrounded it, shining brightly. Timmy opened the chest and found inside a beautiful glowing crystal. As soon as he touched it, a warm light surrounded him, and he felt a sense of peace and strength.
The forest seemed to come alive, as if it were thanking him for finding the treasure. The trees whispered, the flowers danced, and the animals all gathered around him. Timmy knew that he had done something important. He had saved the forest.
Timmy returned to the tree with the Guardian and showed her the crystal. "You have done well, Timmy," she said. "You are now the protector of the Magic Forest." Timmy smiled, knowing that his adventure was just beginning. From that day on, he spent his time exploring the forest, making new friends, and keeping it safe for everyone.
And so, Timmy's life in the Magic Forest was full of joy and adventure. He never stopped learning about the wonders around him, and he knew that as long as he was kind and brave, the forest would always be there to guide him.
"""

# Créer une section rétractable (expander) pour afficher le contenu
with st.expander("Afficher/Cacher le texte analysé"):
    st.write("The Adventure of Timmy and the Magic Forest")
    st.write("Once upon a time, there was a young boy named Timmy. He lived in a small village surrounded by tall ***trees*** and colorful flowers. Every day, Timmy would play outside, running through the fields and exploring the woods nearby. He loved nature and always dreamed of having an adventure. One morning, as he walked near the forest, he noticed something unusual. A bright, glowing light seemed to come from deep inside the ***trees***. Curious, Timmy decided to follow the light.")
    st.write("Timmy walked through the forest, carefully stepping over fallen branches and ducking under the thick vines. As he went deeper, he saw strange animals that he had never seen before. Some were big, like the red fox with shiny fur, and others were small, like the green frogs that jumped around. The light led him to a giant ***tree***. The ***tree*** was much larger than any ***tree*** he had ever seen, and it had a door in its trunk. Timmy felt nervous but excited. He knocked on the door.")
    st.write("To his surprise, the door opened by itself, revealing a friendly-looking woman. She wore a green dress and a crown made of leaves. 'Hello, Timmy,' she said with a smile. 'I have been waiting for you.' Timmy was shocked. How did she know his name? 'Come in,' she invited him. 'I have something special to show you.'")
    st.write("Timmy stepped inside the ***tree***. It was warm and cozy, and there were shelves filled with books, jars of glowing dust, and sparkling crystals. The woman explained that she was the Guardian of the Magic Forest. 'This forest is full of wonders,' she said, 'but only those who are brave and kind can discover its secrets.")
    st.write("Timmy was amazed. 'What kind of secrets?' he asked. The Guardian smiled. 'Well, there are many secrets. There are animals that can talk, plants that move, and even flowers that change color depending on your mood. But there is one secret that is the most important. It is a treasure hidden deep in the forest. If you find it, you will have the power to protect the forest forever.'")
    st.write("Timmy was thrilled. 'I want to find the treasure!' he exclaimed. 'But how do I begin?' The Guardian handed him a map and said, 'Follow the path of the golden leaves. It will lead you to the treasure, but be careful. There are challenges along the way.")
    st.write("Timmy thanked the Guardian and began his journey. The path was not easy. He climbed hills, crossed rivers, and navigated through dark caves. Along the way, he met different creatures. Some were helpful, like the wise owl who gave him advice, while others, like the mischievous raccoon, tried to trick him.")
    st.write("After a long day of traveling, Timmy found a quiet spot to rest. He lay down on a soft bed of moss and looked up at the stars. He thought about the journey ahead. The next day, he continued on his adventure, feeling more determined than ever to find the treasure and save the forest.")
    st.write("As Timmy walked further into the forest, the golden leaves became brighter and brighter. He was getting closer to the treasure. Suddenly, he heard a rustling sound behind him. He turned around and saw a huge bear standing in his way. 'Who goes there?' the bear growled. Timmy was scared, but he remembered the words of the Guardian: 'Be brave and kind.'")
    st.write("Timmy stepped forward. 'I am Timmy, and I am on a quest to find the treasure of the Magic Forest,' he said. The bear looked at him for a moment, then nodded. 'You are brave, little one,' the bear said. 'You may pass, but remember, the treasure is not what you expect.' With that, the bear moved aside, and Timmy continued on his journey.")
    st.write("Finally, after many more hours of walking, Timmy arrived at a clearing where a large stone chest stood. The golden leaves surrounded it, shining brightly. Timmy opened the chest and found inside a beautiful glowing crystal. As soon as he touched it, a warm light surrounded him, and he felt a sense of peace and strength.")
    st.write("The forest seemed to come alive, as if it were thanking him for finding the treasure. The ***trees*** whispered, the flowers danced, and the animals all gathered around him. Timmy knew that he had done something important. He had saved the forest.")
    st.write("Timmy returned to the ***tree*** with the Guardian and showed her the crystal. 'You have done well, Timmy,' she said. 'You are now the protector of the Magic Forest.' Timmy smiled, knowing that his adventure was just beginning. From that day on, he spent his time exploring the forest, making new friends, and keeping it safe for everyone.")
    st.write("And so, Timmy's life in the Magic Forest was full of joy and adventure. He never stopped learning about the wonders around him, and he knew that as long as he was kind and brave, the forest would always be there to guide him.")

# Affichage du nombre de mots dans le texte
st.write("Nombre total de mots (chaque mot est compté autant de fois qu'il apparait) dans le texte :", len(texte.split()))



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

# Découpe le texte en tokens simples avec split()
st.write("### Tokennisation du texte :")
st.write("La tokennisation est le fait de découper le texte en séquence de mot (ou token). Les ", len(texte.split()), "mots dans l'ordre du texte sont :")
tokens = texte.split()

st.code("""
tokens = texte.split()  # Découpe la chaîne "texte" en une liste de mots en utilisant l'espace comme séparateur par défaut.
print(tokens)  # Affiche le contenu de la liste "tokens" dans la console.
""", language='python')

# Créer une section rétractable (expander) pour afficher le contenu
with st.expander("Afficher/Cacher les tokens obtenus (et leur position dans le texte)"):
    st.write(tokens)

# Créer du texte HTML pour justifier et ajouter du contenu Markdown
st.write("On remarque notamment que les mots de fin de phrase sont fusionnés avec le signe de ponctuation. Exemple avec le mot de la position 11 : 'time,' (La virgule reste collée au mot)")

st.write('<p style="color:red;">Suivons nos 2 mots :</p>', unsafe_allow_html=True)
st.write('<ul style="color:red;">'
         '<li>&quot;tree&quot; apparait aux positions : 146 / 148 / 154 / 238 / 740</li>'
         '<li>&quot;trees&quot; apparait aux positions : 28 / 80 / 711</li>'
         '</ul>', unsafe_allow_html=True)

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

# Supprimer tous les signes de ponctuation
texte_nettoye = texte.lower()  # Convertir en minuscule
texte_nettoye = re.sub(r'[^\w\s]', '', texte_nettoye)

# Découper le texte en mots
mots_1 = texte_nettoye.split()
 
# Calculer la fréquence des mots
frequence_mots_1 = Counter(mots_1)

# Trier les mots par fréquence décroissante
mots_tries_1 = frequence_mots_1.most_common()

# Créer un DataFrame pour afficher les résultats dans un tableau
df_1 = pd.DataFrame(mots_tries_1, columns=["Mot", "Fréquence"])

# Affichage des 10 mots les plus fréquents
st.write("### Calculer les fréquences des mots dans le texte :")

# Affichage des mots les plus fréquents dans un DataFrame
st.write("=> Afin de faciliter le traitement, on va supprimer la ponctuation et convertir chaque mot en minuscule.")

st.write("Utilisation de Regex pour faire des traitements sur le texte :")
# code
st.code("""
texte_nettoye = texte.lower()  # Convertir en minuscule
texte_nettoye = re.sub(r'[^\w\s]', ' ', texte_nettoye) # Enlever les signes de ponctuations
""", language='python')

st.code("""
mots_1 = texte_nettoye.split() # Découper le texte en mots
frequence_mots_1 = Counter(mots_1) # Calculer la fréquence des mots
mots_tries_1 = frequence_mots_1.most_common() # Trier les mots par fréquence décroissante
df_1 = pd.DataFrame(mots_tries_1, columns=["Mot", "Fréquence"]) # Créer un DataFrame pour afficher les résultats dans un tableau
df_1
""", language='python')


st.write("Les mots les plus fréquents et leurs occurences :")

st.dataframe(df_1, width=350, height=300)

st.write("=> On remarque que la plupart des mots les plus fréquents ne sont pas significatifs dans le texte.")

st.write("Nombre total de mots uniques (chaque mot est compté 1 seule fois) dans le texte : ", len(df_1), "Pour rappel, le nombre total de mots dans le texte était de ", len(texte.split())) # Affichage du nombre de mots dans le texte

st.write('<p style="color:red;">Suivons nos 2 mots :</p>', unsafe_allow_html=True)
st.write('<ul style="color:red;">'
         '<li>&quot;tree&quot; apparait en 31ème position (numéro 30 de la 1ère colonne) avec une fréquence de 5 fois</li>'
         '<li>&quot;trees&quot; apparait en 45ème position (numéro 44 de la 1ère colonne) avec une fréquence de 3 fois</li>'
         '</ul>', unsafe_allow_html=True)

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

# Affichage du DataFrame avec les mots triés par fréquence
st.write("### Traitement du texte :")
st.write("Afin de régler la problématique des mots non significatifs, nous allons retiré les stopwords.")
st.write("Dans le traitement d'un texte, les stopwords sont des mots qui n'apportement pas de signification importante pour l'analyse, comme les articles, prépositions, et pronoms.")
st.write("*Exemples* : i, me, my, myself, we, our, ours, ourselves, you, your, yours, yourself, yourselves, he, him, his, himself, she, her, hers, herself, it, its, itself, they, them, their, theirs, themselves, what, which, who, whom, this, that, these, those, am, is, are, was, were, be, been, being, have, has, had, having, do, does, did, doing, a, an, the, and, but, if, or, because, as, until, while, of, at, by, for, with, about, against, between, into, through, during, before, after, above, below, to, from, up, down, in, out, on, off, over, under, again, further, then, once, here, there, when, where, why, how, all, any, both, each, few, more, most, other, some, such, no, nor, not, only, own, same, so, than, too, very, s, t, can, will, just, don, should, now, d, ll, m, o, re, ve, y, ain, aren, couldn't, didn't, doesn't, hadn't, hasn't, haven't, isn't, ma, mightn, mustn, needn, shan, shouldn't, wasn, weren't, won, wouldn't, etc...")

# code
st.code("""
nltk.download('stopwords')  # Télécharge le corpus 'stopwords' de la bibliothèque NLTK (qui contient des mots vides en anglais).
stop_words = set(stopwords.words("english"))  # Crée un ensemble ('set') de mots vides (stop words) en anglais à partir du corpus téléchargé.
mots_2 = texte_nettoye.split() # Découper le texte en mots
mots_filtres = [mot for mot in mots_2 if mot.lower() not in stop_words] # Filtrer les mots pour enlever les stopwords
frequence_mots_2 = Counter(mots_filtres) # Calcul de la fréquence des mots après suppression des stopwords
mots_tries_2 = frequence_mots_2.most_common() # Trier les mots par fréquence décroissante
df_2 = pd.DataFrame(mots_tries_2, columns=["Mot", "Fréquence"]) # Créer un DataFrame pour afficher les résultats dans un tableau
df_2 # Afficher le DataFrame
""", language='python')

st.write("Fréquence des mots après suppression des stopwords : ")
# Nettoyage du texte
texte_nettoye = texte.lower()
texte_nettoye = re.sub(r'[^\w\s]', '', texte_nettoye)

# Récupérer les stopwords en anglais depuis NLTK
nltk.download('stopwords')
stop_words = set(stopwords.words("english"))

# Découper le texte en mots
mots_2 = texte_nettoye.split()

# Filtrer les mots pour enlever les stopwords
mots_filtres = [mot for mot in mots_2 if mot.lower() not in stop_words]

# Calcul de la fréquence des mots après suppression des stopwords
frequence_mots_2 = Counter(mots_filtres)

# Trier les mots par fréquence décroissante
mots_tries_2 = frequence_mots_2.most_common()

# Créer un DataFrame pour afficher les résultats dans un tableau
df_2 = pd.DataFrame(mots_tries_2, columns=["Mot", "Fréquence"])

# Afficher le DataFrame dans Streamlit
st.dataframe(df_2, width=350, height=300)

# Affichage du nuage de mots dans Streamlit avec CSS pour centrer l'image
st.write("Nombre total de mots restants après traitement", len(df_2), "Pour rappel, le nombre total de mots uniques était de ", len(df_1))  # Affichage du nombre de mots dans le texte

st.write('<p style="color:red;">Suivons nos 2 mots :</p>', unsafe_allow_html=True)
st.write('<ul style="color:red;">'
         '<li>&quot;tree&quot; apparait en 8ème position (numéro 7 de la 1ère colonne) avec une fréquence de 5 fois</li>'
         '<li>&quot;trees&quot; apparait en 19ème position (numéro 18 de la 1ère colonne) avec une fréquence de 3 fois</li>'
         '</ul>', unsafe_allow_html=True)


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

st.write("### La stemmatisation du texte :")
st.write("La stemmatisation permet de couper des mots pour n'en garder que la racine. Le but est de valoriser ces mots dans un futur algorithme.")
st.write("""Par exemple :
- "marchant", "marché" deviennent "march"
- "manger", "mangeais", "mangé", "mangeons" deviennent "mang"
""")

import nltk
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download('stopwords')
import string

# Tokenisation et conversion en minuscules
tokens = nltk.word_tokenize(texte.lower())

# Nettoyage des caractères indésirables
# On utilise une expression régulière pour remplacer les caractères indésirables par un espace
clean_texte = re.sub(r"[`'’,.\"]", " ", texte)  # Remplace les backticks et apostrophes simples par des espaces

# Découpage en tokens
tokens = clean_texte.split()  # Découpe par espaces

# Filtrage des stop words
filtered_tokens = [
    token for token in tokens
    if token.lower() not in stopwords.words("english")  # Enlève les stop words
]

tokens_clean = []
for words in tokens:
    # On enlève les stopwords et la ponctuation en utilisant string.punctuation
    if words not in nltk.corpus.stopwords.words("english") and words not in string.punctuation :
        tokens_clean.append(words)
tokens_clean

# Importer les bibliothèques nécessaires
from nltk.stem import SnowballStemmer
from nltk.probability import FreqDist

# Initialiser le stemmer pour la langue française
stemmer = SnowballStemmer("english")

# Appliquer le stemming à chaque mot du corpus tokens_clean
tokens_stemmed = [stemmer.stem(word) for word in tokens_clean]

# Créer un objet FreqDist pour compter la fréquence des mots après stemming
freq_dist = FreqDist(tokens_stemmed)

# Afficher les 10 mots les plus fréquents après stemming
print(freq_dist.most_common(10))

mots_tries_stemming = freq_dist.most_common()

# Créer un DataFrame pour afficher la fréquence des mots
df_stemming = pd.DataFrame(mots_tries_stemming, columns=["Mot", "Fréquence"])

# Afficher le DataFrame dans Streamlit
st.dataframe(df_stemming, width=350, height=300)

st.code("""
# Importer les bibliothèques nécessaires
from nltk.stem import SnowballStemmer
from nltk.probability import FreqDist

stemmer = SnowballStemmer("english") # Initialiser le stemmer
tokens_stemmed = [stemmer.stem(word) for word in tokens_clean] # Appliquer le stemming à chaque mot du corpus tokens_clean
freq_dist = FreqDist(tokens_stemmed) # Créer un objet FreqDist pour compter la fréquence des mots après stemming
mots_tries_stemming = freq_dist.most_common() # Trié les mots par frequence
df_stemming = pd.DataFrame(mots_tries_stemming, columns=["Mot", "Fréquence"]) # Créer un DataFrame pour afficher la fréquence des mots
df_stemming # Afficher le DataFrame dans Streamlit
""", language='python')

st.write('<p style="color:red;">Suivons nos 2 mots :</p>', unsafe_allow_html=True)
st.write('<ul style="color:red;">'
         '<li>&quot;tree&quot; apparait en 5ème position (numéro 4 de la 1ère colonne) avec une fréquence de 8 fois</li>'
         '<li>&quot;trees&quot; n&apos;apparait plus car le stemming l&apos;a remis au singulier</li>'
         '</ul>', unsafe_allow_html=True)
st.write("")

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

st.write("### Lemmantisation du texte :")
st.write("La lemmatisation est un processus de traitement du langage naturel (NLP) qui consiste à réduire un mot à sa forme de base ou son lemme. Un lemme est la forme canonique ou de dictionnaire d'un mot.")
st.write("""Par exemple :
- "marchant" et "marché" deviennent "marcher"
- "mangera", "mange" et "mangées" deviennent "manger"
- "meilleure" devient "bon"
""")

# code
st.code("""
mots_3 = texte_nettoye.split() # Découper le texte en mots
mots_sans_stopwords_3 = [mot for mot in mots_3 if mot not in stop_words] # Enlever les stopwords
mots_lemmatizes = [Word(mot).lemmatize() for mot in mots_sans_stopwords_3] # Lemmatisation des mots après suppression des stopwords
frequence_lemmatization = Counter(mots_lemmatizes) # Calcul de la fréquence des mots après lemmatisation
mots_tries_lemmatization = frequence_lemmatization.most_common() # Trier les mots par fréquence décroissante après lemmatisation
df_lemmatization = pd.DataFrame(mots_tries_lemmatization, columns=["Mot", "Fréquence"]) # Créer un DataFrame pour afficher la fréquence des mots
df_lemmatization # Afficher le DataFrame
""", language='python')

st.write("Fréquence des mots après lemmatisation : ")

# Télécharger les ressources nécessaires de nltk
nltk.download("stopwords")

# Nettoyage du texte
texte_nettoye = texte.lower()
texte_nettoye = re.sub(r'[^\w\s]', '', texte_nettoye)

# Récupérer les stopwords en anglais depuis NLTK
stop_words = set(stopwords.words("english"))

# Découper le texte en mots
mots_3 = texte_nettoye.split()

# Enlever les stopwords
mots_sans_stopwords_3 = [mot for mot in mots_3 if mot not in stop_words]

# Lemmatisation des mots après suppression des stopwords
mots_lemmatizes = [Word(mot).lemmatize() for mot in mots_sans_stopwords_3]

# Calcul de la fréquence des mots après lemmatisation
frequence_lemmatization = Counter(mots_lemmatizes)

# Trier les mots par fréquence décroissante après lemmatisation
mots_tries_lemmatization = frequence_lemmatization.most_common()

# Créer un DataFrame pour afficher la fréquence des mots
df_lemmatization = pd.DataFrame(mots_tries_lemmatization, columns=["Mot", "Fréquence"])

# Afficher le DataFrame dans Streamlit
st.dataframe(df_lemmatization, width=350, height=300)

st.write('<p style="color:red;">Suivons nos 2 mots :</p>', unsafe_allow_html=True)
st.write('<ul style="color:red;">'
         '<li>&quot;tree&quot; apparait en 3ème position (numéro 2 de la 1ère colonne) avec une fréquence de 8 fois</li>'
         '<li>&quot;trees&quot; n&apos;apparait plus car la lemmatisation l&apos;a remis au singulier</li>'
         '</ul>', unsafe_allow_html=True)
st.write("")

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

st.write("### Conclusion :")
st.write("Dans le NLP, la tokenisation, la stemmatisation et la lemmatisation sont des étapes fondamentales pour préparer et analyser du texte brut. Chacune joue un rôle spécifique dans le pipeline de prétraitement des données textuelles.")
st.write("La tokenisation est une étape clé pour structurer le texte")
st.write("La stemmatisation est rapide et utile pour des tâches simples où la précision n’est pas critique.")
st.write("La lemmatisation, bien que plus lente, est préférable pour des analyses linguistiques avancées ou des tâches nécessitant une sémantique correcte.")

st.write("Ainsi, le choix entre stemmatisation et lemmatisation dépend de l'équilibre entre performance et précision requis dans le projet NLP")