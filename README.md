# OCR and Document Search Web Application

This repository contains a web-based Optical Character Recognition (OCR) and document search application that supports both **Hindi** and **English** text. The application is built using **Streamlit** and leverages the **GOT-OCR 2.0** model for advanced text extraction, along with **Tesseract OCR** for more conventional image processing.

## Key Features

- Multi-language OCR (English & Hindi) using **GOT-OCR 2.0** and **Tesseract**.
- Simple, intuitive web interface built with **Streamlit**.
- Supports GPU acceleration for faster processing using **PyTorch**.
- Deployed via **Streamlit Sharing** for easy accessibility.

---

## Demo

You can check out the live demo of the application here: [Live Demo](https://gotocr.streamlit.app/)

---

## Prerequisites

Before you begin, make sure you have the following:

- **Python 3.9+** installed.
- **Tesseract-OCR** installed on your system (required for Tesseract OCR integration). You can find the installation instructions [here](https://github.com/tesseract-ocr/tesseract#installing-tesseract).
- **CUDA**-enabled GPU (optional, but recommended for faster OCR processing).

---

## Setup Instructions

Follow these steps to set up the project on your local machine:

### 1. Clone the Repository

First, clone the GitHub repository to your local system:

```bash
git clone (https://github.com/aliarmaghan/GOT_-OCR-and-Document-Search-Web-Application-Prototype.git)
cd your-repo-name
```
### 2.Install Tesseract-OCR

Ensure Tesseract-OCR is installed. You can verify by running:

```bash
tesseract --version
```
If not installed, refer to the official Tesseract installation guide for your specific operating system.

### 3. Set Up a Python Virtual Environment
It's a good practice to use a virtual environment to manage dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```
### 4. Install Python Dependencies
Install the required packages specified in requirements.txt:

```bash
pip install -r requirements.txt
```
These packages include:

- PyTorch and Transformers for model processing.
- Streamlit for the web app interface.
- Pytesseract for Tesseract OCR integration.

### Running the Web Application Locally
Once the environment is set up, follow these steps to run the web application:

## 1. Start the Streamlit App:

Run the following command to launch the app:
```bash
streamlit run app.py
```

## 2. Open the Web Interface:

Once the app starts, it will open in your default browser at http://localhost:8501. The app allows you to upload an image (in formats like PNG or JPEG) for OCR.

## 3. Upload an Image:

You can upload images of documents or screenshots. The app will extract text from the image using both GOT-OCR 2.0 and Tesseract.

## 4. View Extracted Text:

The extracted text from the image will be displayed in the interface. You can choose between Hindi or English text processing based on the input language.

# File Overview
- `app.py:` The main script that runs the Streamlit app. It allows users to upload an image and extract text using GOT-OCR 2.0 and Tesseract.

- `requirements.txt:` Lists all the Python packages required to run the application, including PyTorch, Transformers, and Streamlit.

- `load_got_model():` Loads the GOT-OCR 2.0 model from Hugging Face.

- `extract_text_with_got():` Extracts text from images using the GOT-OCR model.
