import streamlit as st
from translator import translate_text

st.set_page_config(page_title="Language Translator", layout="centered")

st.title("🌐 Language Translator")
st.write("Translate text between any two languages using Google Translate.")

text = st.text_area("Enter text to translate:", height=150)
source_lang = st.selectbox("Source Language", ["auto", "en", "fr", "es", "de", "hi", "zh", "ar", "ru"])
target_lang = st.selectbox("Target Language", ["en", "fr", "es", "de", "hi", "zh", "ar", "ru"])

if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some text to translate.")
    else:
        translated = translate_text(text, source_lang, target_lang)
        st.success("Translation:")
        st.write(translated)
        st.text_area("Translated Text", translated, height=150)

st.caption("Built for CodeAlpha AI Internship")
