import streamlit as st
import re

st.set_page_config(page_title="Password strength Checker", page_icon="🔐")

st.title(" 🔐Password Strength Checker")
st.markdown("""
## Welcome To The Ultimate PASSWORD STRENGTH CHECKER 👋
use this simple tool to check the strength of your password to get suggestion on how to make it stronger.
            we will give you help tips to create a **Strong Password**🔏""")

password = st.text_input("Enter your password", type="password")

feedback = []

score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌Password should be at least 08 characters long.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌Password should contain at least both uppercase and lowercase letter.")

    if re.search(r'\d', password):
        score += 1
    else :
        feedback.append("❌Password should contain at least one digit.")

    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one special character (!@#$%^&*).")
    if score == 4:
        feedback.append("✅Your Password is Strong!🎉")
    elif score == 3:
        feedback.append("🟡Your Password is Moderately Strong. It could be stroner.")
    else:
        feedback.append("🔴Your Password is Weak. please make it stronger.")

    if feedback:
        st.markdown("## Improvement Suggestions")
        for tip in feedback:
            st.write(tip)
else:
    st.info("Please enter a password to get started.")