import streamlit as st
from st_audiorec import st_audiorec
import googletrans
from gtts import gTTS
import os
import speech_recognition as sr
import io
import paths.image as image # Import the image.py file

def translate_app():

    input_lang = 'english'
    output_lang = 'gujarati'

    st.sidebar.header("CHOOSE")
    input_method = st.sidebar.radio("Choose input method:", ("Text", "Speech", "Image"))

    st.title("Speech and Text Translator")

    if input_method == "Image":
        image.Translate()  # Call the main function from image.py
        return  # Exit this function to prevent further execution

    if input_method == "Text":
        input_text = st.text_area("Enter text to translate:", height=150)
    else:
        st.write("Record your speech:")
        wav_audio_data = st_audiorec()
        
        if wav_audio_data is not None:
            # Convert audio bytes to text
            r = sr.Recognizer()
            with io.BytesIO(wav_audio_data) as source:
                audio = sr.AudioFile(source)
                try:
                    with audio as source:
                        audio_data = r.record(source)
                    input_lang_code = 'en'  # English
                    input_text = r.recognize_google(audio_data, language=input_lang_code)
                except sr.UnknownValueError:
                    st.error("Speech recognition could not understand the audio. Please try again.")
                    input_text = ""
                except sr.RequestError as e:
                    st.error(f"Could not request results from speech recognition service. Please try again.")
                    input_text = ""
        else:
            input_text = ""

    if input_text:
        st.subheader(f"Input (English): {input_text}")

    if st.button("Translate"):
        if input_text:
            translator = googletrans.Translator()
            input_lang_code = 'en'  # English
            output_lang_code = 'gu'  # Gujarati
            
            translation = translator.translate(input_text, src=input_lang_code, dest=output_lang_code)
            
            st.subheader(f"Translation (Gujarati): {translation.text}")

            tts = gTTS(translation.text, lang=output_lang_code)
            tts.save("translation.mp3")
            
            st.audio("translation.mp3")

            # Clean up the audio file
            os.remove("translation.mp3")
        else:
            st.warning("Please enter some text or record speech to translate.")

if __name__ == '__main__':
    translate_app()