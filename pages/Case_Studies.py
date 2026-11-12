import streamlit as st

from components.layout import Layout
from components.navbar import navbar
from components.project_card import project_links
from data.projects import PROJECTS

Layout.setup(page_title="Case studies")
navbar()

st.title("Case studies")
st.write(
    "Each study is one public repository. The problem is the decision the product "
    "has to make. The proof lines are the constraints already written in that repo."
)

for project in PROJECTS:
    st.divider()
    st.subheader(project["title"])
    st.caption(project["eyebrow"])
    st.markdown(f"**Problem.** {project['problem']}")
    st.markdown(f"**Decision.** {project['decision']}")
    if st.button("Open the full page", key=f"case-{project['slug']}"):
        st.switch_page(project["page"])
    project_links(project)
