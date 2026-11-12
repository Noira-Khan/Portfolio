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
I work on enterprise lending systems at Unisys, and I build AI products
where the output has a boundary: a card payment that is allowed or reviewed,
a fund fact that must cite one page, a catalogue answer that only uses
retrieved products, and a voice note that is not sent until it is reviewed.
"""
        )

        st.write("")

        b1, b2 = st.columns(2)

        with b1:
            if st.button("View products", use_container_width=True, type="primary"):
                st.switch_page("pages/Products_Built.py")

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
