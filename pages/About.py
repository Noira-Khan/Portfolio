from pathlib import Path
import streamlit as st


def about():
    st.divider()

    st.markdown(
        """
        <h2 style="letter-spacing:2px;color:#6B7280;">
            ABOUT
        </h2>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    left, right = st.columns([1, 2], gap="large")

    # ===================================================
    # LEFT SIDE
    # ===================================================

    with left:
        st.image(
            "assets/images/formalpic.png",
            use_container_width=True,
        )

        st.subheader("Current")

        st.markdown(
            """
- **Unisys India Private Limited, New Delhi**
- Engineer Business Systems Analyst
- January 2024 – Present
"""
        )

        st.subheader("Previously")

        st.markdown(
            """
- Mathematics Graduate, University of Delhi (2017) — **86%**
- Microsoft AI Product Management Professional Certificate (2026)
- IIBA Business Analysis Certification (2022)
- Data Analytics & Visualization Certification (2023) — TechTaleo
- Built AI & Machine Learning projects using **RAG, LLMs, Python, SQL, and Power BI**
"""
        )

    # ===================================================
    # RIGHT SIDE
    # ===================================================

    with right:
        st.write(
            """
I'm currently working as an **Engineer Business Systems Analyst**
at **Unisys**, where I collaborate with business stakeholders,
optimize enterprise processes, and deliver technology solutions.
I have hands-on experience with B2B products in the Fintech domain.
Working in enterprise technology sparked my interest in
**Artificial Intelligence**, **Machine Learning**, synchronizing new technologies with current business.

I'm building AI-powered products that combine engineering,
customer understanding, and product strategy.
"""
        )

        st.subheader("Current Portfolio Projects")

        st.markdown(
            """
- AI Fraud Detection
- Multimodal Retail Assistant (RAG)
- AI Interview Coach
- AI Customer Support Agent
"""
        )

        st.write(
            """
My goal is to become an **AI Product Manager**
who bridges technology, customer needs, and business strategy
to build products that create meaningful impact.
"""
        )

        st.write("")

        # --------------------------
        # BUTTONS
        # --------------------------

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.link_button(
                "LinkedIn",
                "https://www.linkedin.com/in/noira-khan/",
                use_container_width=True,
            )

        with c2:
            st.link_button(
                "GitHub",
                "https://github.com/Noira-K",
                use_container_width=True,
            )

        with c3:
            resume_path = Path("assets/resume/resume_noira_khan.pdf")

            if resume_path.exists():
                with open(resume_path, "rb") as pdf:
                    st.download_button(
                        label="Download Resume",
                        data=pdf,
                        file_name="resume_noira_khan.pdf",
                        mime="application/pdf",
                        use_container_width=True,
                        key="about_resume"
                    )

    st.write("")
    st.write("")