import streamlit as st
from PIL import Image

# --- SETTINGS ---
PAGE_TITLE = "Digital CV | Leart Bokshi"
PAGE_ICON = "👋"

NAME = "Leart Bokshi"
DESCRIPTION = "Data Science & Artificial Intelligence student"

EMAIL = "leartbokshi@gmail.com"
LINKEDIN_URL = "https://www.linkedin.com/in/leart-bokshi-228823213/"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- FILES ---
resume_file = "assets/cv.pdf"
profile_pic_file = "assets/profile-pic.png"

with open(resume_file, "rb") as f:
    pdf_bytes = f.read()

profile_pic = Image.open(profile_pic_file)

# --- NAVIGATION ---
page = st.sidebar.radio("Navigate", ["Home", "About"])

# ================= HOME =================
if page == "Home":

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(profile_pic, width=230)

    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)

        st.download_button(
            label="📄 Download CV",
            data=pdf_bytes,
            file_name="Leart_Bokshi_CV.pdf",
            mime="application/pdf",
        )

    # EDUCATION / FOCUS
    st.subheader("Focus Area")
    st.write("""
- 🎓 Data Science & Artificial Intelligence
- 🧠 Machine Learning fundamentals
- 📊 Data analysis & visualization
- 💻 Python programming
""")

    # SKILLS
    st.subheader("Skills")
    st.write("""
- Python (Pandas, NumPy, Scikit-learn basics)
- SQL 
- Data analysis & visualization
- Machine Learning concepts
- HTML, CSS, JavaScript basics
             Power BI, SPSS
""")

    # WORK EXPERIENCE
    st.subheader("Work Experience")
    st.write("---")

    st.write("🏢 **Shtypshkronja Litografia**")
    st.write("04/2023 – Present")
    st.write("""
- Puna në proceset operative dhe organizative
- Menaxhim i detyrave të përditshme të punës
- Koordinim i aktiviteteve në kompani
""")

    # PROJECTS
    st.subheader("Projects")

    st.write("📌 Export–Import Kosovo / Business System (2015 – 2018)")
    st.write("""
- Menaxhim dhe analizë e proceseve të eksport-importit
- Organizim i rrjedhës së punës dhe dokumentacionit
- Bazë për kuptimin e sistemeve biznesore dhe logjistikës
""")

    st.write("📌 Data Science Learning Projects")
    st.write("""
- Data cleaning & preprocessing me Python
- Modele bazike të Machine Learning
- Ushtrime me Pandas, NumPy dhe Scikit-learn
""")

# ================= ABOUT =================
elif page == "About":

    st.title("About Me")

    st.write("""
I am a Data Science & Artificial Intelligence student focused on building strong foundations in machine learning, data analysis, and programming.

I combine practical work experience with continuous learning in modern data technologies.
""")

    st.write(f"📧 {EMAIL}")
    st.write(f"🔗 {LINKEDIN_URL}")