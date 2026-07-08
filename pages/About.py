import streamlit as st
from components.navbar import navbar
from components.about import about

st.set_page_config(layout="wide")

navbar()
about()