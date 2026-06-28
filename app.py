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
    st.title("📚 Lecture 12 - Database Design & Data Warehousing")

st.write("""
Lecture 12 focused on the fundamental concepts of relational database design and data
warehouse modeling. The lecture covered SQL relationships, database normalization,
Slowly Changing Dimensions (SCD), and the comparison between Star Schema and Snowflake
Schema. These concepts are essential for designing reliable databases, ensuring data
consistency, and building efficient Business Intelligence (BI) and Data Warehouse
solutions.
""")

st.markdown("---")

st.header("1. SQL Relationships")

st.markdown("""
Relationships define how data is connected between different tables in a relational
database. By using relationships, databases can avoid duplicate information while
maintaining consistency and integrity.

The lecture introduced three main relationship types:

### One-to-One (1:1)
Each record in one table is associated with exactly one record in another table.
This type of relationship is commonly used when additional information about an entity
needs to be stored separately for security or organizational purposes.

### One-to-Many (1:N)
One record from a parent table can be linked to multiple records in a child table.
For example, one customer can place many orders, while each order belongs to only one customer.
This is the most frequently used relationship in relational databases.

### Many-to-Many (M:N)
Multiple records from one table can be related to multiple records in another table.
Since relational databases cannot implement this relationship directly, an intermediate
junction table is created to connect both entities. A common example is students and courses,
where one student can enroll in many courses, and one course can have many students.
""")

st.markdown("---")

st.header("2. Database Normalization")

st.markdown("""
Database normalization is a database design technique that organizes data into
multiple related tables to reduce redundancy and improve data integrity.
A normalized database minimizes duplicated information and prevents inconsistencies
when inserting, updating, or deleting records.

The main objectives of normalization are:

- Reduce data redundancy
- Improve consistency and accuracy
- Prevent insertion anomalies
- Prevent update anomalies
- Prevent deletion anomalies
- Simplify database maintenance

The lecture introduced the first three normal forms:

### First Normal Form (1NF)
- Each column contains atomic (indivisible) values.
- Repeating groups are removed.
- Every row is uniquely identified.

### Second Normal Form (2NF)
- The table must already satisfy 1NF.
- Partial dependencies are removed.
- Every non-key attribute depends on the entire primary key.

### Third Normal Form (3NF)
- The table must satisfy 2NF.
- Transitive dependencies are eliminated.
- Every non-key attribute depends only on the primary key.

Normalization results in cleaner database structures that are easier to maintain and
less prone to data inconsistencies.
""")

st.markdown("---")

st.header("3. Slowly Changing Dimensions (SCD)")

st.markdown("""
Slowly Changing Dimensions are techniques used in data warehouses to manage changes
in dimensional data over time. They allow organizations to decide whether historical
information should be preserved or overwritten.

The lecture covered three common SCD types:

### Type 1
Old values are overwritten by new values.
Historical information is not preserved.
This approach is simple and requires less storage.

### Type 2
Instead of updating the existing record, a new row is inserted whenever changes occur.
This preserves the complete history of the data and is widely used in Business Intelligence.

### Type 3
Historical information is stored in additional columns, allowing limited history
to be maintained. This method is useful when only previous values are required.

Selecting the appropriate SCD type depends on business requirements and reporting needs.
""")

st.markdown("---")

st.header("4. Star Schema vs Snowflake Schema")

st.markdown("""
The lecture also introduced dimensional modeling, which is commonly used in Data
Warehousing for analytical processing.

### Star Schema

The Star Schema consists of one central fact table connected directly to several
denormalized dimension tables.

Advantages:
- Simple database design
- Easy to understand
- Faster query execution
- Excellent performance for reporting and analytics

Disadvantages:
- Higher data redundancy
- Requires more storage space

### Snowflake Schema

The Snowflake Schema extends the Star Schema by normalizing the dimension tables
into multiple related tables.

Advantages:
- Reduced redundancy
- Better storage efficiency
- Improved data consistency

Disadvantages:
- More complex structure
- Queries require additional joins
- Slightly slower performance compared to Star Schema

Both schemas are widely used depending on the complexity and requirements of the
data warehouse.
""")

st.markdown("---")

st.header("Key Takeaways")

st.markdown("""
After completing this lecture, I learned how relational databases organize data using
different relationship types and why proper database design is important.
I also understood how normalization improves database quality by reducing redundancy
and preventing anomalies.

Furthermore, I learned how Slowly Changing Dimensions preserve historical information
within data warehouses and how Star and Snowflake schemas support analytical processing.
These concepts provide a strong foundation for designing scalable relational databases,
developing Business Intelligence solutions, and working with modern data warehouse systems.
""")

st.success("""
Overall, Lecture 12 provided a comprehensive introduction to database design principles
and data warehouse concepts. Understanding SQL relationships, normalization,
Slowly Changing Dimensions, and dimensional schemas is essential for building efficient,
maintainable, and scalable database systems used in real-world applications.
""")