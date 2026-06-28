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
    ["🏠 Home", "👨‍💻 About", "📂 Projects"]
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
I am a final-year **Data Science & Artificial Intelligence** student passionate about transforming data into meaningful insights.

Throughout my studies, I have worked on projects involving data analysis, machine learning, business intelligence, and full-stack software development.

I enjoy solving real-world problems using modern technologies such as Python, SQL, Power BI, React, and FastAPI.

My long-term goal is to build a successful career as a Data Scientist or AI Engineer by developing intelligent and data-driven solutions.
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
Below are two of the most significant projects I have completed during my studies.
""")

    st.markdown("---")

    # =======================================================

    st.header("📊 Kosovo Export & Import Analysis (2018–2025)")

    st.write("""
This project focuses on analyzing Kosovo's export and import performance between **2018 and 2025** using official data from the **Kosovo Agency of Statistics (ASK)**.
""")

    st.subheader("Project Objectives")

    st.markdown("""
- Analyze yearly export trends
- Analyze yearly import trends
- Compare exports with imports
- Identify economic patterns
- Build interactive dashboards
""")

    st.subheader("Technologies Used")

    st.markdown("""
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Power BI
""")

    st.subheader("Main Tasks")

    st.markdown("""
- Data cleaning
- Data preprocessing
- Exploratory Data Analysis (EDA)
- Trend analysis
- Charts and visualizations
- Dashboard development
""")

    st.subheader("Outcome")

    st.write("""
The project provides valuable insights into Kosovo's international trade by identifying import and export trends over time through interactive dashboards and Python visualizations.
""")

    st.markdown("---")

    # =======================================================

    st.header("💊 PharmAI – Pharmacy Management System")

    st.write("""
PharmAI is a modern full-stack web application developed for managing pharmacy operations efficiently.
""")

    st.subheader("Technologies Used")

    st.markdown("""
- React
- FastAPI
- SQL Server Express
""")

    st.subheader("System Features")

    st.markdown("""
- Medicine management
- Inventory management
- Sales management
- Customer management
- Database integration
- Authentication
- CRUD operations
""")

    st.subheader("My Contribution")

    st.markdown("""
- Frontend development with React
- Backend API development using FastAPI
- Database implementation using SQL Server Express
- CRUD functionality
- Testing and debugging
""")

    st.subheader("Outcome")

    st.write("""
The application streamlines pharmacy operations by providing an integrated solution for inventory, medicine management, and sales while ensuring efficient database management and a user-friendly interface.
""")