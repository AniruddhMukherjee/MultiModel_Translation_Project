import streamlit as st
from PIL import Image
import pytesseract
import numpy as np
import googletrans
from gtts import gTTS
import os

# Set the Tesseract executable path (may be different in your environment)
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

def image_to_text(image):
    # Convert the image to grayscale
    gray_image = image.convert('L')
    
    # Perform text extraction
    extracted_text = pytesseract.image_to_string(gray_image)
    
    return extracted_text

# Streamlit app

def Translate():
    # File uploader
    st.title("Image to Text")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the image
        image = Image.open(uploaded_file)
    
        # Display the uploaded image
        st.image(image, caption='Uploaded Image', use_column_width=True)
    
        # Convert image to text
        extracted_text = image_to_text(image)
        
        # Display the extracted text
        st.subheader("Extracted Text:")
        st.text(extracted_text)

        # Language selection for translation
        st.subheader("Translate extracted text")
        output_lang = st.selectbox("Select output language:", 
                                list(googletrans.LANGUAGES.values()), 
                                index=list(googletrans.LANGUAGES.values()).index('german'))

        if st.button("Translate"):
            translator = googletrans.Translator()
            output_lang_code = list(googletrans.LANGUAGES.keys())[list(googletrans.LANGUAGES.values()).index(output_lang)]
            
            translation = translator.translate(extracted_text, dest=output_lang_code)
            
            st.subheader(f"Translation to {output_lang}:")
            st.text(translation.text)

            # Generate audio for the translated text
            tts = gTTS(translation.text, lang=output_lang_code)
            tts.save("translation.mp3")
            
            st.audio("translation.mp3")

            # Clean up the audio file
            os.remove("translation.mp3")