import streamlit as st
from deep_translator import GoogleTranslator

# Clean language names for UI
languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Chinese (Simplified)": "zh-cn",
    "Japanese": "ja",
    "Arabic": "ar",
    "Russian": "ru",
    "Portuguese": "pt",
    "Italian": "it",
    "Korean": "ko",
    "Turkish": "tr"
}

st.title('🌐 Language Translator')

# Input
source_text = st.text_input('Enter the text to translate')

# Dropdown with proper names
target_language = st.selectbox('Select Your Language', list(languages.keys()))

# Button
if st.button('Translate'):
    if source_text.strip() == "":
        st.warning("Please enter text")
    else:
        try:
            translated = GoogleTranslator(
                source='auto',
                target=languages[target_language]
            ).translate(source_text)

            st.success("Translated Text:")
            st.write(translated)

        except:
            st.error("Translation failed")







# https://www.kaggle.com/code/shehriaralikhan/sentimantal-analysis-via-naive-bayes-models
