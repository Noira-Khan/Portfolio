import streamlit as st

from data.projects import PROJECTS
from components.project_card import project_card


def work_strip() -> None:
    st.markdown(
        """
        <h2 style="letter-spacing:2px;color:#6B7280;">
            WORK
        </h2>
        """,
        unsafe_allow_html=True,
    )
    st.write(
        "Four public repositories. Finance Shield is the decision product. "
        "The others show retrieval with a boundary, a facts assistant that refuses, "
        "and a voice interaction that does not send until the person reviews it."
    )

    left, right = st.columns(2, gap="large")
    columns = [left, right]
    for index, project in enumerate(PROJECTS):
        with columns[index % 2]:
            project_card(project, button_key=f"home-{project['slug']}")
