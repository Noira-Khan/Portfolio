import streamlit as st


def navbar():

    st.markdown(
        """
        <style>

        .navbar-container{
            position:sticky;
            top:0;
            background:white;
            z-index:999;
            border-bottom:1px solid #E5E7EB;
            margin-bottom:30px;
            padding:12px 0;
        }

        .logo{
            font-size:34px;
            font-weight:700;
            color:#111827;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="navbar-container">', unsafe_allow_html=True)

    c1, c2, c3, c4, c5, c6, c7 = st.columns(
        [2.8, 1, 1.2, 1.1, 1.4, 1, 1]
    )

    # Empty space where the logo used to be
    with c1:
        st.markdown("Noira Khan", unsafe_allow_html=True)

    with c2:
        if st.button("About", key="nav_about", use_container_width=True):
            st.switch_page("pages/about.py")

    with c3:
        if st.button("Case Studies", key="nav_case", use_container_width=True):
            st.switch_page("pages/Case_Studies.py")

    with c4:
        if st.button("Experience", key="nav_exp", use_container_width=True):
            st.switch_page("pages/experience.py")

    with c5:
        if st.button("AI Projects", key="nav_projects", use_container_width=True):
            st.switch_page("pages/Products_Built.py")

    with c6:
        if st.button(
        "Contact",
        key="nav_contact",
        use_container_width=True
    ):
            st.switch_page("pages/contact.py")

    st.markdown("</div>", unsafe_allow_html=True)