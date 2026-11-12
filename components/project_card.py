import streamlit as st


def project_card(project: dict, *, button_key: str) -> None:
    """One catalog card. Image is optional; every card links to the case page and the repo."""

    with st.container(border=True):
        image = project.get("image")
        if image:
            st.image(image, use_container_width=True)
        else:
            st.markdown(f"**{project['eyebrow']}**")

        st.markdown(f"### {project['title']}")
        st.caption(project["summary"])

        st.write(" · ".join(project["stack"]))

        view, source = st.columns(2)
        with view:
            if st.button(
                "Case study",
                key=f"{button_key}-case",
                use_container_width=True,
                type="primary",
            ):
                st.switch_page(project["page"])
        with source:
            st.link_button(
                "GitHub",
                project["repo"],
                use_container_width=True,
            )


def project_links(project: dict) -> None:
    demo = project.get("demo")
    if demo:
        left, right = st.columns(2)
        with left:
            st.link_button("Open the app", demo, use_container_width=True)
        with right:
            st.link_button("GitHub", project["repo"], use_container_width=True)
    else:
        st.link_button("GitHub", project["repo"])
