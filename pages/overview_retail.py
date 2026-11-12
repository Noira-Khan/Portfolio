import streamlit as st

from components.layout import Layout
from components.navbar import navbar
from components.project_card import project_links
from data.projects import by_slug

project = by_slug("retail")

Layout.setup(page_title=project["title"], page_icon="🛍️")
navbar()

# -------------------------------------------------------
# Hero
# -------------------------------------------------------

st.title(project["title"])

st.markdown("""
### Search 44,417 fashion products with words or a photo. Retrieval stays on the machine.
""")

st.write(project["summary"])
project_links(project)

st.image(
    "products/retail_assistant/rag_cover.jpg",
    use_container_width=True
)

st.divider()

# -------------------------------------------------------
# Project Highlights
# -------------------------------------------------------

st.subheader("Project Highlights")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Catalogue", "44,417")

with c2:
    st.metric("Default search", "Lexical")

with c3:
    st.metric("Semantic", "Optional")

with c4:
    st.metric("API key", "Not required")

st.divider()

# -------------------------------------------------------
# Application Screenshots
# -------------------------------------------------------

st.header("📸 Application Screenshots")

st.write(
    "Explore the major workflows of the Multimodal Retail Assistant."
)

left, center, right = st.columns([1, 3, 1])

with center:

    st.image(
        "products/retail_assistant/screenshots/home.png",
        caption="Home Dashboard",
        use_container_width=True
    )

    st.image(
        "products/retail_assistant/screenshots/image_search.png",
        caption="Image Search",
        use_container_width=True
    )

    st.image(
        "products/retail_assistant/screenshots/ai_analysis.png",
        caption="AI Product Analysis",
        use_container_width=True
    )

    st.image(
        "products/retail_assistant/screenshots/comparison_products.png",
        caption="Product Comparison",
        use_container_width=True
    )

    st.image(
        "products/retail_assistant/screenshots/comparison_results.png",
        caption="Comparison Results",
        use_container_width=True
    )

    st.image(
        "products/retail_assistant/screenshots/analytics.png",
        caption="Analytics Dashboard",
        use_container_width=True
    )

st.divider()

# -------------------------------------------------------
# Project Overview
# -------------------------------------------------------

st.header("Project Overview")

st.write(project["summary"])
st.write(project["decision"])

st.divider()

# -------------------------------------------------------
# Business Problem
# -------------------------------------------------------

st.header("Business Problem")

st.write("""
Traditional e-commerce platforms rely heavily on keyword matching, making it difficult for customers to discover products when they don't know the exact product name or struggle to describe what they're looking for.

Common challenges include:

• Inability to search using images

• Poor semantic understanding of user intent

• Limited product discovery

• Low recommendation relevance

• Reduced customer engagement

These limitations often lead to abandoned searches and missed sales opportunities.
""")

st.divider()

# -------------------------------------------------------
# Solution
# -------------------------------------------------------

st.header("Solution")

st.write("""
The Multimodal Retail Assistant combines several AI technologies into a unified shopping experience.

The system enables users to:

• Search products using natural language

• Upload images for visual similarity search

• Retrieve semantically relevant products using vector search

• Ask AI-powered questions about products

• Compare multiple products before making purchasing decisions

The application leverages Retrieval-Augmented Generation (RAG) to provide grounded recommendations while reducing hallucinations through metadata-aware retrieval.
""")

st.divider()

# -------------------------------------------------------
# Key Features
# -------------------------------------------------------

st.header("Key Features")

col1, col2 = st.columns(2)

with col1:
    st.success("Semantic Product Search")
    st.success("Visual Product Search")
    st.success("RAG-based Retrieval")
    st.success("Natural Language Queries")
    st.success("AI Product Analysis")

with col2:
    st.success("Product Comparison")
    st.success("Analytics Dashboard")
    st.success("Context-aware Recommendations")
    st.success("Modern Streamlit UI")
    st.success("Scalable Vector Search")

st.header("Tech Stack")

