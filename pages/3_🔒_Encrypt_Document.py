import streamlit as st
import hashlib
import base64

from cryptography.fernet import Fernet


st.set_page_config(
    page_title="Encrypt Document | SecureVault",
    page_icon="🔒",
    layout="wide"
)


# ============================================================
# PAGE HEADER
# ============================================================

st.title("🔒 Encrypt Document")

st.write(
    "Protect your document with a password and download "
    "the encrypted file."
)

st.divider()


# ============================================================
# ENCRYPTION FUNCTIONS
# ============================================================

def derive_key(password):

    password_hash = hashlib.sha256(
        password.encode()
    ).digest()

    return base64.urlsafe_b64encode(
        password_hash
    )


def encrypt_file(file_bytes, password):

    key = derive_key(password)

    cipher = Fernet(key)

    encrypted_data = cipher.encrypt(
        file_bytes
    )

    return encrypted_data


# ============================================================
# DOCUMENT UPLOAD
# ============================================================

st.subheader("📄 Select Document")

uploaded_file = st.file_uploader(
    "Choose a document to encrypt",
    type=["pdf", "txt", "docx"],
    help="Supported formats: PDF, TXT and DOCX"
)


# ============================================================
# DOCUMENT INFORMATION
# ============================================================

if uploaded_file is not None:

    file_bytes = uploaded_file.getvalue()

    st.success(
        f"✅ Document selected: {uploaded_file.name}"
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


    # ========================================================
    # PASSWORD
    # ========================================================

    st.subheader("🔑 Set Encryption Password")

    password = st.text_input(
        "Enter a password",
        type="password",
        placeholder="Enter a strong password"
    )

    confirm_password = st.text_input(
        "Confirm password",
        type="password",
        placeholder="Re-enter the password"
    )


    # ========================================================
    # ENCRYPT
    # ========================================================

    if st.button(
        "🔐 Encrypt Document",
        use_container_width=True
    ):

        if not password:

            st.error(
                "❌ Please enter a password."
            )

        elif password != confirm_password:

            st.error(
                "❌ Passwords do not match."
            )

        else:

            try:

                encrypted_data = encrypt_file(
                    file_bytes,
                    password
                )

                encrypted_filename = (
                    uploaded_file.name
                    + ".encrypted"
                )

                st.success(
                    "✅ Document encrypted successfully!"
                )

                st.download_button(
                    label="⬇️ Download Encrypted Document",
                    data=encrypted_data,
                    file_name=encrypted_filename,
                    mime="application/octet-stream",
                    use_container_width=True
                )

                st.info(
                    "🔑 Remember your password. "
                    "You will need the same password to decrypt "
                    "this document."
                )

            except Exception as e:

                st.error(
                    f"❌ Encryption failed: {e}"
                )


# ============================================================
# SECURITY INFORMATION
# ============================================================

st.divider()

st.subheader("🛡️ Security Information")

st.write(
    "SecureVault uses password-derived keys with Fernet "
    "symmetric encryption to protect uploaded documents."
)

st.warning(
    "⚠️ Keep your password safe. If you lose it, the encrypted "
    "document cannot be recovered through SecureVault."
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "SecureVault • Password-Protected Document Encryption"
)