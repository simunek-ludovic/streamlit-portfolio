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

st.write("Cinéma")