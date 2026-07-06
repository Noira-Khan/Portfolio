from pathlib import Path
import streamlit as st


def hero():

    left, right = st.columns([1.6, 1], gap="large")

    # ==========================================
    # LEFT
    # ==========================================

    with left:

        st.caption("Hi, I'm")

        st.title("Noira Khan")

        st.markdown(
            """
### Engineer Business Systems Analyst  
## Transitioning to AI Product Management
"""
        )

        st.write("")

        st.write(
            """
Building intelligent AI products using **Machine Learning,
Retrieval-Augmented Generation (RAG), Large Language Models,
and Product Strategy**.

I enjoy transforming customer problems into scalable AI-powered
solutions through product thinking, experimentation, and user research.
"""
        )

        st.write("")

        b1, b2 = st.columns(2)

        with b1:
            st.link_button(
                "View Case Studies",
                "https://noirakhan.github.io/portfolio/",
                
                use_container_width=True,
            )

        with b2:
            resume = Path("assets/resume/resume_noira_khan.pdf")


            if resume.exists():

                with open(resume, "rb") as pdf:

                    st.download_button(
                        "Download Resume",
                        data=pdf,
                        file_name="Noira_Khan_Resume.pdf",
                        mime="application/pdf",
                        use_container_width=True,
                        key="hero_resume"
                    )

    # ==========================================
    # RIGHT
    # ==========================================

    with right:

        st.image(
            "assets/images/selfpic.jpeg",
            use_container_width=True,
        )

        st.markdown(
            """
### Engineer Business Systems Analyst | AI Product Management 
"""
        )

    st.divider()
