import streamlit as st


def navbar():

    st.markdown(
        """
        <style>

        .navbar-container{
            position:sticky;
            top:0;
            z-index:999;
            background:white;
            border-bottom:1px solid #E5E7EB;
            padding:12px 0;
            margin-bottom:20px;
        }

        .logo{
            font-size:30px;
            font-weight:700;
            color:#111827;
            padding-top:8px;
        }

        .stButton > button{
            width:100%;
            background:transparent;
            border:none;
            color:#6B7280;
            font-size:17px;
            font-weight:500;
            border-radius:0;
            padding:10px 0;
            transition:0.2s;
        }

        .stButton > button:hover{
            color:#111827;
            border-bottom:2px solid #111827;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="navbar-container">', unsafe_allow_html=True)

    logo, home, projects, case, resume = st.columns(
        [3.2, 1, 1.3, 1.5, 1]
    )

    with logo:
        st.markdown(
            "<div class='logo'>Noira Khan</div>",
            unsafe_allow_html=True,
        )

    with home:
        if st.button("Home", use_container_width=True):
            st.switch_page("home.py")

    with projects:
        if st.button("Products Built", use_container_width=True):
            st.switch_page("pages/Products_Built.py")

    with case:
        if st.button("Case Studies", use_container_width=True):
            st.switch_page("pages/Case_Studies.py")

    # with resume:
    #     if st.button("Resume", use_container_width=True):
    #         st.switch_page("pages/resume.py")

    st.markdown("</div>", unsafe_allow_html=True)