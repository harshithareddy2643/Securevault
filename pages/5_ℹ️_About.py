import streamlit as st

st.set_page_config(
    page_title="About | SecureVault",
    page_icon="ℹ️",
    layout="wide"
)

# ============================================================
# HEADER
# ============================================================

st.title("ℹ️ About SecureVault")

st.write(
    "Learn about the purpose, architecture, technologies and "
    "workflow behind SecureVault."
)

st.divider()


# ============================================================
# PROJECT OVERVIEW
# ============================================================

st.header("🔐 Project Overview")

st.write(
    "SecureVault is a digital document security and intelligent "
    "document processing system. It allows users to upload documents, "
    "extract their content, securely encrypt and decrypt files, and "
    "ask questions about processed documents using a Retrieval-Augmented "
    "Generation (RAG) pipeline."
)


# ============================================================
# OBJECTIVE
# ============================================================

st.header("🎯 Project Objective")

st.write(
    "The main objective of SecureVault is to combine document security "
    "with intelligent document understanding in a single application."
)

st.markdown("""
- 📄 Process PDF, TXT and DOCX documents
- 🔎 Retrieve relevant information from documents
- 🤖 Generate answers using a local Llama 3.2 model
- 🔒 Protect documents using password-based encryption
- 🔓 Restore encrypted documents using the correct password
""")


# ============================================================
# RAG ARCHITECTURE
# ============================================================

st.header("🧠 RAG Architecture")

st.write(
    "SecureVault uses Retrieval-Augmented Generation to answer "
    "questions based on the uploaded document."
)

steps = [
    ("1️⃣", "Document Upload",
     "The user uploads a PDF, TXT or DOCX document."),

    ("2️⃣", "Text Extraction",
     "The application extracts readable text from the document."),

    ("3️⃣", "Chunking",
     "The extracted text is divided into smaller document chunks."),

    ("4️⃣", "Embeddings",
     "Sentence Transformers converts the chunks into vector embeddings."),

    ("5️⃣", "FAISS Retrieval",
     "FAISS searches for the document chunks most relevant to the question."),

    ("6️⃣", "Llama 3.2",
     "The retrieved context is provided to Llama 3.2 to generate the answer.")
]

for icon, title, description in steps:

    with st.container(border=True):

        col1, col2 = st.columns([1, 5])

        with col1:
            st.markdown(f"## {icon}")

        with col2:
            st.subheader(title)
            st.write(description)


# ============================================================
# SECURITY ARCHITECTURE
# ============================================================

st.header("🔒 Document Security")

st.write(
    "SecureVault uses password-based symmetric encryption to protect "
    "documents."
)

security_steps = [
    ("📄", "Select Document",
     "Choose a PDF, TXT or DOCX file."),

    ("🔑", "Enter Password",
     "Provide a password for the document."),

    ("🔒", "Fernet Encryption",
     "The document is encrypted using a Fernet key derived from the password."),

    ("📦", "Encrypted File",
     "The encrypted document is saved with the .encrypted extension."),

    ("🔓", "Decryption",
     "The original document can be restored using the correct password.")
]

for icon, title, description in security_steps:

    with st.container(border=True):

        st.subheader(f"{icon} {title}")

        st.write(description)


# ============================================================
# TECHNOLOGIES
# ============================================================

st.header("🛠️ Technologies Used")

tech1, tech2, tech3 = st.columns(3)

with tech1:

    st.subheader("🐍 Python")

    st.write(
        "Core programming language used to build SecureVault."
    )

with tech2:

    st.subheader("🎈 Streamlit")

    st.write(
        "Used to create the interactive web application interface."
    )

with tech3:

    st.subheader("📄 PyPDF / python-docx")

    st.write(
        "Used for extracting content from supported document formats."
    )


tech4, tech5, tech6 = st.columns(3)

with tech4:

    st.subheader("🧠 Sentence Transformers")

    st.write(
        "Used to generate vector embeddings for document chunks."
    )

with tech5:

    st.subheader("🔎 FAISS")

    st.write(
        "Used for similarity-based retrieval of relevant document chunks."
    )

with tech6:

    st.subheader("🤖 Llama 3.2 + Ollama")

    st.write(
        "Used for local document question answering."
    )


# ============================================================
# PROJECT WORKFLOW
# ============================================================

st.header("🚀 Complete SecureVault Workflow")

workflow = [
    "📤 Upload Document",
    "📝 Extract Text",
    "✂️ Create Chunks",
    "🧠 Generate Embeddings",
    "🔎 Retrieve Relevant Information",
    "🤖 Generate Answer",
    "🔒 Encrypt / 🔓 Decrypt Documents"
]

for item in workflow:

    st.markdown(f"### {item}")


# ============================================================
# SECURITY NOTE
# ============================================================

st.header("🛡️ Security Note")

st.warning(
    "Keep your document passwords safe. SecureVault requires the "
    "correct password to decrypt an encrypted document."
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "SecureVault • Digital Document Security & Processing System"
)