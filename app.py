import streamlit as st
from PIL import Image

# ================= SETTINGS =================
PAGE_TITLE = "Digital CV | Leart Bokshi"
PAGE_ICON = "👋"

NAME = "Leart Bokshi"
DESCRIPTION = "Data Science & Artificial Intelligence student"

EMAIL = "leartbokshi@gmail.com"
LINKEDIN_URL = "https://www.linkedin.com/in/leart-bokshi-228823213/"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# ================= FILES =================
profile_pic_file = "assets/profile-pic.png"
resume_file = "assets/egezon baruti cv.pdf"   # <-- PDF yt real

# Load profile image (safe)
try:
    profile_pic = Image.open(profile_pic_file)
except:
    profile_pic = None

# Load PDF safely
try:
    with open(resume_file, "rb") as f:
        pdf_bytes = f.read()
    pdf_ok = True
except:
    pdf_bytes = None
    pdf_ok = False

# ================= NAVIGATION =================
page = st.sidebar.radio("Navigate", ["Home", "About"])

# ================= HOME =================
if page == "Home":

    col1, col2 = st.columns([1, 2])

    with col1:
        if profile_pic:
            st.image(profile_pic, width=230)
        else:
            st.write("📷 Add profile image in assets")

    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)

        # Download CV button (safe)
        if pdf_ok:
            st.download_button(
                label="📄 Download CV",
                data=pdf_bytes,
                file_name="Leart_Bokshi_CV.pdf",
                mime="application/pdf",
            )
        else:
            st.warning("CV PDF not found in assets folder")

    # ================= FOCUS =================
    st.subheader("Focus Area")
    st.write("""
- 🎓 Data Science & Artificial Intelligence
- 🧠 Machine Learning basics
- 📊 Data analysis & visualization
- 💻 Python programming
""")

    # ================= SKILLS =================
    st.subheader("Skills")
    st.write("""
- Python (Pandas, NumPy, Scikit-learn basics)
- SQL fundamentals
- Machine Learning concepts
- Data visualization
- HTML, CSS, JavaScript basics
""")

    # ================= WORK EXPERIENCE =================
    st.subheader("Work Experience")
    st.write("---")

    st.write("🏢 **Shtypshkronja Litografia**")
    st.write("04/2023 – Present")
    st.write("""
- Puna në procese operative dhe organizative
- Menaxhim i detyrave të përditshme
- Koordinim i aktiviteteve të punës
""")

    # ================= PROJECTS =================
    st.subheader("Projects")

    st.write("📌 Export–Import Business System (Kosovo)")
    st.write("""
- Analizë e proceseve të eksport-importit
- Organizim i dokumentacionit dhe rrjedhës së punës
- Kuptim i sistemeve biznesore dhe logjistikës
""")

    st.write("📌 Data Science Learning Projects")
    st.write("""
- Data cleaning & preprocessing me Python
- Modele bazike të Machine Learning
- Ushtrime me Pandas dhe NumPy
""")

# ================= ABOUT =================
elif page == "About":

    st.title("About Me")

    st.write("""
I am a Data Science & Artificial Intelligence student in the final stage of studies.

I focus on machine learning, data analysis, and building practical projects using Python.
""")

    st.write(f"📧 {EMAIL}")
    st.write(f"🔗 {LINKEDIN_URL}")