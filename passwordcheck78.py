import re
import streamlit as st

# Page styling
st.set_page_config(page_title="Password Strength Checker By Nazia Siraj", page_icon="🌘", layout="centered")

# Custom CSS
st.markdown("""
<style>
    .main {text-align: center;}
    .stTextInput {width: 60% !important; margin: auto;}
    .stButton button {
        width: 50% !important;
        background-color: blue !important;
        color: white !important;
        font-size: 18px;
    }
    .stButton button:hover {
        background-color: red !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# Page title and description
st.title("🔐 Password Strength Generator")
st.write("Enter your password below to check its security level. 🔍")

# Placeholder for password strength
strength_placeholder = st.empty()

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be **at least 8 characters long**.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **both uppercase (A-Z) and lowercase (a-z) letters**.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one number (0-9)**.")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include **at least one special character (!@#$%^&*)**.")

    # Display password strength results
    if score == 4:
        strength_placeholder.success("✅ **Strong Password** - Your password is secure.")
    elif score == 3:
        strength_placeholder.info("⚠️ **Moderate Password** - Consider improving security by adding more features.")
    else:
        strength_placeholder.error("❌ **Weak Password** - Follow the suggestions below to strengthen it.")

    # Feedback
    if feedback:
        with st.expander("🔍 **Improve Your Password** "):
            for item in feedback:
                st.write(item)

# Password input field
password = st.text_input("Enter your password:", type="password", help="Make sure your password is strong 🔐")

# Button to check password strength
if password:
    check_password_strength(password)
else:
    strength_placeholder.warning("⚠️ Please enter a password first!")  # Show warning if password is empty
