import streamlit as st
from st_audiorec import st_audiorec
import googletrans
from gtts import gTTS
import os
import speech_recognition as sr
import io

def translate_speech():
    st.title("Speech Translator")

    input_lang = st.selectbox("Select input language:", list(googletrans.LANGUAGES.values()), index=list(googletrans.LANGUAGES.values()).index('english'))
    output_lang = st.selectbox("Select output language:", list(googletrans.LANGUAGES.values()), index=list(googletrans.LANGUAGES.values()).index('german'))
    
    st.subheader("Record your speech:")
    wav_audio_data = st_audiorec()
        
    if wav_audio_data is not None:
        # Convert audio bytes to text
        r = sr.Recognizer()
        with io.BytesIO(wav_audio_data) as source:
            audio = sr.AudioFile(source)
            try:
                with audio as source:
                    audio_data = r.record(source)
                input_lang_code = list(googletrans.LANGUAGES.keys())[list(googletrans.LANGUAGES.values()).index(input_lang)]
                input_text = r.recognize_google(audio_data, language=input_lang_code)
                st.success("Speech recognized successfully!")
                st.subheader(f"Text in {input_lang} : {input_text}")
            except sr.UnknownValueError:
                st.error("Speech recognition could not understand the audio. Please try again.")
                input_text = ""
            except sr.RequestError as e:
                st.error(f"Could not request results from speech recognition service. Please try again.")
                input_text = ""
    else:
        input_text = ""


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
    translate_speech()