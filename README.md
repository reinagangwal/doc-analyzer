Document Analyzer (Streamlit App)


Overview :

Document Analyzer is a simple and interactive web application built with Streamlit that lets you:

~ Upload documents (.pdf, .docx, or .txt)
~ Extract all text content
~ Get basic statistics:
~ Word count
~ Sentence count
~ Paragraph count
~ Character count
~ Estimated reading time
~ Preview the extracted text for a quick overview

Features
~ Support for PDFs (using pdfplumber)
~ Support for DOCX files (using python-docx)
~ Support for plain text files (.txt)
~ Tokenization with NLTK (punkt and punkt_tab)
~ Interactive interface powered by Streamlit
~ Automatically calculates reading time (~200 wpm)