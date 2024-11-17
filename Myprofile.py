import streamlit as st

# Set the page configuration
st.set_page_config(page_title="My Profile", page_icon=":briefcase:", layout="wide")

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About Me", "Projects", "Contact"])

# Home Page
if page == "Home":
    st.title("Welcome to My Profile!")
    st.write("Hi, I'm [Deekshith.M]. I'm a [Student] passionate about [To learn new things].")

# About Me Page
elif page == "About Me":
    st.header("About Me")
    st.write("""
    I'm [Deekshith.M], a [Editing videos ].  
    Here's a little about me:
    - 🌟 Skills: Python, Data Science, Machine Learning
    - 📚 Education: [B.Tech IT]
    - 🏆 Achievements: [sucess in 3 projects given by company ]
    """)

# Projects Page
elif page == "Projects":
    st.header("Projects")
    st.write("Here are some of the projects I've worked on:")
    st.subheader("Project 1: [Finding schoolbus]")
    st.write("[This will show the location of the school bus where it is located]")
    st.write("[GitHub Link](https://github.com)")
    
    st.subheader("Project 2: [biomatric Atteandance ]")
    st.write("[This will show the information of the given ID user]")
    st.write("[GitHub Link](https://github.com)")
    
    # Add more projects as needed

# Contact Page
elif page == "Contact":
    st.header("Contact Me")
    st.write("Feel free to reach out to me:")
    st.write("- 📧 Email: your_email@deekshith.com")
    st.write("- 💼 LinkedIn: [Deekshith linkedin Profile](https://linkedin.com)")
    st.write("- 🐦 Twitter: [Deekshith ](https://twitter.com)")