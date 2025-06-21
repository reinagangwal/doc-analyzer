# Basic Document Analyzer

import streamlit as st
import pdfplumber
from docx import Document
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

st.title("📄 Document Analyzer")

uploaded_file = st.file_uploader(
    "Upload your document",
    type=["pdf", "docx", "txt"]
)

if uploaded_file is not None:
    with st.spinner("Extracting text..."):
        raw_text = ""
        file_ext = uploaded_file.name.split('.')[-1].lower()

        try:
            if file_ext == "pdf":
                # Parse PDF
                with pdfplumber.open(uploaded_file) as pdf:
                    raw_text = "".join(page.extract_text() or "" for page in pdf.pages)

            elif file_ext == "docx":
                # Parse DOCX
                doc = Document(uploaded_file)
                raw_text = "\n".join(p.text for p in doc.paragraphs)

            elif file_ext == "txt":
                raw_text = uploaded_file.read().decode("utf-8")

            else:
                st.error(f"Unsupported file type: {file_ext}")

        except Exception as e:
            st.error(f"Could not read file: {e}")

        # Proceed if we have text
        if raw_text:
            st.subheader("📄 Extracted Text (first 500 chars)")
            st.text_area("Preview", raw_text[:500], height=200)

            # Analysis
            words = word_tokenize(raw_text)
            sentences = sent_tokenize(raw_text)
            paragraphs = raw_text.split("\n")

            st.write(f"**Word Count:** {len(words)}")
            st.write(f"**Sentence Count:** {len(sentences)}")
            st.write(f"**Paragraph Count (approx):** {len(paragraphs)}")
            st.write(f"**Character Count:** {len(raw_text)}")
            st.write(f"**Estimated Reading Time (minutes):** {len(words)/200:.2f}")
