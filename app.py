import streamlit as st
import os

# Sidebar navigation
st.sidebar.title('Navigation')
section = st.sidebar.radio('Go to', ['Home', 'Resume', 'Projects', 'Contact'])

# Home/About Me
if section == 'Home':
    st.header('About Me')
    cols = st.columns([2,1])
    with cols[0]:
        st.markdown('<h1 style="margin-bottom:0;">Lukas Fisher</h1>', unsafe_allow_html=True)
        st.write('📍 Portland, OR')
        st.write('📚 University of Denver, Ritchie School of Engineering and Computer Science')
        st.write('📧 lukasfisher2002@gmail.com')
        st.write('[LinkedIn](https://www.linkedin.com/in/lukas-fisher-0b88a4276/)')
        st.write('**Academic and Career Highlights:**')
        st.markdown('''
- BS in Mechanical Engineering from the University of Denver
- GPA: 3.68
- Proficient in SolidWorks, ANSYS Fluent, and MATLAB
- Worked for the University of Denver's Center for Sustainability
- Currently working for Portland City United as an Assistant Soccer Coach

        ''')
        st.write('**Personal Interests:**')
        st.markdown('''
- Former D1 Soccer Player
- Traveling and exploring new destinations
- Fly fishing, camping, rafting, anything outdoors
- Plant Based foods and cooking      
        ''')
    image_path = os.path.join(os.path.dirname(__file__), 'profile.png')
    with cols[1]:
        st.image(image_path, width=188)
    st.write('')
    # Add two images side by side at the bottom of the Home section (direct file names)
    img_cols = st.columns(2)
    with img_cols[0]:
        st.image('./soccer.JPG', caption='Mens Soccer Final Four', use_container_width=True)
    with img_cols[1]:
        st.image('./fishpic.JPG', caption='Madison River, MT', use_container_width=True)

# Resume
elif section == 'Resume':
    st.header('Resume')
    st.subheader('Education')
    st.write('''**University of Denver, Denver, CO (September 2020 - December 2024)**  \
             
    BS in Mechanical Engineering, Minors in Mathematics and Sustainability  \
             
    GPA: 3.68''')
    st.write('Relevant Courses: Computational Fluid Dynamics, Mechanical Systems w/ CAD, Heat Transfer, Power and Energy, Renewable Energy Systems.')
   
    st.write('''**Central Catholic High School, Portland, OR (August 2016 - May 2020)**  \
             
    Four-year Honor Student, National Honor Society member \
             
    GPA: 4.22  ''')
    st.subheader('Experience')
    st.write('**Assistant Soccer Coach at Portland City United (January 2025 - Present)**  \nU8 and U18 Boys teams')
    st.write('**Division I Mens Soccer Player, University of Denver (September 2020 – December 2024)**  \n'
             'Played 73 games over 5 seasons while pursuing a STEM degree')
    st.write('**Mathematics Tutor, University of Denver (September 2024 – December 2024)**  \n'
             'Assisted first-year students with Calculus and Business Calculus')
    st.write('**Center for Sustainability, University of Denver (September 2022 – June 2023)**  \n'
             'Managed programs to provide low-cost clothes and food to students in need')
    st.subheader('Technical Skills')
    st.write('SolidWorks, ANSYS Fluent, MATLAB')
    # Fix download button to serve the actual PDF file
    with open("Resume.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    st.download_button(label="Download Resume (PDF)", data=PDFbyte, file_name="Resume.pdf", mime="application/pdf")

# Projects
elif section == 'Projects':
    st.header('Projects')
    st.markdown('<span style="font-size:18px; font-weight:600;">\'Surfing into Sustainability – Reimagining Surfboards for a Better Planet\'</span>', unsafe_allow_html=True)
    st.write('- Senior capstone project: Led a team to design a 100% recycleable and 100% recycled surfboard alternative.')
    st.write('- Presented to 300+ university peers, faculty, and staff.')
    image_path = os.path.join(os.path.dirname(__file__), 'project1.jpeg')
    cols = st.columns([1,2,1])
    with cols[1]:
        st.image(image_path, caption='Design Stage Prototype Surfboard', width=300)
    st.write('More projects coming soon!')

# Contact
elif section == 'Contact':
    st.header('Contact')
    st.write('''
    - Email: lukasfisher2002@gmail.com  
    - Phone: 503 544 9934  
    - [LinkedIn](https://www.linkedin.com/in/lukas-fisher-0b88a4276/)
    ''') 
