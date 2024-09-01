import streamlit as st
from PIL import Image
import pytesseract
import numpy as np
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import os
#import cv2

# Tesseract configuration
if not os.path.exists('/usr/bin/tesseract'):
    st.warning("Tesseract is not installed. Please install it or adjust the path.")
    pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
else:
    pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

def image_to_text(image):
    # Convert the image to grayscale
    gray_image = image.convert('L')
    
    # Perform text extraction
    extracted_text = pytesseract.image_to_string(gray_image)
    
    return extracted_text

def Translate():
    st.title("Image to Text Translator")

    # Image source selection
    image_source = st.radio("Select image source:", ("Upload Image", "Capture from Camera"))

    image = None

    if image_source == "Upload Image":
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
    else:
        # Camera capture
        camera_image = st.camera_input("Take a picture")
        if camera_image is not None:
            image = Image.open(camera_image)

    if image is not None:
        # Display the image
        st.image(image, caption='Image for Translation', use_column_width=True)
    
        # Convert image to text
        extracted_text = image_to_text(image)
        
        # Display the extracted text
        st.subheader("Extracted Text:")
        st.text(extracted_text)

        # Language selection for translation
        st.subheader("Translate extracted text")
        output_lang = st.selectbox("Select output language:", 
                                list(LANGUAGES.values()), 
                                index=list(LANGUAGES.values()).index('german'))

        if st.button("Translate"):
            translator = Translator()
            output_lang_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(output_lang)]
            
            translation = translator.translate(extracted_text, dest=output_lang_code)
            
            st.subheader(f"Translation to {output_lang}:")
            st.text(translation.text)

            # Generate audio for the translated text
            tts = gTTS(translation.text, lang=output_lang_code)
            tts.save("translation.mp3")
            
            st.audio("translation.mp3")

            # Clean up the audio file
            os.remove("translation.mp3")

if __name__ == "__main__":
    Translate()