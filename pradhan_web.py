import streamlit as st
import pandas as pd
from pathlib import Path

# ---------- CONFIG ----------
st.set_page_config(page_title="Pradhan Coaching Institute", layout="wide")

# ---------- CUSTOM CSS ----------
# ---------- IMPROVED FORM STYLING ----------
st.markdown("""
    <style>
        /* Style Streamlit input boxes */
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea,
        .stSelectbox > div > div > select {
            background-color: #ffffff !important;   /* White background */
            color: #000000 !important;              /* Black text */
            font-weight: 500 !important;            /* Medium bold */
            border: 2px solid #2c3e50 !important;   /* Dark border */
            border-radius: 10px !important;
            padding: 8px !important;
        }

        /* Improve placeholder text visibility */
        .stTextInput > div > div > input::placeholder,
        .stTextArea > div > div > textarea::placeholder {
            color: #555555 !important;
            opacity: 1 !important;
        }

        /* Style the select dropdown text */
        .stSelectbox div[data-baseweb="select"] > div {
            color: #000000 !important;
            font-weight: 500 !important;
        }
    </style>
""", unsafe_allow_html=True)


# ---------- HEADER ----------
st.markdown("<div class='title'>Pradhan Coaching Institute</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Empowering Students for a Brighter Future</div>", unsafe_allow_html=True)

# ---------- ABOUT ----------
st.header("📘 About Us")
st.write("""
Welcome to **Shree Coaching Institute**.  
We specialize in academic excellence and competitive exam preparation with expert teachers and personalized mentoring.  
Our mission is to unlock every student's true potential.
""")

# ---------- COURSES ----------
st.header("🎓 Courses Offered")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<div class='course-card'><h3>Mathematics</h3><p>Class 8-12, IIT-JEE Foundation</p></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='course-card'><h3>Science</h3><p>Physics, Chemistry, Biology - NEET & Boards</p></div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='course-card'><h3>English</h3><p>Spoken English, Grammar, Literature</p></div>", unsafe_allow_html=True)

# ---------- REGISTRATION FORM ----------
st.header("📝 Student Registration Form")

name = st.text_input("Full Name")
email = st.text_input("Email Address")
phone = st.text_input("Phone Number")
course = st.selectbox("Select Course", ["Mathematics", "Science", "English"])
message = st.text_area("Additional Message (optional)")

if st.button("Register"):
    if name and email and phone:
        # Save registration to CSV
        file = Path("registrations.csv")
        new_data = pd.DataFrame([[name, email, phone, course, message]],
                                columns=["Name", "Email", "Phone", "Course", "Message"])
        if file.exists():
            old_data = pd.read_csv(file)
            df = pd.concat([old_data, new_data], ignore_index=True)
        else:
            df = new_data
        df.to_csv(file, index=False)
        st.success("✅ Registration submitted successfully! We’ll contact you soon.")
    else:
        st.error("⚠️ Please fill in all required fields (Name, Email, Phone).")

# ---------- CONTACT ----------
st.header("📍 Contact Us")
st.write("""
📌 Address: 123 Main Road, Pune, India  
📞 Phone: +91 98765 43210  
📧 Email: contact@shreecoaching.com  
""")

# ---------- FOOTER ----------
st.markdown("<div class='footer'>© 2025 Shree Coaching Institute | Designed with ❤️ in Streamlit</div>", unsafe_allow_html=True)
