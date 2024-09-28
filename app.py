import streamlit as st
from PIL import Image
import os
from ocr_model import extract_text_with_got  # Import your OCR function

st.title("OCR Web Application (GOT-OCR 2.0)")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Open the uploaded image
    image = Image.open(uploaded_file)

    # Convert the image to RGB mode if it's not already in RGB
    if image.mode != 'RGB':
        image = image.convert('RGB')

    # Display the uploaded image in the Streamlit app
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Save the uploaded image to a temporary file
    temp_file_path = "temp_image.jpg"  # Temporary file path
    image.save(temp_file_path, format='JPEG')  # Save the image in JPEG format

    # Extract text using the GOT-OCR model by passing the file path
    st.write("Extracting text...")
    extracted_text = extract_text_with_got(temp_file_path)  # Pass the file path, not the PIL object

    # Clean up by removing the temporary file
    os.remove(temp_file_path)

    # Display the extracted text
    st.text_area("Extracted Text", value=extracted_text, height=200)

    # Keyword search functionality
    search_term = st.text_input("Search within the text")
    if search_term:
        if search_term.lower() in extracted_text.lower():
            st.write(f"Keyword '{search_term}' found!")
            st.write(extracted_text.replace(search_term, f"**{search_term}**"))
        else:
            st.write(f"Keyword '{search_term}' not found.")
