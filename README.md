# Multi-Modal Translation App

## Overview
This Streamlit-based application offers translation services using audio, text, and images. It leverages advanced machine learning models and APIs to provide a comprehensive translation experience.

## Features
1. **Image Translation**
   - Upload images or capture from camera
   - Extract text from images using Tesseract OCR
   - Translate extracted text to selected language
   - Text-to-speech output for translated text

2. **Text Translation**
   - Auto-detect input language
   - Translate text to selected language
   - Text-to-speech output for translated text

3. **Speech Translation**
   - Record speech input
   - Convert speech to text
   - Translate text to selected language
   - Text-to-speech output for translated text

## Technologies Used
- Streamlit: For the web application framework
- PyTesseract: For Optical Character Recognition (OCR)
- Google Translate API: For language translation
- gTTS (Google Text-to-Speech): For converting text to speech
- Speech Recognition: For converting speech to text

## Setup and Installation
1. Install required packages:
   ```
   pip install streamlit pillow pytesseract numpy googletrans==3.1.0a0 gTTS speech_recognition st_audiorec
   ```
2. Ensure Tesseract is installed on your system and the path is correctly set.

## Usage
Run the Streamlit app:
```
streamlit run app.py
```

## Note
This application uses a sequence-to-sequence transformer model for translations, providing accurate and context-aware results across different modalities.

## Future Improvements
- Implement more advanced OCR techniques for better image text extraction
- Add support for more languages and dialects
- Improve user interface for a more seamless experience

## The website link:
https://multitranslation.streamlit.app/