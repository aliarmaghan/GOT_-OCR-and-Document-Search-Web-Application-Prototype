import streamlit as st
from PIL import Image
import pytesseract
from langdetect import detect
import os

# Import the GOT OCR model extraction function
from ocr_model import extract_text_with_got


# Function to extract text using GOT (from ocr_model.py)
def extract_text_got(temp_file_path):
    got_extracted_text = extract_text_with_got(temp_file_path)
    return got_extracted_text  # Return directly if it's a string

# Function to extract Hindi text using Tesseract
def extract_text_tesseract(image):
    hindi_text = pytesseract.image_to_string(image, lang='hin')
    return hindi_text

# Function to detect the language of the text
def detect_language(text):
    try:
        return detect(text)
    except:
        return None

# Function to combine results from GOT (English) and Tesseract (Hindi)
def extract_combined_text(image):
    # Step 1: Extract English text using GOT
    english_text = extract_text_got(image)
    
    # Step 2: Detect language of extracted text
    language = detect_language(english_text)
    
    # Step 3: If English detected, extract Hindi using Tesseract as fallback
    if language != 'hi':
        hindi_text = extract_text_tesseract(image)
        combined_text = english_text + "\n" + hindi_text
    else:
        combined_text = english_text
    
    return combined_text

# Web app UI using Streamlit
st.title("Multilingual OCR (English + Hindi) Web App")

uploaded_image = st.file_uploader("Upload an image", type=['png', 'jpg', 'jpeg'])

if uploaded_image is not None:
    # Open the uploaded image
    image = Image.open(uploaded_image)

    # Convert the image to RGB mode if it's not already in RGB
    if image.mode != 'RGB':
        image = image.convert('RGB')

    # Display the uploaded image in the Streamlit app
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Save the uploaded image to a temporary file
    temp_file_path = "temp_image.jpg"  # Temporary file path
    image.save(temp_file_path, format='JPEG')  # Save the image in JPEG format

    #-------------

    # Extract text from the image
    extracted_text = extract_combined_text(temp_file_path)

    # Clean up by removing the temporary file
    os.remove(temp_file_path)
    
    # Display extracted text
    st.subheader("Extracted Text:")
    st.text(extracted_text)
    
    # Keyword search functionality
    search_query = st.text_input("Enter keyword to search:")
    if search_query:
        if search_query.lower() in extracted_text.lower():
            st.write(f"'{search_query}' found in the extracted text!")
        else:
            st.write(f"'{search_query}' not found in the extracted text.")


   