import streamlit as st
from pathlib import Path
import io

from pypdf import PdfReader

from rag_engine import create_chunks, create_vector_store


st.set_page_config(
    page_title="Upload & Process | SecureVault",
    page_icon="📤",
    layout="wide"
)


# ============================================================
# PAGE HEADER
# ============================================================

st.title("📤 Upload & Process")

st.write(
    "Upload a document and prepare it for intelligent "
    "question answering using the SecureVault RAG pipeline."
)

st.divider()


# ============================================================
# SESSION STATE
# ============================================================

if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None

if "document_text" not in st.session_state:
    st.session_state.document_text = ""

if "rag_chunks" not in st.session_state:
    st.session_state.rag_chunks = []

if "rag_index" not in st.session_state:
    st.session_state.rag_index = None


# ============================================================
# TEXT EXTRACTION FUNCTIONS
# ============================================================

def extract_pdf_text(file_bytes):

    pdf_stream = io.BytesIO(file_bytes)

    reader = PdfReader(pdf_stream)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def extract_text(file_bytes, filename):

    extension = Path(filename).suffix.lower()

    if extension == ".pdf":

        return extract_pdf_text(file_bytes)

    elif extension == ".txt":

        return file_bytes.decode(
            "utf-8",
            errors="ignore"
        )

    elif extension == ".docx":

        try:

            from docx import Document

            document = Document(
                io.BytesIO(file_bytes)
            )

            paragraphs = []

            for paragraph in document.paragraphs:

                if paragraph.text.strip():
                    paragraphs.append(
                        paragraph.text
                    )

            return "\n".join(paragraphs)

        except ImportError:

            st.error(
                "DOCX processing requires python-docx."
            )

            return ""

    return ""


# ============================================================
# UPLOAD DOCUMENT
# ============================================================

st.subheader("📄 Select Your Document")

uploaded_file = st.file_uploader(
    "Upload a PDF, TXT or DOCX file",
    type=["pdf", "txt", "docx"]
)


# ============================================================
# DOCUMENT INFORMATION
# ============================================================

if uploaded_file is not None:

    st.session_state.uploaded_file = uploaded_file

    file_bytes = uploaded_file.getvalue()

    st.success(
        f"✅ Document uploaded: {uploaded_file.name}"
    )

    st.divider()

    st.subheader("📋 Document Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "File Name",
            uploaded_file.name
        )

    with col2:
        st.metric(
            "File Type",
            uploaded_file.type
        )

    with col3:
        st.metric(
            "File Size",
            f"{len(file_bytes) / 1024:.2f} KB"
        )

    st.divider()


# ============================================================
# EXTRACT AND PROCESS
# ============================================================

if uploaded_file is not None:

    if st.button(
        "📖 Extract & Process Document",
        use_container_width=True
    ):

        file_bytes = uploaded_file.getvalue()

        # ----------------------------------------------------
        # TEXT EXTRACTION
        # ----------------------------------------------------

        with st.spinner(
            "📖 Extracting document text..."
        ):

            try:

                extracted_text = extract_text(
                    file_bytes,
                    uploaded_file.name
                )

            except Exception as e:

                st.error(
                    f"❌ Text extraction failed: {e}"
                )

                extracted_text = ""

        # ----------------------------------------------------
        # PROCESS EXTRACTED TEXT
        # ----------------------------------------------------

        if extracted_text.strip():

            st.session_state.document_text = extracted_text

            st.success(
                "✅ Document text extracted successfully!"
            )

            # ------------------------------------------------
            # RAG PROCESSING
            # ------------------------------------------------

            with st.spinner(
                "🧠 Creating document chunks and embeddings..."
            ):

                try:

                    chunks = create_chunks(
                        extracted_text,
                        chunk_size=500
                    )

                    if chunks:

                        index, embeddings = (
                            create_vector_store(chunks)
                        )

                        st.session_state.rag_chunks = chunks

                        st.session_state.rag_index = index

                        st.success(
                            f"✅ Created {len(chunks)} "
                            "document chunks."
                        )

                    else:

                        st.warning(
                            "⚠️ No document chunks were created."
                        )

                except Exception as e:

                    st.error(
                        f"❌ RAG processing failed: {e}"
                    )

        else:

            st.error(
                "❌ Could not extract text from this document."
            )


# ============================================================
# PROCESSING STATUS
# ============================================================

if st.session_state.document_text:

    st.divider()

    st.subheader("📊 Processing Status")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.success("✅ Text Extracted")

    with col2:

        if st.session_state.rag_chunks:

            st.success(
                f"✅ {len(st.session_state.rag_chunks)} Chunks"
            )

        else:

            st.warning("⏳ Chunks Pending")

    with col3:

        if st.session_state.rag_index is not None:

            st.success("✅ Vector Store Ready")

        else:

            st.warning("⏳ Vector Store Pending")


# ============================================================
# EXTRACTED TEXT
# ============================================================

if st.session_state.document_text:

    st.divider()

    st.subheader("📝 Extracted Document Text")

    st.text_area(
        "Document Content",
        st.session_state.document_text,
        height=350
    )


# ============================================================
# RAG INFORMATION
# ============================================================

if st.session_state.rag_chunks:

    st.divider()

    st.subheader("🧠 RAG Information")

    st.write(
        "The document has been divided into chunks and "
        "converted into vector embeddings for similarity search."
    )

    st.info(
        f"🔎 Total document chunks: "
        f"{len(st.session_state.rag_chunks)}"
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "SecureVault • Document Upload & RAG Processing"
)
