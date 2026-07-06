import streamlit as st
from pathlib import Path


def contact_section():
    st.title("Let's Connect")

    st.write(
        """
I'm always interested in discussing new opportunities, collaborations, or just having a chat about AI and product management.

Feel free to reach out.
"""
    )

    st.write("")
    st.write("")

    left, right = st.columns(2, gap="large")

    # =====================================================
    # LEFT COLUMN
    # =====================================================

    with left:
        # ---------------- Email ---------------- #

        c1, c2 = st.columns([1, 8])

        with c1:
            st.image("assets/icons/Gmail.png", width=38)

        with c2:
            st.markdown("### Email")

        st.markdown(
            """
<a href="mailto:noirak4@gmail.com?subject=Opportunity%20for%20AI%20Product%20Manager">
noirak4@gmail.com
</a>
""",
            unsafe_allow_html=True,
        )

        st.write("")
        st.write("")

        # ---------------- Phone ---------------- #

        c1, c2 = st.columns([1, 8])

        with c1:
            st.image("assets/icons/Phone.jpeg", width=38)

        with c2:
            st.markdown("### Phone")

        st.markdown(
            """
<a href="tel:+918755972525">
+91 87559 72525
</a>
""",
            unsafe_allow_html=True,
        )

        st.write("")
        st.caption("Usually responds immediately.")

    # =====================================================
    # RIGHT COLUMN
    # =====================================================

    with right:
        # ---------------- LinkedIn ---------------- #

        c1, c2 = st.columns([1, 8])

        with c1:
            st.image("assets/icons/LinkedIn.png", width=38)

        with c2:
            st.markdown("### LinkedIn")

        st.link_button(
            "Open LinkedIn",
            "https://www.linkedin.com/in/noira-khan/",
            use_container_width=True,
        )

        st.write("")
        st.write("")

        # ---------------- Resume ---------------- #

        c1, c2 = st.columns([1, 8])

        with c1:
            st.image("assets/icons/resume.jpeg", width=45)

        with c2:
            st.markdown("### Resume")

        resume = Path("assets/resume/resume_noira_khan.pdf")

        if resume.exists():
            with open(resume, "rb") as pdf:
                st.download_button(
                    label="Download Resume",
                    data=pdf,
                    file_name="Noira_Khan_Resume.pdf",
                    mime="application/pdf",
                    use_container_width=True,
                    key="contact_resume",
                )