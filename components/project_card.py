import streamlit as st


def project_card(
    title: str,
    subtitle: str,
    image_path: str,
    page_path: str,
    button_key: str,
):
    """
    Reusable project card.

    Parameters
    ----------
    title : Project title
    subtitle : Short description
    image_path : Path to cover image
    page_path : Path used by st.switch_page()
    button_key : Unique button key
    """

    st.markdown(
        """
        <style>

        .project-card{
            background:white;
            border-radius:18px;
            overflow:hidden;
            border:1px solid #ececec;
            box-shadow:0 8px 20px rgba(0,0,0,0.08);
            transition:all .35s ease;
            margin-bottom:20px;
        }

        .project-card:hover{
            transform:translateY(-6px);
            box-shadow:0 18px 40px rgba(0,0,0,.16);
        }

        .project-image img{
            width:100%;
            border-radius:18px 18px 0 0;
        }

        .project-content{
            padding:18px;
        }

        .project-title{
            font-size:28px;
            font-weight:700;
            color:#1f2937;
            margin-bottom:8px;
        }

        .project-subtitle{
            font-size:16px;
            color:#6b7280;
            line-height:1.6;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="project-card">', unsafe_allow_html=True)

    st.markdown('<div class="project-image">', unsafe_allow_html=True)
    st.image(image_path, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="project-content">
            <div class="project-title">
                {title}
            </div>

            <div class="project-subtitle">
                {subtitle}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("View Project →", key=button_key, use_container_width=True):
        st.switch_page(page_path)

    st.markdown("</div>", unsafe_allow_html=True)