import streamlit as st
from components.section_title import section_title
from components.project_card import project_card


def products_built():

    st.write("")
    st.divider()

    section_title(
        "PRODUCTS BUILT",
        "AI-powered applications combining engineering, machine learning, and product thinking."
    )

    st.write("")

    project_card(
        title="Multimodal Retail Assistant",
        subtitle="AI-powered shopping assistant using Multimodal Search, Retrieval-Augmented Generation (RAG), and Large Language Models.",
        tags=[
            "RAG",
            "LLM",
            "Computer Vision",
            "Streamlit",
            "Python"
        ],
        image="assets/images/retail.png",
        github="#",
        demo="#",
        page="projects/retail_assistant/overview_retail.py"
    )
    project_card(
        title="AI Fraud Detection",
        subtitle="Machine Learning pipeline for detecting fraudulent financial transactions with explainable predictions.",
        tags=[
            "Machine Learning",
            "FastAPI",
            "Python",
            "Scikit-Learn"
        ],
        image="assets/images/fraud.png",
        github="#",
        demo="#",
        page="projects/fraud_detection/overview_fraud.py"
    )
    project_card(
        title="AI Interview Coach",
        subtitle="LLM-powered interview preparation assistant with personalized feedback and question generation.",
        tags=[
            "LLM",
            "Prompt Engineering",
            "FastAPI",
            "Python"
        ],
        image="assets/images/interview.png",
        github="#",
        demo="#",
        page="projects/interview_coach/overview_interview.py"
    )
    project_card(
        title="AI Customer Support Agent",
        subtitle="Conversational AI assistant capable of answering customer queries using Retrieval-Augmented Generation.",
        tags=[
            "RAG",
            "LLM",
            "FastAPI",
            "Streamlit"
        ],
        image="assets/images/support.png",
        github="#",
        demo="#",
        page="projects/support_agent/overview_support.py"
    )
    st.write("")
    st.info(
        "More AI products are currently under development as I continue exploring Product Management, Generative AI, and Intelligent Systems."
    )

    st.write("")