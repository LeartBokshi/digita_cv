import streamlit as st
from PIL import Image
import os

# ================= SETTINGS =================
PAGE_TITLE = "Digital CV | Leart Bokshi"
PAGE_ICON = "👋"

NAME = "Leart Bokshi"
DESCRIPTION = "Data Science & Artificial Intelligence student"

EMAIL = "leartbokshi@gmail.com"
LINKEDIN_URL = "https://www.linkedin.com/in/leart-bokshi-228823213/"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# ================= FILE PATHS =================
PROFILE_PIC_PATH = os.path.join("assets", "profile-pic.png")

# ================= LOAD IMAGE =================
try:
    profile_pic = Image.open(PROFILE_PIC_PATH)
except FileNotFoundError:
    profile_pic = None

# ================= SIDEBAR NAVIGATION =================
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About"])

# ================= HOME PAGE =================
if page == "Home":

    col1, col2 = st.columns([1, 2])

    with col1:
        if profile_pic:
            st.image(profile_pic, width=230)
        else:
            st.info("📷 Add profile image in assets folder")

    with col2:
        st.title(NAME)
        st.subheader(DESCRIPTION)

        st.write(f"📧 {EMAIL}")
        st.write(f"🔗 {LINKEDIN_URL}")

    st.markdown("---")

    # ================= FOCUS =================
    st.subheader("🎯 Focus Area")
    st.write("""
- Data Science & Artificial Intelligence  
- Machine Learning  
- Data Analysis & Visualization  
- Python Programming  
""")

    st.markdown("---")

    # ================= SKILLS =================
    st.subheader("🛠 Skills")
    st.write("""
- Python (Pandas, NumPy, Scikit-learn basics)  
- SQL fundamentals  
- Excel (Pivot tables, formulas, analysis)  
- Machine Learning basics  
- Data Visualization (Matplotlib / Seaborn)  
- HTML, CSS, JavaScript basics  
""")

    st.markdown("---")

    # ================= EXPERIENCE =================
    st.subheader("💼 Work Experience")

    st.write("🏢 **Shtypshkronja Litografia**")
    st.write("04/2023 – Present")

    st.write("""
- Organizim i proceseve të punës  
- Menaxhim i detyrave ditore  
- Koordinim i aktiviteteve operative  
""")

    st.markdown("---")

    # ================= PROJECTS =================
    st.subheader("📂 Projects")

    st.write("📊 **Export & Import Analysis of Kosovo (2018–2025)**")
    st.write("""
- Pastrim dhe analizë e dataset-it me Python  
- Vizualizim i trendeve ekonomike  
- Insights nga të dhënat reale  
""")

    st.write("🤖 **Data Science Learning Projects**")
    st.write("""
- Data cleaning & preprocessing  
- Machine Learning basics  
- Ushtrime me Pandas & NumPy  
""")

# ================= ABOUT PAGE =================
elif page == "About":

    st.title("About Me")

    st.write("""
I am a Data Science & Artificial Intelligence student in the final stage of my studies.

I am passionate about machine learning, data analysis, and building real-world projects using Python.

My goal is to become a professional Data Scientist / AI Engineer and work on impactful data-driven solutions.
""")