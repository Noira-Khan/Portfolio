import streamlit as st

from components.layout import Layout
from components.navbar import navbar
from components.project_card import project_card
from data.projects import PROJECTS

Layout.setup(page_title="Products")
navbar()

st.title("Products")
st.write(
    "Shipped work from github.com/Noira-Khan. "
    "Case studies on this site use the same list, so a new repository is added once."
)

left, right = st.columns(2, gap="large")
columns = [left, right]
for index, project in enumerate(PROJECTS):
    with columns[index % 2]:
        project_card(project, button_key=f"products-{project['slug']}")
