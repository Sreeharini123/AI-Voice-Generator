import streamlit as st
from gtts import gTTS
import os
import tempfile
from playsound import playsound

st.set_page_config(page_title="AI Voice Generator", page_icon="🗣️")
st.title("🗣️ AI Voice Generator for Mute Individuals")

text = st.text_input("Enter your message:")
language = "en"
emotion = st.selectbox("Choose Emotion", ["Neutral", "Happy", "Sad"])

if st.button("Speak"):
    if text:
        tts = gTTS(text, lang=language)
        temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts.save(temp_audio.name)

        audio_file = open(temp_audio.name, "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')
    else:
        st.warning("Please enter some text.")
