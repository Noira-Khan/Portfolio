import streamlit as st

from components.navbar import navbar
from components.project_card import project_card

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="Products Built",
    page_icon="🚀",
    layout="wide",
)

# --------------------------------------------------
# Hide Streamlit Sidebar
# --------------------------------------------------

st.markdown("""
<style>

/* Hide sidebar */
[data-testid="stSidebar"]{
    display:none;
}

/* Hide sidebar expand button */
[data-testid="collapsedControl"]{
    display:none;
}

/* Reduce top padding */
.block-container{
    padding-top:2rem;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Navbar
# --------------------------------------------------

navbar()

# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("Products Built")

st.markdown(
"""
Explore a collection of AI products that I designed and developed, combining
Artificial Intelligence, Machine Learning and Product Thinking to solve
real-world business problems.
"""
)

st.markdown("---")

# ==================================================
# PROJECT 1
# ==================================================

project_card(
    title="🛍️ Multimodal Retail Assistant",
    subtitle="""
AI-powered fashion discovery platform using Computer Vision,
Retrieval-Augmented Generation (RAG) and Large Language Models.
""",
    image_path="products/retail_assistant/rag_cover.jpg",
    page_path="pages/overview_retail.py",
    button_key="retail",
)

# ==================================================
# PROJECT 2
# ==================================================

project_card(
    title="Finance Shield AI",
    subtitle="""
AI-powered credit card fraud detection system using
Machine Learning, FastAPI and Streamlit.
""",
    image_path="products/fraud_detection/fraud_cover.jpeg",
    page_path="pages/overview_fraud.py",
    button_key="fraud",
)