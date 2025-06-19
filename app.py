import streamlit as st
import pyttsx3

st.title("Voice Generator for Mute People")

text = st.text_input("Enter your message:")
emotion = st.selectbox("Choose Emotion", ["Neutral", "Happy", "Sad"])

if st.button("Speak"):
    engine = pyttsx3.init()
    if emotion == "Happy":
        engine.setProperty('rate', 180)
    elif emotion == "Sad":
        engine.setProperty('rate', 100)
    engine.say(text)
    engine.runAndWait()