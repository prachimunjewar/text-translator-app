import streamlit as st
from deep_translator import GoogleTranslator

# Get all supported languages
languages_dict = GoogleTranslator().get_supported_languages(as_dict=True)

# Reverse dictionary (same as your old logic)
language_options = {v: k for k, v in languages_dict.items()}
language_names = list(language_options.keys())

st.title('Language Translator')

source_text = st.text_input('Enter the text to translate')
target_language = st.selectbox('Select Your Language', options=language_names)

translate = st.button('Translate')

if translate:
    if source_text.strip() == "":
        st.warning("Please enter text")
    else:
        try:
            target_language_code = language_options[target_language]

            translated = GoogleTranslator(
                source='auto',
                target=target_language_code
            ).translate(source_text)

            st.write(translated)

        except Exception as e:
            st.error("Translation failed")







# https://www.kaggle.com/code/shehriaralikhan/sentimantal-analysis-via-naive-bayes-models
