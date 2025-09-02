import streamlit as st
import pandas as pd
from pathlib import Path

# ---------- CONFIG ----------
st.set_page_config(page_title="Pradhan Coaching Institute", layout="wide")

# ---------- CUSTOM CSS ----------
st.markdown("""
    <style>
        body {
            background-color: #f8f9fa;
            font-family: 'Segoe UI', sans-serif;
        }
        .title {
            font-size: 50px;
            text-align: center;
            color: #2c3e50;
            margin-bottom: 10px;
        }
        .subtitle {
            font-size: 20px;
            text-align: center;
            color: #7f8c8d;
            margin-bottom: 30px;
        }
        .course-card {
            background: white;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            margin: 10px;
        }
        .footer {
            text-align: center;
            margin-top: 50px;
            font-size: 14px;
            color: gray;
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
