import streamlit as st
from st_audiorec import st_audiorec
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import os
import speech_recognition as sr
import io

def translate_text():
    st.title("Text Translator with Auto Language Detection")

    # Only select output language
    output_lang = st.selectbox("Select output language:", list(LANGUAGES.values()), index=list(LANGUAGES.values()).index('english'))

    input_text = st.text_area("Enter text to translate (language will be auto-detected):", height=150)
    
    if input_text:
        st.subheader(f"Input text: {input_text}")

    if st.button("Translate"):
        if input_text:
            translator = Translator()
            
            # Detect input language
            detection = translator.detect(input_text)
            detected_lang = LANGUAGES.get(detection.lang, 'Unknown')
            st.write(f"Detected input language: {detected_lang}")

            # Get output language code
            output_lang_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(output_lang)]
            
            # Translate
            translation = translator.translate(input_text, dest=output_lang_code)
            
            st.subheader(f"Translation: {translation.text}")

            # Text-to-speech
            tts = gTTS(translation.text, lang=output_lang_code)
            tts.save("translation.mp3")
            
            st.audio("translation.mp3")

            # Clean up the audio file
            os.remove("translation.mp3")
        else:
            st.warning("Please enter some text to translate.")

if __name__ == '__main__':
    translate_text()