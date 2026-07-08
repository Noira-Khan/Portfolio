import streamlit as st

from components.navbar import navbar

st.set_page_config(
    page_title="Multimodal Retail Assistant",
    page_icon="🛍️",
    layout="wide"
)

navbar()

# -----------------------------
# Hero
# -----------------------------

st.title("🛍️ Multimodal Retail Assistant")

st.markdown("""
### AI-powered Fashion Discovery using Computer Vision, RAG & Large Language Models
""")

st.image("products/retail_assistantrag_cover.jpg", use_container_width=True)

st.divider()

# -----------------------------
# Project Overview
# -----------------------------

st.header("📌 Project Overview")

st.write("""
The **Multimodal Retail Assistant** is an AI-powered shopping assistant that helps users
discover fashion products using natural language and visual search.

Instead of relying only on keyword matching, the assistant understands user intent,
retrieves relevant products using Retrieval-Augmented Generation (RAG), and provides
personalized recommendations through Large Language Models.

The application demonstrates how Generative AI can improve product discovery,
reduce search friction, and create a conversational shopping experience.
""")

st.divider()

# -----------------------------
# Business Problem
# -----------------------------

st.header("💼 Business Problem")

st.write("""
Traditional e-commerce search often depends on exact keyword matching.

Customers frequently struggle to:

- Find products similar to an image
- Describe fashion items using natural language
- Discover relevant alternatives
- Receive personalized recommendations

This results in poor product discovery and reduced conversion rates.
""")

st.divider()

# -----------------------------
# Solution
# -----------------------------

st.header("💡 Solution")

st.write("""
The application combines multiple AI capabilities into a single shopping assistant.

It enables users to:

- Search products using natural language
- Retrieve visually similar products
- Ask AI questions about products
- Receive context-aware recommendations
- Compare multiple products before purchase

The system combines Computer Vision, Vector Search, Retrieval-Augmented Generation (RAG),
and Large Language Models to deliver relevant shopping experiences.
""")

st.divider()

# -----------------------------
# Key Features
# -----------------------------

st.header("✨ Key Features")

col1, col2 = st.columns(2)

with col1:
    st.success("Semantic Product Search")
    st.success("RAG-based Retrieval")
    st.success("Natural Language Queries")
    st.success("Product Recommendations")

with col2:
    st.success("Visual Search")
    st.success("AI Shopping Assistant")
    st.success("Product Comparison")
    st.success("Modern Streamlit UI")

st.divider()

# -----------------------------
# Tech Stack
# -----------------------------

st.header("🛠️ Tech Stack")

st.markdown("""
- Python
- Streamlit
- FAISS
- Sentence Transformers
- Hugging Face
- Retrieval-Augmented Generation (RAG)
- Large Language Models
- Computer Vision
""")

st.divider()

# -----------------------------
# Product Thinking
# -----------------------------

st.header("Product Thinking")

st.write("""
The focus of this project was not only building an AI application but designing a product
that improves customer experience.

Key product considerations included:

- Reducing search effort
- Improving product discoverability
- Increasing user engagement
- Supporting conversational shopping
- Creating a scalable recommendation workflow
""")

st.divider()

# -----------------------------
# Future Roadmap
# -----------------------------

st.header(" Future Enhancements")

st.markdown("""
- Voice-based shopping assistant
- Personalized recommendations based on user history
- Outfit generation
- Real-time inventory integration
- Customer preference memory
""")

st.divider()

# -----------------------------
# Demo
# -----------------------------

st.header("🔗 Live Demo")

col1, col2 = st.columns(2)

with col1:
    st.link_button(
        "🚀 Launch Streamlit Demo",
        "https://multimodal-rag-pro-search.streamlit.app/"
    )

with col2:
    st.link_button(
        "💻 GitHub Repository",
        "https://github.com/Noira-Khan/multimodal-rag-product-search"
    )