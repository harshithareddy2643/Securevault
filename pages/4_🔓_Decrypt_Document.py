import streamlit as st
import hashlib
import base64

from cryptography.fernet import Fernet


st.set_page_config(
    page_title="Decrypt Document | SecureVault",
    page_icon="🔓",
    layout="wide"
)


# ============================================================
# PAGE HEADER
# ============================================================

st.title("🔓 Decrypt Document")

st.write(
    "Restore an encrypted document using the same password "
    "that was used during encryption."
)

st.divider()


# ============================================================
# DECRYPTION FUNCTIONS
# ============================================================

def derive_key(password):

    password_hash = hashlib.sha256(
        password.encode()
    ).digest()

    return base64.urlsafe_b64encode(
        password_hash
    )


def decrypt_file(encrypted_data, password):

    key = derive_key(password)

    cipher = Fernet(key)

    return cipher.decrypt(encrypted_data)


# ============================================================
# UPLOAD ENCRYPTED DOCUMENT
# ============================================================

st.subheader("📁 Select Encrypted Document")

encrypted_file = st.file_uploader(
    "Upload an encrypted document",
    type=["encrypted"],
    help="Upload a SecureVault .encrypted file"
)


# ============================================================
# FILE INFORMATION
# ============================================================

if encrypted_file is not None:

    encrypted_bytes = encrypted_file.getvalue()

    st.success(
        f"✅ Encrypted document selected: "
        f"{encrypted_file.name}"
    )

    st.divider()

    st.subheader("📋 Encrypted File Information")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "File Name",
            encrypted_file.name
        )

    with col2:

        st.metric(
            "File Size",
            f"{len(encrypted_bytes) / 1024:.2f} KB"
        )

    st.divider()


    # ========================================================
    # PASSWORD
    # ========================================================

    st.subheader("🔑 Enter Decryption Password")

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter the encryption password"
    )


    # ========================================================
    # DECRYPT
    # ========================================================

    if st.button(
        "🔓 Decrypt Document",
        use_container_width=True
    ):

        if not password:

            st.error(
                "❌ Please enter the decryption password."
            )

        else:

            try:

                decrypted_data = decrypt_file(
                    encrypted_bytes,
                    password
                )

                original_filename = (
                    encrypted_file.name.replace(
                        ".encrypted",
                        ""
                    )
                )

                st.success(
                    "✅ Document decrypted successfully!"
                )

                st.download_button(
                    label="⬇️ Download Decrypted Document",
                    data=decrypted_data,
                    file_name=original_filename,
                    mime="application/octet-stream",
                    use_container_width=True
                )

                st.info(
                    "📄 Your original document has been restored."
                )

            except Exception:

                st.error(
                    "❌ Incorrect password or corrupted "
                    "encrypted file."
                )


# ============================================================
# SECURITY INFORMATION
# ============================================================

st.divider()

st.subheader("🛡️ Security Information")

st.write(
    "The encrypted document can only be restored when "
    "the correct password is provided."
)

st.warning(
    "⚠️ Make sure you enter the same password that was used "
    "when the document was encrypted."
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "SecureVault • Secure Document Decryption"
)