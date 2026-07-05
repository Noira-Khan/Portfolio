import streamlit as st


def navbar():

    st.markdown(
        """
        <div class="navbar">

            <div class="logo">
                <a href="/">Noira Khan</a>
            </div>

            <div class="nav-links">
                <a href="#about">About</a>
                <a href="#case-studies">Case Studies</a>
                <a href="#experience">Experience</a>
                <a href="#projects">Products Built</a>
                
                <a href="#contact">Contact</a>
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )
    