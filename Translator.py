'''
from googletrans import Translator, LANGUAGES
import streamlit as st

# Get language codes and names from googletrans
language_options = {v: k for k, v in LANGUAGES.items()}
language_names = list(language_options.keys())

st.title('Language Translator')

source_text = st.text_input('Enter the text to translate')
target_language = st.selectbox('Select Your Language', options=language_names)

translate = st.button('Translate')

if translate:
    translator = Translator()
    target_language_code = language_options[target_language]
    out = translator.translate(source_text, dest=target_language_code)
    st.write(out.text)

'''
from googletrans import Translator, LANGUAGES
import streamlit as st

# Get language codes and names from googletrans
language_options = {v: k for k, v in LANGUAGES.items()}
language_names = list(language_options.keys())

st.title('Language Translator')

source_text = st.text_input('Enter the text to translate')
target_language = st.selectbox('Select Your Language', options=language_names)

translate = st.button('Translate')

if translate:
    translator = Translator()
    target_language_code = language_options[target_language]
    out = translator.translate(source_text, dest=target_language_code)
    st.write(out.text)








# https://www.kaggle.com/code/shehriaralikhan/sentimantal-analysis-via-naive-bayes-models