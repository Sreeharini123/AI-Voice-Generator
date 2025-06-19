import streamlit as st
from gtts import gTTS
import tempfile

st.set_page_config(page_title="AI Voice Generator", page_icon="🗣️")
st.title("🗣️ AI Voice Generator for Mute Individuals")

text = st.text_input("Enter your message:")
emotion = st.selectbox("Choose Emotion", ["Neutral", "Happy", "Sad"])

if st.button("Speak"):
    if text:
        slow = True if emotion == "Sad" else False
        tts = gTTS(text, lang='en', slow=slow)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            tts.save(fp.name)
            st.audio(fp.name, format="audio/mp3")
    else:
        st.warning("Please enter some text.")
