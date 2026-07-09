import streamlit as st

from components.navbar import navbar

st.set_page_config(
    page_title="Multimodal Retail Assistant",
    page_icon="🛍️",
    layout="wide"
)

navbar()

# -------------------------------------------------------
# Hero
# -------------------------------------------------------

st.title("🛍️ Multimodal Retail Assistant")

st.markdown("""
### AI-powered Fashion Discovery using Computer Vision, Retrieval-Augmented Generation (RAG), Vector Search and Large Language Models
""")

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
    st.metric("Search", "Semantic + Visual")

with c2:
    st.metric("Architecture", "RAG")

with c3:
    st.metric("AI Modules", "4")

with c4:
    st.metric("Status", "🟢 Live")

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

st.write("""
The **Multimodal Retail Assistant** is an AI-powered fashion discovery platform that enables users to search for products using natural language and visual inputs instead of relying solely on keyword-based search.

The application combines Computer Vision, FAISS Vector Search, Retrieval-Augmented Generation (RAG), and Large Language Models to deliver highly relevant, context-aware product recommendations.

Designed with both technical implementation and product thinking in mind, the solution demonstrates how modern AI can improve product discovery, reduce search friction, and create a more engaging shopping experience.
""")

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
🔍 FAISS
</span>

<span style="
background:#ff9800;
color:white;
padding:6px 12px;
border-radius:8px;
margin:4px;
display:inline-block;">
🖼 OpenCLIP
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

st.success("✅ Phase 1 — Semantic Product Search")
st.success("✅ Phase 2 — AI Shopping Assistant")
st.success("✅ Phase 3 — Product Comparison")
st.success("✅ Phase 4 — Analytics Dashboard")

st.warning("🚧 Phase 5 — Voice Search")
st.warning("🚧 Phase 6 — Recommendation Engine")

st.divider()

# -------------------------------------------------------
# Live Demo
# -------------------------------------------------------

st.header("Live Demo")

st.markdown(
    """
<div style="
display:flex;
align-items:center;
gap:10px;
margin-bottom:15px;
">

<span style="
height:14px;
width:14px;
background-color:#22c55e;
border-radius:50%;
display:inline-block;
"></span>

<span style="
font-size:20px;
font-weight:600;
">
Live on Streamlit Cloud
</span>

</div>
""",
    unsafe_allow_html=True,
)

st.write("""
Experience the **Multimodal Retail Assistant** in action. Search products using
natural language, upload fashion images for visual search, compare products,
and explore AI-powered recommendations powered by Retrieval-Augmented Generation (RAG).
""")

col1, col2 = st.columns(2)

with col1:
    st.link_button(
        "Launch Live Demo",
        "https://multimodal-rag-pro-search.streamlit.app/",
        use_container_width=True,
    )

with col2:
    st.link_button(
        "GitHub Repository",
        "https://github.com/Noira-Khan/multimodal-rag-product-search",
        use_container_width=True,
    )

st.info(
    "💡 Try uploading a fashion image or searching for products using natural language to experience semantic search, AI-powered recommendations, product comparison, and analytics."
)

st.divider()