# IMPORTS
import streamlit as st
import youtube_dl as yt

# Summarizing Methods supported
current_method = ["TF-IDF", "Frequency", "Gensim"]

# UI ELEMENTS
st.write("# Youtube Summarizer")
## Text input
url = st.text_input("Enter a valid URL")
## Method of summary
method = st.selectbox("Select the Summarizer method", current_method)
## Fraction
fraction = st.slider(
    "Fraction of Caption Needed as Summary", min_value=0.1, max_value=1.0, value=0.3
)
