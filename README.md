# SecureVault – Digital Document Security System

SecureVault is a Python-based document security and question-answering system that combines document processing, RAG (Retrieval-Augmented Generation), local LLMs, and password-based encryption.

## Features

- Upload PDF, TXT, and DOCX documents
- Extract text from documents
- Split documents into chunks
- Generate embeddings using Sentence Transformers
- Store and retrieve document vectors using FAISS
- Ask questions about uploaded documents using RAG
- Generate answers using the local Llama 3.2 model through Ollama
- Encrypt documents using Fernet encryption
- Decrypt encrypted documents using a password

## RAG Workflow

Upload Document  
→ Text Extraction  
→ Text Chunking  
→ Embeddings  
→ FAISS Vector Store  
→ Relevant Chunk Retrieval  
→ Llama 3.2  
→ Answer

## Security Workflow

Document  
→ Password  
→ Key Derivation  
→ Fernet Encryption  
→ `.encrypted` File

The encrypted file can later be decrypted using the correct password.

## Technologies Used

- Python
- Streamlit
- Sentence Transformers
- FAISS
- Ollama
- Llama 3.2
- PyPDF
- python-docx
- Cryptography
- Requests

## Project Structure

```text
SecureVault/
├── app.py
├── utils.py
├── pdf_reader.py
├── rag_engine.py
├── requirements.txt
├── .gitignore
└── pages/
    ├── 1_📤_Upload_&_Process.py
    ├── 2_🤖_Ask_Document.py
    ├── 3_🔒_Encrypt_Document.py
    ├── 4_🔓_Decrypt_Document.py
    └── 5_ℹ️_About.py