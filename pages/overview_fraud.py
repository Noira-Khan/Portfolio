import streamlit as st

from components.navbar import navbar

# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------

st.set_page_config(
    page_title="Finance Shield AI",
    page_icon="🛡️",
    layout="wide"
)

navbar()

# -------------------------------------------------------
# Hero Section
# -------------------------------------------------------

st.title("🛡️ Finance Shield AI")

st.markdown("""
### AI-powered Credit Card Fraud Detection using Machine Learning
""")

st.image(
    "products/fraud_detection/fraud_cover.jpeg",
    use_container_width=True
)

st.divider()

# -------------------------------------------------------
# Project Overview
# -------------------------------------------------------

st.header("Project Overview")

st.write("""
Finance Shield AI is an end-to-end machine learning application built to detect
potentially fraudulent credit card transactions in real time.

The project combines data preprocessing, feature engineering, model training,
and an interactive Streamlit interface into a complete fraud detection workflow.

Rather than focusing only on model accuracy, the goal was to build a practical
product that demonstrates how AI can support fraud analysts with faster,
more informed decision-making through an intuitive user experience.
""")

st.divider()

# -------------------------------------------------------
# Business Problem
# -------------------------------------------------------

st.header("Business Problem")

st.write("""
Financial institutions process millions of card transactions every day, making
manual fraud detection impossible at scale.

Traditional rule-based systems often struggle to distinguish genuine purchases
from fraudulent ones, generating unnecessary alerts and frustrating customers.

The challenge is to accurately identify fraudulent transactions while reducing
false positives and improving operational efficiency.
""")

st.divider()

# -------------------------------------------------------
# Solution
# -------------------------------------------------------

st.header("Solution")

st.write("""
Finance Shield AI uses a supervised machine learning model to evaluate
transaction characteristics and estimate the likelihood of fraud.

Users simply enter transaction details through the application interface and
receive an instant prediction along with a clear risk assessment.

The solution demonstrates how machine learning can support fraud analysts by
providing faster, more consistent, and data-driven decisions.
""")

st.divider()

# -------------------------------------------------------
# System Architecture
# -------------------------------------------------------

st.header("System Architecture")

st.write("""
The application follows a modular architecture where transaction data passes
through preprocessing, feature engineering, the trained machine learning model,
and finally into an intuitive user interface for prediction and analysis.
""")

st.image(
    "products/fraud_detection/screenshots/system_architecture.png",
    use_container_width=True
)

st.divider()

# -------------------------------------------------------
# How the System Works
# -------------------------------------------------------

st.header("How the System Works")

st.markdown("""
1. User enters transaction details.

2. Input data is preprocessed.

3. Engineered features are generated.

4. The trained model predicts fraud probability.

5. Results are displayed with a business-friendly risk assessment.
""")

st.divider()

# -------------------------------------------------------
# Application Screenshots
# -------------------------------------------------------

st.header("Application Walkthrough")

st.subheader("Fraud Prediction Engine")

st.write("""
The prediction interface allows users to submit transaction information and
receive an instant fraud prediction.
""")

st.image(
    "products/fraud_detection/screenshots/fraud_engine.png",
    use_container_width=True
)

st.subheader("Executive Dashboard")

st.write("""
The dashboard provides a high-level overview of predictions, enabling business
users to monitor fraud trends and evaluate model outcomes.
""")

st.image(
    "products/fraud_detection/screenshots/executive_dashboard.png",
    use_container_width=True
)

st.subheader("Model Performance")

st.write("""
The model was evaluated using standard classification metrics to ensure strong
fraud detection performance while minimizing false positives.
""")

st.image(
    "products/fraud_detection/screenshots/model_performance.png",
    use_container_width=True
)

st.divider()

# -------------------------------------------------------
# Machine Learning Pipeline
# -------------------------------------------------------

st.header("Machine Learning Pipeline")

st.markdown("""
- Data Loading
- Exploratory Data Analysis
- Data Cleaning
- Feature Engineering
- Train/Test Split
- Handling Class Imbalance
- Model Training
- Hyperparameter Tuning
- Model Evaluation
- Model Serialization
- Streamlit Deployment
""")

st.divider()

# -------------------------------------------------------
# Tech Stack
# -------------------------------------------------------

st.header("Technology Stack")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
### Frontend

- Streamlit

### Backend

- Python
- FastAPI
""")

with col2:

    st.markdown("""
### Machine Learning

- Scikit-Learn
- XGBoost

### Libraries

- Pandas
- NumPy
- Joblib
""")

st.divider()

# -------------------------------------------------------
# Product Thinking
# -------------------------------------------------------

st.header("Product Thinking")

st.write("""
This project was approached as a complete AI product rather than only a machine
learning model.

Alongside predictive performance, the focus was on designing an application
that is intuitive for business users, easy to maintain, and capable of
supporting real-world fraud investigation workflows.

Key product decisions included:

• Simple user experience

• Fast prediction response time

• Clear presentation of results

• Modular application architecture

• Easy deployment using Streamlit

• Scalable design for future enhancements
""")

st.divider()

# -------------------------------------------------------
# Business Impact
# -------------------------------------------------------

st.header("Business Impact")

st.success("Reduce fraud-related financial losses")

st.success("Improve fraud investigation speed")

st.success("Lower false-positive rates")

st.success("Improve customer experience")

st.success("Support data-driven business decisions")

st.success("Increase operational efficiency")

st.divider()

# -------------------------------------------------------
# Future Roadmap
# -------------------------------------------------------

st.header("Future Enhancements")

st.markdown("""
- Explainable AI using SHAP

- REST API with FastAPI

- Real-time fraud scoring

- Human-in-the-loop review workflow

- Continuous model retraining

- Cloud deployment (AWS)

- Model monitoring and drift detection

- Fraud analytics dashboard
""")

st.image(
    "products/fraud_detection/screenshots/product_roadmap.png",
    use_container_width=True
)

st.divider()

# -------------------------------------------------------
# Live Demo
# -------------------------------------------------------

st.header("Explore the Project")

col1, col2 = st.columns(2)

with col1:

    st.link_button(
        "Launch Streamlit Demo",
        "https://financeshieldai.streamlit.app/"
    )

with col2:

    st.link_button(
        "GitHub Repository",
        "https://github.com/Noira-Khan/ML-Fraud-Detection-Project"
    )