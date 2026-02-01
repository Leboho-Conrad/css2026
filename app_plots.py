# CV

import pandas as pd
import streamlit as st



# Page setup
st.set_page_config(page_title="Leboho Conrad Ngako CV", layout="wide")

# Header
st.title("Leboho Conrad Ngako")
st.subheader(" Full Stack Developer  |  Software Developer  |  Data Analyst  |  Data Scientist ")

# Contact Information with clickable icons
st.header("Contacts")

st.markdown("""
📧 [Email](mailto:conradngako@gamil.com)  |📞 [Phone](tel:+27732601433) |🔗 [LinkedIn](https://www.linkedin.com/in/leboho-conrad-ngako-a523a7273/)  |💻 [GitHub](https://github.com/Leboho-Conrad)  
📍 Johannesburg, South Africa
""")


# Profile Summary
st.header("Profile Summary")
st.write("""
 A passionate recent BSc Mathematical Sciences graduate majoring in Statistics
 and Computer Science with a strong interest in technology and analytics. 
 Demonstrates sound knowledge of statistical methods, programming principles,
 and problem-solving techniques, with a proactive approach to learning new 
 technologies. Seeking an internship or graduate opportunity to gain practical 
 experience and contribute to data-driven and technology-based solutions.
""")

# Education
st.header("🎓Education")
st.subheader("-Bachelor of Science In Mathematical Sciences , University Of Limpopo (2022-2025)  ")
st.write("""
         **RELEVENT COURSEWORK:** 
         
             -Databases,
             -Artificial Intelligence,
             -Computer Networks,
             -Operating Systems, 
             -Data Structures & Algorithms,
             -Time Series Analysis, 
             -Sampling theory,
             -Inferencial Statistics,
             -Applied Linear Regression,
             -Linear Algrebra, 
             -Advanced Calculus.
    
""")


# Technical Skills
st.header("🛠 Technical Skills")

skills = [
    "HTML & CSS",
    "JavaScript",
    "PHP",
    "React.js",
    "Python",
    "PostgreSQL",
    "SQL",
    "Node.js",
    "Express.js",
    "Java",
    "Web Application",
    "Machine Learning",
    "Data Visualization",
    "Big Data Analysis"
]

st.markdown("\n".join([f"- {skill}" for skill in skills]))


# Soft Skills
st.header("🛠Soft Skills")
st.write("""
- Strong Verbal & Communication Skills        
- Collaboration & Teamwork
- Problem-Solving & Critical Thinking
- Adaptability & Continuous Learning
- Time Management & Organization 
""")

# Certifications
st.header("📜Certifications")

st.markdown("""
📜 [Data Science 101 (IBM)](https://courses.skillsbuild.skillsnetwork.site/certificates/7ce7148fa338482faf3ee2c2a0187dd3)  
📜 [Data Science Tools (IBM)](https://courses.skillsbuild.skillsnetwork.site/certificates/eece901b0dd6497b824b1f8413f605e0)  
📜 [MOBILE DIGITAL LITERACY (NEMISA - UL) ](https://doc-00-1s-apps-viewer.googleusercontent.com/viewer/secure/pdf/1uskh4v532gu0e7fneri73qpf2i7hs4f/ar5iojpl2redi103tjssn7mf83vudvdf/1769884050000/drive/12605077334137569845/ACFrOgC383uZrEMXO7QNxtkaSk5b-FkMhmtHZpTyK5bai1Ov43ee1ysNhq15vSkjLACA7EhbqPiPd7imEza2D4flwtKhk1I15shqJ3rmI7bCK3piWfVBddZjPQWf7qxuIT5Zo5PPwjwbUtsVXHkbxMbuvNd86Tzwa6ozWMFO449dVtljpie5dyhZAxkYfVyR9F-xMxReDU3fGT00PV0HA01P7yclhDujgYaCnvPzSE68S_UtES3anFSGzFTCUf9VFHBY9gR36qhXoQ-BKkrs?print=true&nonce=u22nngtv69t5k&user=12605077334137569845&hash=b672j75lpsb7v9co0evtd8jmu15m3io8)  
📜 [Digital Literacy Made Easy (NEMISA - UL) ](https://doc-0o-1s-apps-viewer.googleusercontent.com/viewer/secure/pdf/1uskh4v532gu0e7fneri73qpf2i7hs4f/v5pb36cpogk37laqcq6fpqs8ob7i7b1a/1769884200000/drive/12605077334137569845/ACFrOgAROokYahrNdLihDdA6TaWlV4iiDOfdO51HijmsjYhHTWTrRIA35giOMWeg66iDei2IVoINUtRrTSCdqsk3A7hZOa68scrpufSRs4AIbfUrm0uIFUskOAEv3IUZdHLDT9Hpk_4buqtn-M5YznIdWlJMjx2vJa1RJYX0I9_XkrFWZT9tYKKT011gr7J8v8Ruo72p9HfQRp70J6UUL0DZN5qdD8a4nsR47SbVFvXoKIQ0zfCINo-vaJz8_IBAlWspB1AVZ0VpfNcEQpA_?print=true)  

""")




# Projects
st.header("💼Projects")
st.write("""
**Project 1: E-Commerce Store**  

-Frontend: HTML, CSS & Javascript 
 
-Backend: PHP

-Database: PostgreSQL 

-Features:
    
    -Product catalog with categories
    -Shopping cart and checkout
    -Order history and user profiles
    -Admin panel (add/remove products)
   
**Project 2: Car Rental website**  
 
-Frontend (User Interface)
Tech: React 

-Features:
    
      -Browse available cars (with filters: type, price, location)
      -Booking form (select dates, car type, pickup/drop-off location)
      -User login/signup
      -Dashboard for viewing reservations
      
-Backend (Server & API)
Tech: Node.js  with Express 

-Features:
    
      -REST API endpoints for cars, users, and bookings
      -Authentication (JWT or session-based)
      -Business logic ( prevent double-booking the same car)

 -Database:PostgreSQL


https://auto-rent-o.netlify.app/        (still under development)

https://pgc-gym-0.netlify.app/#                ||
 
""")



# Languages
st.header("🌍Languages")
st.write("""
- English 
- Sepedi 
""")


# Interests
st.header("⚽Interests & Hobbies")
st.write("""
- Research in AI and Machine Learning    
- Football
- Chess  
""")



st.markdown("© 2026 leboho Conrad Ngako. Built with Streamlit.")
