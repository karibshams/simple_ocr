# app.py

import streamlit as st
from extract_text import extract_text

st.set_page_config(page_title="OCR Scraper", layout="centered")

st.title("📄 OCR Scraper")
st.write("Upload any document or image and extract text using OCR and parsing.")

uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx", "txt", "png", "jpg", "jpeg", "bmp", "tiff", "heic"])

if uploaded_file is not None:
    st.info("Extracting text...")
    try:
        text = extract_text(uploaded_file, uploaded_file.name)
        if text:
            st.success("✅ Text extracted successfully!")
            st.text_area("Extracted Text", text, height=400)
        else:
            st.warning("⚠️ No text found or failed to extract text.")
    except Exception as e:
        st.error(f"❌ An error occurred: {e}")
