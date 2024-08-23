import streamlit as st
from st_audiorec import st_audiorec
import googletrans
from gtts import gTTS
import os
import speech_recognition as sr
import io
import paths.image as image
import paths.speech as speech
import paths.text as text

def translate_app():

    st.sidebar.header("CHOOSE METHOD:")
    input_method = st.sidebar.radio("Choose input method:", ("Text", "Speech", "Image"))

    if input_method == "Text":
        text.translate_text()

    if input_method == "Speech":
        speech.translate_speech()

    if input_method == "Image":
        image.Translate()


if __name__ == '__main__':
    translate_app()