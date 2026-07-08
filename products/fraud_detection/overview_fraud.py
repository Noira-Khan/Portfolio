import streamlit as st

from components.navbar import navbar

st.set_page_config(
    page_title="Finance Shield AI",
    page_icon="🛡️",
    layout="wide"
)

navbar()

# -----------------------------
# Hero
# -----------------------------

st.title("🛡️ Finance Shield AI")

st.markdown("""
### AI-powered Credit Card Fraud Detection using Machine Learning
""")

st.image("products/fraud_detection/fraud_cover.jpeg", use_container_width=True)

st.divider()

# -----------------------------
# Project Overview
# -----------------------------

st.header("📌 Project Overview")

st.write("""
Finance Shield AI is an intelligent fraud detection platform designed to identify
potentially fraudulent credit card transactions in real time.

The solution combines machine learning with an intuitive Streamlit interface,
allowing users to quickly evaluate transaction risk while understanding the
factors influencing the prediction.

The project demonstrates how AI can help financial institutions reduce fraud,
improve operational efficiency, and support faster risk-based decision making.
""")

st.divider()

# -----------------------------
# Business Problem
# -----------------------------

st.header("💼 Business Problem")

st.write("""
Financial institutions process millions of transactions every day, making it
extremely difficult to manually identify fraudulent activity.

Traditional rule-based systems often generate high false positives,
leading to unnecessary transaction blocks and poor customer experience.

Businesses need a scalable solution capable of detecting suspicious
transactions accurately while minimizing disruptions for legitimate users.
""")

st.divider()

# -----------------------------
# Solution
# -----------------------------

st.header("💡 Solution")

st.write("""
Finance Shield AI uses a trained machine learning model to analyze transaction
attributes and estimate the probability of fraud.

The application provides:

- Real-time fraud prediction
- Instant risk assessment
- Simple user-friendly interface
- Fast model inference
- Explainable prediction workflow
- Interactive dashboard for decision support

The system demonstrates how AI can augment fraud analysts by providing
rapid, data-driven insights during transaction evaluation.
""")

st.divider()

# -----------------------------
# Key Features
# -----------------------------

st.header("✨ Key Features")

col1, col2 = st.columns(2)

with col1:
    st.success("Real-time Fraud Prediction")
    st.success("Machine Learning Pipeline")
    st.success("FastAPI Backend")
    st.success("Interactive Streamlit UI")

with col2:
    st.success("Transaction Risk Assessment")
    st.success("Feature Engineering")
    st.success("Model Inference")
    st.success("Business-friendly Dashboard")

st.divider()

# -----------------------------
# Tech Stack
# -----------------------------

st.header("🛠️ Tech Stack")

st.markdown("""
- Python
- Streamlit
- FastAPI
- Scikit-learn
- Pandas
- NumPy
- Joblib
- Machine Learning
""")

st.divider()

# -----------------------------
# Product Thinking
# -----------------------------

st.header("🧠 Product Thinking")

st.write("""
The objective of this project was to create more than a machine learning model.

The focus was on designing a practical fraud detection product that balances
accuracy, usability, and business value.

Key product considerations included:

- Simple workflow for analysts
- Fast prediction response time
- Easy deployment
- Clear presentation of results
- Scalable architecture
- Intuitive user experience
""")

st.divider()

# -----------------------------
# Business Impact
# -----------------------------

st.header("📈 Business Impact")

st.write("""
An AI-powered fraud detection system can provide significant operational benefits.

Potential business outcomes include:

- Faster fraud detection
- Reduced financial losses
- Lower false-positive rates
- Improved customer trust
- Increased operational efficiency
- Better decision support for fraud teams
""")

st.divider()

# -----------------------------
# Future Roadmap
# -----------------------------

st.header("🚀 Future Enhancements")

st.markdown("""
- Explainable AI (SHAP/LIME)
- Real-time streaming predictions
- Fraud monitoring dashboard
- Customer risk profiling
- Continuous model retraining
- Cloud deployment
- Human-in-the-loop review workflow
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
        "https://financeshieldai.streamlit.app/"
    )

with col2:
    st.link_button(
        "💻 GitHub Repository",
        "https://github.com/Noira-Khan/ML-Fraud-Detection-Project"
    )