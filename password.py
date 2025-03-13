import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")

# Custom CSS for Styling
st.markdown("""
    <style>
        .stApp {
            background-color: #d5c412;
        }
        
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main">', unsafe_allow_html=True)
st.title("🔐 Password Strength Checker")
st.markdown('''
## 🔒Welcome to the ultimate password strength checker!
Use this simple password strength checker to evaluate your password's strength.
We will give you helpful tips to make your **password stronger**.
''')

password = st.text_input("**Enter your password**", type="password", key="password")

feedback = []
score = 0

if password:
    if len(password) > 8:
        score += 1
    else:
        feedback.append("❌ Password should have at least 8 characters.")

    if re.search("[A-Z]", password) and re.search("[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should have both uppercase and lowercase letters.")
    
    if re.search("[0-9]", password):
        score += 1
    else:
        feedback.append("❌ Password should have at least one number.")

    if re.search("[_@$*!&-/%#]", password):
        score += 1
    else:
        feedback.append("❌ Password should have at least one special character (_@$*!&-/%#).")

    if score == 4:
        st.markdown('<p class="strong">✅ Your password is strong 💪.</p>', unsafe_allow_html=True)
    elif score == 3:
        st.markdown('<p class="medium">🟡 Your password is medium strength. It can be stronger.</p>', unsafe_allow_html=True)
    else:
        st.markdown('<p class="weak">🔴 Your password is weak. Please make it stronger.</p>', unsafe_allow_html=True)

    if feedback:
        st.markdown("## Improvements suggestion")
        for feed in feedback:
            st.write(feed)

st.markdown('</div>', unsafe_allow_html=True)
