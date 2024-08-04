import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
# Set the title of the web app
# st.title("Tech & Analytics Consultancy")

# Load the logo image
logo = Image.open("images/logo_vectorize.png")

# Add a navigation bar to the sidebar
with st.container():
    st.image(logo, use_column_width=True)
    selected = option_menu(
        menu_title=None,
        options=["About Us", "Tech Stack", "Contact Us"],
        icons=["info-circle", "tools", "envelope"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
            "nav-link": {
                "text-align": "left",
                "--hover-color": "#eee",
            }
        }
    )

# Content for each section
if selected == "About Us":
    st.subheader("Intelligent, Fast, Direct")
    st.header("What We Do")

    # Intelligent Solutions Section
    st.subheader("Intelligent Solutions")
    st.markdown("""
    - **AI and Data Analytics Solutions**: Leveraging advanced algorithms and machine learning techniques to transform data into actionable insights.
    - **Predictive Analytics**: Anticipating future trends and behaviors to help you stay ahead of the competition.
    - **Business Intelligence**: Implementing robust BI tools to enhance decision-making processes.
    """)

    # Fast Implementation Section
    st.subheader("Fast Implementation")
    st.markdown("""
    - **Rapid Prototyping**: Quickly developing prototypes to validate ideas and accelerate project timelines.
    - **Agile Development**: Employing agile methodologies to ensure quick turnaround and continuous delivery of high-quality software.
    - **Cloud Integration**: Swiftly integrating cloud solutions to enhance scalability and performance.
    """)

    # Direct Approach Section
    st.subheader("Direct Approach")
    st.markdown("""
    - **Solutions Architecture Advice**: Providing clear and straightforward guidance on designing efficient and scalable IT architectures.
    - **Cloud Advisory Services**: Offering expert advice on cloud strategy, migration, and optimization to maximize ROI.
    - **Technical Consulting**: Delivering direct and practical solutions to complex technical challenges.
    - **Software Engineering Services**: Crafting tailored software solutions to meet your unique business needs with precision and clarity.
    """)

elif selected == "Tech Stack":
    st.header("Our Tech Stack")
    st.markdown("""
    - **Programming Languages**: Python, JavaScript, SQL
    - **Frameworks**: Flask, Django, React, Angular
    - **Data Tools**: Pandas, NumPy, SciPy, TensorFlow, PyTorch
    - **Cloud Platforms**: AWS, Azure, Google Cloud
    - **DevOps**: Docker, Kubernetes, Jenkins, Git
    """)

elif selected == "Contact Us":
    st.header("Contact Us")
    st.markdown("""
    - **Email**: christian.ferrao@gmail.com
    - **Social Media**:
        - [LinkedIn](https://www.linkedin.com/in/christian-pfeiffer-ferrao-b96434110/)
    """)


