import streamlit as st

from components.navbar import navbar
from components.project_card import project_card


st.set_page_config(
    page_title="Products Built",
    page_icon="🚀",
    layout="wide",
)

# -------------------------
# Navbar
# -------------------------
navbar()

# -------------------------
# Header
# -------------------------

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    """
    <h1 style='text-align:center;'>
        Products Built
    </h1>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <p style='text-align:center;
              color:gray;
              font-size:18px;
              margin-bottom:40px;'>
    AI Products built from concept to deployment.
    </p>
    """,
    unsafe_allow_html=True,
)

# -------------------------
# Product Cards
# -------------------------

col1, col2 = st.columns(2, gap="large")

with col1:

    project_card(
        title="Multimodal Retail Assistant",
        subtitle="""
AI-powered product discovery using
Vision, Retrieval-Augmented Generation (RAG),
and Large Language Models.
""",
        image_path="assets/rag_cover.png",
        page_path="products/retail_assistant/overview_retail.py",
        button_key="retail",
    )


with col2:

    project_card(
        title="Finance Shield AI",
        subtitle="""
Credit Card Fraud Detection
using Machine Learning,
FastAPI and Streamlit.
""",
        image_path="assets/fraud_cover.png",
        page_path="products/fraud_detection/overview_fraud.py",
        button_key="fraud",
    )