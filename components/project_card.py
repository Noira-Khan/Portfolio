import streamlit as st


def project_card(
    title: str,
    subtitle: str,
    image_path: str,
    page_path: str,
    button_key: str,
):
    """
    Reusable Project Card
    """

    with st.container():

        # Cover Image
        st.image(image_path, use_container_width=True)

        # Title
        st.markdown(f"## {title}")

        # Description
        st.caption(subtitle)

        # View Project Button
        if st.button(
            "View Project →",
            key=button_key,
            use_container_width=True,
            type="primary",
        ):
            st.switch_page(page_path)

        st.markdown("---")