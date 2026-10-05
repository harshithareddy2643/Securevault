import streamlit as st
import requests

from rag_engine import search_documents


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Ask Document - SecureVault",
    page_icon="🤖",
    layout="wide"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    [data-testid="stSidebarNav"] {
        display: none;
    }

    .page-header {
        padding: 20px 0 25px 0;
    }

    .page-header h1 {
        font-size: 40px;
        margin-bottom: 5px;
    }

    .page-header p {
        color: #9da0ad;
        font-size: 17px;
    }

    .answer-box {
        padding: 10px;
        line-height: 1.7;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        """
        <div style="text-align:center; padding:15px 0 20px 0;">
            <h2>🔐 SecureVault</h2>
            <p style="color:#9da0ad;">
                Digital Document Security & Processing
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown("### 🧭 Navigation")

    st.page_link(
        "app.py",
        label="🏠 Home"
    )

    st.page_link(
        "pages/1_📤_Upload_&_Process.py",
        label="📤 Upload & Process"
    )

    st.page_link(
        "pages/2_🤖_Ask_Document.py",
        label="🤖 Ask Document"
    )

    st.page_link(
        "pages/3_🔒_Encrypt_Document.py",
        label="🔒 Encrypt Document"
    )

    st.page_link(
        "pages/4_🔓_Decrypt_Document.py",
        label="🔓 Decrypt Document"
    )

    st.page_link(
        "pages/5_ℹ️_About.py",
        label="ℹ️ About"
    )

    st.markdown("---")

    st.markdown("### ⚙️ System")

    st.markdown("🐍 Python")
    st.markdown("🧠 RAG + FAISS")
    st.markdown("🤖 Llama 3.2")


# =========================================================
# PAGE HEADER
# =========================================================

st.markdown(
    """
    <div class="page-header">
        <h1>🤖 Ask Your Document</h1>
        <p>
            Ask questions about your uploaded document using
            Retrieval-Augmented Generation (RAG).
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# CHECK DOCUMENT
# =========================================================

if "document_text" not in st.session_state:
    st.warning("⚠️ No document has been processed yet.")

    st.info(
        "Please go to **Upload & Process**, upload a document, "
        "and click **Extract & Process Document** first."
    )

    st.stop()


if not st.session_state.document_text:
    st.warning("⚠️ No document text is available.")

    st.info(
        "Please process a document from the **Upload & Process** page."
    )

    st.stop()


if "rag_index" not in st.session_state:
    st.warning("⚠️ Vector store is not ready.")

    st.info(
        "Please process your document again from the "
        "**Upload & Process** page."
    )

    st.stop()


if st.session_state.rag_index is None:
    st.warning("⚠️ Vector store is not ready.")

    st.info(
        "Please process your document again from the "
        "**Upload & Process** page."
    )

    st.stop()


# =========================================================
# DOCUMENT INFORMATION
# =========================================================

st.markdown("## 📄 Current Document")

uploaded_file = st.session_state.get("uploaded_file")

if uploaded_file is not None:
    document_name = uploaded_file.name
else:
    document_name = "Uploaded document"


col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Document",
        document_name
    )

with col2:

    st.metric(
        "Chunks",
        len(st.session_state.get("rag_chunks", []))
    )


# =========================================================
# GENERATE ANSWER USING OLLAMA
# =========================================================

def generate_answer(question, context):

    prompt = f"""
You are a helpful document question-answering assistant.

Answer the question using ONLY the information in the
document context below.

If the answer cannot be found in the context, say:

"I could not find the answer in the document."

Do not make up information.

DOCUMENT CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        },
        timeout=300
    )

    response.raise_for_status()

    result = response.json()

    return result["response"]


# =========================================================
# QUESTION INPUT
# =========================================================

st.markdown("## 💬 Ask a Question")

question = st.text_input(
    "Enter your question:",
    placeholder="Example: What is the main topic of this document?"
)


# =========================================================
# ASK BUTTON
# =========================================================

if st.button(
    "🤖 Ask Document",
    type="primary",
    use_container_width=True
):

    if not question.strip():

        st.warning("⚠️ Please enter a question.")

    else:

        # -------------------------------------------------
        # RETRIEVE RELEVANT CHUNKS
        # -------------------------------------------------

        with st.spinner("🔎 Searching the document..."):

            try:

                relevant_chunks = search_documents(
                    question,
                    st.session_state.rag_chunks,
                    st.session_state.rag_index,
                    top_k=2
                )

            except Exception as e:

                st.error(
                    f"❌ Error while searching the document: {e}"
                )

                st.stop()


        # -------------------------------------------------
        # CHECK SEARCH RESULTS
        # -------------------------------------------------

        if not relevant_chunks:

            st.warning(
                "⚠️ No relevant information was found in the document."
            )

            st.stop()


        # -------------------------------------------------
        # SHOW RETRIEVED INFORMATION
        # -------------------------------------------------

        st.markdown("## 🔎 Relevant Document Sections")

        for i, chunk in enumerate(
            relevant_chunks,
            start=1
        ):

            with st.expander(
                f"Relevant Section {i}"
            ):

                st.write(chunk)


        # -------------------------------------------------
        # PREPARE CONTEXT
        # -------------------------------------------------

        context = "\n\n".join(relevant_chunks)


        # -------------------------------------------------
        # GENERATE ANSWER
        # -------------------------------------------------

        st.markdown("## 🤖 Answer")

        with st.spinner(
            "🧠 Llama 3.2 is generating the answer..."
        ):

            try:

                answer = generate_answer(
                    question,
                    context
                )

                st.success(
                    "✅ Answer generated successfully!"
                )

                st.markdown(
                    f"""
                    <div class="answer-box">
                        {answer}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            except requests.exceptions.Timeout:

                st.error(
                    "⏱️ The request timed out."
                )

                st.info(
                    "Try asking a shorter or more specific question."
                )

            except requests.exceptions.ConnectionError:

                st.error(
                    "❌ Could not connect to Ollama."
                )

                st.info(
                    "Make sure Ollama is running on your Mac."
                )

            except requests.exceptions.RequestException as e:

                st.error(
                    f"❌ Ollama request failed: {e}"
                )

            except Exception as e:

                st.error(
                    f"❌ Unexpected error: {e}"
                )


# =========================================================
# HOW RAG WORKS
# =========================================================

st.markdown("---")

st.markdown("## 🧠 How RAG Works")

with st.container(border=True):

    st.markdown(
        """
        **1. Question**  
        Your question is converted into a search query.

        **2. Retrieval**  
        FAISS finds the most relevant document sections.

        **3. Context**  
        The relevant sections are provided to Llama 3.2.

        **4. Generation**  
        Llama 3.2 generates an answer using the retrieved context.
        """
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div style="
        text-align:center;
        color:#777b89;
        padding:30px 0 10px 0;
        font-size:13px;
    ">
        🔐 SecureVault — Intelligent Document Question Answering
    </div>
    """,
    unsafe_allow_html=True
)