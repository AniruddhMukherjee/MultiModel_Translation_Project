import streamlit as st
from st_audiorec import st_audiorec
import googletrans
from gtts import gTTS
import os
import speech_recognition as sr
import io

def translate_text():
    st.title("Text Translator")

    input_lang = st.selectbox("Select input language:", list(googletrans.LANGUAGES.values()), index=list(googletrans.LANGUAGES.values()).index('english'))
    output_lang = st.selectbox("Select output language:", list(googletrans.LANGUAGES.values()), index=list(googletrans.LANGUAGES.values()).index('german'))

    input_text = st.text_area("Enter text to translate:", height=150)
    
    if input_text:
        st.subheader(f"input : {input_text}")

    if st.button("Translate"):
        if input_text:
            translator = googletrans.Translator()
            input_lang_code = list(googletrans.LANGUAGES.keys())[list(googletrans.LANGUAGES.values()).index(input_lang)]
            output_lang_code = list(googletrans.LANGUAGES.keys())[list(googletrans.LANGUAGES.values()).index(output_lang)]
            
            translation = translator.translate(input_text, src=input_lang_code, dest=output_lang_code)
            
            st.subheader(f"Translation: {translation.text}")

            tts = gTTS(translation.text, lang=output_lang_code)
            tts.save("translation.mp3")
            
            st.audio("translation.mp3")

            # Clean up the audio file
            os.remove("translation.mp3")
        else:
            st.warning("Please enter some text or record speech to translate.")

if __name__ == '__main__':
    translate_text()