st.markdown("""
<span style="
background:#24292f;
color:white;
padding:6px 12px;
border-radius:8px;
margin:4px;
display:inline-block;">
🐍 Python
</span>

<span style="
background:#ff4b4b;
color:white;
padding:6px 12px;
border-radius:8px;
margin:4px;
display:inline-block;">
⚡ Streamlit
</span>

<span style="
background:#2e8b57;
color:white;
padding:6px 12px;
border-radius:8px;
margin:4px;
display:inline-block;">
🔍 TF–IDF
</span>

<span style="
background:#ff9800;
color:white;
padding:6px 12px;
border-radius:8px;
margin:4px;
display:inline-block;">
FAISS MiniLM
</span>

<span style="
background:#6f42c1;
color:white;
padding:6px 12px;
border-radius:8px;
margin:4px;
display:inline-block;">
🤗 Hugging Face
</span>

<span style="
background:#007acc;
color:white;
padding:6px 12px;
border-radius:8px;
margin:4px;
display:inline-block;">
🧠 Gemini
</span>

<span style="
background:#0d9488;
color:white;
padding:6px 12px;
border-radius:8px;
margin:4px;
display:inline-block;">
📚 RAG
</span>

<span style="
background:#795548;
color:white;
padding:6px 12px;
border-radius:8px;
margin:4px;
display:inline-block;">
👁 Computer Vision
</span>

""", unsafe_allow_html=True)

st.divider()

# -------------------------------------------------------
# Product Thinking
# -------------------------------------------------------

st.header("Product Thinking")

st.write("""
This project was designed with a product mindset rather than as a standalone AI prototype.

The primary objective was to improve the online shopping experience by reducing search friction and enabling users to discover products more intuitively.

From a product perspective, the solution focuses on:

• Improving product discoverability

• Reducing dependency on exact keyword searches

• Delivering personalized shopping experiences

• Increasing customer engagement through conversational AI

• Building a scalable architecture for future recommendation capabilities

The application demonstrates how AI can solve a real customer problem while supporting measurable business outcomes such as higher engagement and improved product discovery.
""")

st.divider()

# -------------------------------------------------------
# Business Impact
# -------------------------------------------------------

st.header("Business Impact")

c1, c2 = st.columns(2)

with c1:
    st.success("✔ Improved Product Discoverability")
    st.success("✔ Reduced Search Friction")
    st.success("✔ Semantic Product Retrieval")
    st.success("✔ Faster Customer Decision Making")

with c2:
    st.success("✔ AI-powered Recommendations")
    st.success("✔ Explainable Search Results")
    st.success("✔ Scalable Vector Search Architecture")
    st.success("✔ Enhanced Shopping Experience")

st.divider()

# -------------------------------------------------------
# Future Roadmap
# -------------------------------------------------------

st.header("🗺️ Future Roadmap")

st.markdown("""
### Completed

- Semantic Product Search
- Visual Image Search
- AI Product Analysis
- Product Comparison
- Analytics Dashboard
- Retrieval-Augmented Generation (RAG)

---

### Planned Enhancements

- 🎤 Voice-based Shopping Assistant
- ❤️ Personalized Recommendations
- 👕 AI Outfit Generation
- 📦 Real-time Inventory Integration
- 👤 Customer Preference Memory
- ☁️ Cloud-native Vector Database
- ⚡ Hybrid Search (Image + Text)
- 📊 User Behaviour Analytics
""")

st.divider()

# -------------------------------------------------------
# Development Journey
# -------------------------------------------------------

st.header("🗓️ Development Journey")

st.markdown("""
The project was developed incrementally, with each phase introducing a new AI capability to enhance the shopping experience.
""")

st.markdown(
    """
- Lexical search, filters, comparison, recommendations, and catalogue answers run without an API key.
- Semantic FAISS is a separate index build. It is not the default path.
- Gemini is used for an uploaded-photo caption and for free-form styling notes.
- Voice input is a separate prototype, [Quiet Push-to-Talk](https://github.com/Noira-Khan/voice-input-prototype), not a mode inside this app.
- The dataset has no prices, so the UI does not filter by price.
"""
)

st.divider()

# -------------------------------------------------------
# Live Demo
# -------------------------------------------------------

st.header("Open the project")

st.write(
    "The Streamlit app and the GitHub repository are separate from this portfolio. "
    "Search, filters, comparison, and catalogue answers run without an API key."
)

project_links(project)

st.info(
    "💡 Try uploading a fashion image or searching for products using natural language to experience semantic search, AI-powered recommendations, product comparison, and analytics."
)

st.divider()