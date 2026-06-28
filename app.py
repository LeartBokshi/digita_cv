import streamlit as st
from PIL import Image
import os

# ================= SETTINGS =================
PAGE_TITLE = "Digital CV | Leart Bokshi"
PAGE_ICON = "👋"

NAME = "Leart Bokshi"
DESCRIPTION = "Data Science & Artificial Intelligence Student"

EMAIL = "leartbokshi@gmail.com"
LINKEDIN_URL = "https://www.linkedin.com/in/leart-bokshi-228823213/"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# ================= FILE PATH =================
PROFILE_PIC_PATH = os.path.join("assets", "profile-pic.png")

# ================= LOAD IMAGE =================
try:
    profile_pic = Image.open(PROFILE_PIC_PATH)
except FileNotFoundError:
    profile_pic = None

# ================= SIDEBAR =================
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    ["🏠 Home", "👨‍💻 About", "📂 Projects", "📚 Lessons"]
)

# ===========================================================
# HOME
# ===========================================================
if page == "🏠 Home":

    col1, col2 = st.columns([1, 2])

    with col1:
        if profile_pic:
            st.image(profile_pic, width=230)
        else:
            st.info("Profile image not found.")

    with col2:
        st.title(NAME)
        st.subheader(DESCRIPTION)

        st.write(f"📧 {EMAIL}")
        st.write(f"🔗 {LINKEDIN_URL}")

    st.markdown("---")

    st.subheader("🎯 Focus Area")
    st.write("""
- Data Science & Artificial Intelligence
- Machine Learning
- Data Analysis & Visualization
- Python Programming
""")

    st.markdown("---")

    st.subheader("🛠 Technical Skills")

    st.markdown("""
### Programming Languages
- Python
- Java
- JavaScript

### Data & Analytics
- SQL
- Excel
- Power BI
- SPSS

### Machine Learning
- Data Cleaning
- Data Preprocessing
- Basic Machine Learning Models

### Data Visualization
- Matplotlib
- Seaborn
- Power BI Dashboards

### Web Development
- HTML
- CSS
- React
- FastAPI
""")

    st.markdown("---")

    st.subheader("💼 Work Experience")

    st.write("### Shtypshkronja Litografia")
    st.write("**04/2023 – Present**")

    st.markdown("""
- Organizing daily business processes
- Managing operational tasks
- Coordinating workflow
- Team collaboration
- Problem solving
""")

# ===========================================================
# ABOUT
# ===========================================================
elif page == "👨‍💻 About":

    st.title("About Me")

    st.write("""
I am a final-year Data Science & Artificial Intelligence student passionate about transforming data into meaningful insights.

I enjoy working on data analysis, machine learning, BI dashboards, and software development using Python, SQL, Power BI, React, and FastAPI.

My goal is to build intelligent and data-driven solutions that solve real-world problems.
""")

    st.markdown("---")

    st.subheader("Education")

    st.write("""
**Bachelor in Data Science & Artificial Intelligence**  
University for Business and Technology (UBT)  
Expected Graduation: 2026
""")

    st.markdown("---")

    st.subheader("Career Interests")

    st.markdown("""
- Artificial Intelligence
- Machine Learning
- Data Science
- Data Analytics
- Business Intelligence
- Backend Development
""")

# ===========================================================
# PROJECTS
# ===========================================================
elif page == "📂 Projects":

    st.title("Projects Portfolio")

    st.write("""
Below are two main projects completed during my studies.
""")

    st.markdown("---")

    st.header("📊 Kosovo Export & Import Analysis (2018–2025)")

    st.write("""
This project analyzes Kosovo's export and import trends using official ASK data.
""")

    st.markdown("""
- Data cleaning & preprocessing
- Exploratory Data Analysis (EDA)
- Trend analysis
- Visualization (Matplotlib & Seaborn)
- Power BI dashboard
""")

    st.markdown("---")

    st.header("💊 PharmAI – Pharmacy Management System")

    st.write("""
Full-stack pharmacy management system.
""")

    st.markdown("""
- React frontend
- FastAPI backend
- SQL Server database
- CRUD operations
- Authentication system
""")

# ===========================================================
# LESSONS
# ===========================================================
elif page == "📚 Lessons":

    lesson = st.sidebar.radio(
        "Select Lesson",
        ["Lecture_12"]
    )

    if lesson == "Lecture_12":

        st.title("📚 Lecture 12 - Database Design & Data Warehousing")

        st.write("""
Lecture 12 provided an introduction to the core principles of relational database design and data warehousing. 
In this lecture, we explored how data is structured and managed in relational systems, focusing on how SQL 
relationships define connections between tables and ensure data consistency. We also discussed why proper database 
design is important for avoiding redundancy and maintaining data integrity in large systems.

Additionally, the lecture covered database normalization, which is a key process used to organize data into 
efficient structures by reducing duplication and eliminating anomalies during data operations. We studied the 
first three normal forms (1NF, 2NF, and 3NF) and how they progressively improve database quality and structure.

Another important topic was Slowly Changing Dimensions (SCD), which explains how changes in data over time are 
handled in data warehouses. We learned different SCD types, including Type 1, Type 2, and Type 3, and how each 
approach is used depending on whether historical data needs to be preserved or overwritten.

Finally, we compared Star Schema and Snowflake Schema, two common dimensional modeling techniques used in data 
warehousing. The Star Schema offers a simpler structure with faster query performance, while the Snowflake Schema 
provides better normalization and reduced redundancy but with more complex queries.

Overall, this lecture helped build a strong foundation in database design concepts and data warehouse modeling, 
which are essential for working with modern data-driven systems and Business Intelligence solutions.
""")