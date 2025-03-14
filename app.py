import streamlit as st
from gtts import gTTS
import os

# Streamlit UI
st.title("🗣 Multilingual Text-to-Speech Converter")
st.write("Enter text in your selected language, and I'll generate speech for you!")

# Language selection
languages = {
    "Urdu": "ur",
    "English": "en",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Chinese": "zh"
}

selected_language = st.selectbox("Select Language:", list(languages.keys()))

# User input
text = st.text_area("Enter your text below:", " ")

if st.button("Convert to Speech"):
    if text.strip():
        # Convert text to speech
        lang_code = languages[selected_language]
        tts = gTTS(text=text, lang=lang_code)
        audio_file = "output.mp3"
        tts.save(audio_file)
        
        # Play audio
        st.audio(audio_file, format="audio/mp3")
        
        # Provide download link
        with open(audio_file, "rb") as file:
            st.download_button("Download Audio", file, file_name="speech.mp3", mime="audio/mp3")
    else:
        st.warning("⚠️ Please enter some text before converting.")
