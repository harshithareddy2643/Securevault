import streamlit as st

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="SecureVault",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown(
    """
    <style>

    /* Hide Streamlit's automatic page navigation */
    [data-testid="stSidebarNav"] {
        display: none;
    }

    /* Main page */
    .main {
        padding-top: 1rem;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #262733;
    }

    /* Sidebar divider */
    .sidebar-divider {
        height: 1px;
        background-color: #555762;
        margin: 25px 0;
    }

    /* Hero section */
    .hero {
        padding: 25px 10px 35px 10px;
    }

    .hero h1 {
        font-size: 46px;
        margin-bottom: 5px;
    }

    .hero p {
        font-size: 19px;
        color: #9da0ad;
    }

    /* Section headings */
    .section-title {
        font-size: 30px;
        font-weight: 700;
        margin-top: 25px;
        margin-bottom: 20px;
    }

    /* Workflow cards */
    .workflow-card {
        height: 145px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
    }

    .workflow-icon {
        font-size: 40px;
        margin-bottom: 8px;
    }

    .workflow-title {
        font-size: 20px;
        font-weight: 700;
        margin-bottom: 7px;
    }

    .workflow-description {
        font-size: 14px;
        color: #9da0ad;
    }

    /* Technology cards */
    .technology-card {
        height: 75px;
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
        font-size: 17px;
        font-weight: 600;
        padding: 8px;
    }

    /* Info cards */
    .info-card {
        min-height: 150px;
        padding: 10px;
    }

    .info-icon {
        font-size: 35px;
    }

    .info-title {
        font-size: 20px;
        font-weight: 700;
    }

    .info-text {
        color: #9da0ad;
        font-size: 14px;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #777b89;
        padding: 35px 0 10px 0;
        font-size: 13px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

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

    st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)

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

    st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)

    st.markdown("### ⚙️ System")

    st.markdown("🐍 Python")
    st.markdown("🧠 RAG + FAISS")
    st.markdown("🤖 Llama 3.2")

# ---------------------------------------------------------
# HERO SECTION
# ---------------------------------------------------------

st.markdown(
    """
    <div class="hero">
        <h1>🔐 SecureVault</h1>
        <p>
            Secure document processing, intelligent retrieval,
            and password-based document protection.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# WELCOME SECTION
# ---------------------------------------------------------

st.markdown("## 👋 Welcome to SecureVault")

st.write(
    """
    SecureVault is a digital document security and processing system
    that combines document processing, Retrieval-Augmented Generation
    (RAG), local LLM-based question answering, and document encryption.
    """
)

st.write(
    """
    Upload a document, process its contents, ask questions using RAG,
    or securely encrypt and decrypt your documents.
    """
)

# ---------------------------------------------------------
# FEATURE CARDS
# ---------------------------------------------------------

st.markdown("## ✨ Key Features")

feature_columns = st.columns(3)

features = [
    (
        "📄",
        "Document Processing",
        "Upload PDF, TXT, and DOCX files and extract their text."
    ),
    (
        "🤖",
        "RAG Question Answering",
        "Retrieve relevant document sections and generate answers using Llama 3.2."
    ),
    (
        "🔐",
        "Document Security",
        "Protect documents using password-based Fernet encryption."
    )
]

for col, (icon, title, description) in zip(feature_columns, features):

    with col:
        with st.container(border=True):
            st.markdown(
                f"""
                <div class="info-card">
                    <div class="info-icon">{icon}</div>
                    <div class="info-title">{title}</div>
                    <p class="info-text">{description}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

# ---------------------------------------------------------
# RAG PROCESSING WORKFLOW
# ---------------------------------------------------------

st.markdown("## 🧠 RAG Processing Workflow")

rag_steps = [
    ("📤", "Upload", "Upload your document"),
    ("📝", "Extract", "Extract document text"),
    ("✂️", "Chunk", "Split text into chunks"),
    ("🧠", "Embed", "Create text embeddings"),
    ("🔎", "Retrieve", "Find relevant sections"),
    ("🤖", "Answer", "Generate an answer"),
]

# ---------------- ROW 1 ----------------

cols = st.columns(3)

for col, (icon, title, description) in zip(cols, rag_steps[:3]):

    with col:
        with st.container(border=True):
            st.markdown(
                f"""
                <div class="workflow-card">
                    <div class="workflow-icon">{icon}</div>
                    <div class="workflow-title">{title}</div>
                    <div class="workflow-description">
                        {description}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

# ---------------- ROW 2 ----------------

cols = st.columns(3)

for col, (icon, title, description) in zip(cols, rag_steps[3:]):

    with col:
        with st.container(border=True):
            st.markdown(
                f"""
                <div class="workflow-card">
                    <div class="workflow-icon">{icon}</div>
                    <div class="workflow-title">{title}</div>
                    <div class="workflow-description">
                        {description}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

# ---------------------------------------------------------
# SECURITY WORKFLOW
# ---------------------------------------------------------

st.markdown("## 🔐 Security Workflow")

security_steps = [
    ("📄", "Document", "Select a document"),
    ("🔑", "Password", "Enter a password"),
    ("🔒", "Encrypt", "Secure the document"),
    ("🔓", "Decrypt", "Restore the document"),
]

cols = st.columns(4)

for col, (icon, title, description) in zip(cols, security_steps):

    with col:
        with st.container(border=True):
            st.markdown(
                f"""
                <div class="workflow-card">
                    <div class="workflow-icon">{icon}</div>
                    <div class="workflow-title">{title}</div>
                    <div class="workflow-description">
                        {description}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

# ---------------------------------------------------------
# TECHNOLOGIES USED
# ---------------------------------------------------------

st.markdown("## 🛠️ Technologies Used")

technologies = [
    ("🐍", "Python"),
    ("📍", "Streamlit"),
    ("🔎", "FAISS"),
    ("🧠", "Sentence Transformers"),
    ("🤖", "Llama 3.2"),
]

cols = st.columns(5)

for col, (icon, name) in zip(cols, technologies):

    with col:
        with st.container(border=True):
            st.markdown(
                f"""
                <div class="technology-card">
                    {icon}&nbsp;&nbsp;{name}
                </div>
                """,
                unsafe_allow_html=True
            )

# ---------------------------------------------------------
# HOW SECUREVAULT WORKS
# ---------------------------------------------------------

st.markdown("## 🚀 How SecureVault Works")

st.write(
    """
    SecureVault follows two main processing pipelines:
    """
)

workflow_columns = st.columns(2)

with workflow_columns[0]:

    with st.container(border=True):

        st.markdown("### 🧠 Intelligent Document Processing")

        st.markdown(
            """
            **1. Upload** → Select a document

            **2. Extract** → Extract the document text

            **3. Chunk** → Divide text into smaller sections

            **4. Embed** → Convert text into vector embeddings

            **5. Retrieve** → Find the most relevant sections

            **6. Answer** → Generate an answer using Llama 3.2
            """
        )

with workflow_columns[1]:

    with st.container(border=True):

        st.markdown("### 🔐 Document Security")

        st.markdown(
            """
            **1. Select** → Choose a document

            **2. Password** → Enter a password

            **3. Encrypt** → Protect the document

            **4. Download** → Save the encrypted file

            **5. Decrypt** → Restore the original document
            """
        )

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown(
    """
    <div class="footer">
        🔐 SecureVault — Digital Document Security & Processing
        <br>
        Built with Python, Streamlit, RAG, FAISS and Llama 3.2
    </div>
    """,
    unsafe_allow_html=True
)