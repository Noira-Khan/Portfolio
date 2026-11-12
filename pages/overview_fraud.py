import streamlit as st

from components.layout import Layout
from components.navbar import navbar
from components.project_card import project_links
from data.projects import by_slug

project = by_slug("fraud")

Layout.setup(page_title=project["title"], page_icon="🛡️")
navbar()

# -------------------------------------------------------
# Hero Section
# -------------------------------------------------------

st.title(project["title"])

st.markdown("""
### A card payment is Allowed or sent to Review. Review does not decline the card.
""")

st.write(project["summary"])
project_links(project)

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
Finance Shield scores one card payment, or a small file of payments, on this computer.
The saved model is already in the repository. The original public dataset is not required to run the desk.

The screen leads with precision, recall, and F1 at a 95% cutoff. Accuracy is shown as a number that stays high even when fraud is missed, so it is not the decision metric.
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

st.write(project["decision"])

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
1. A single payment, or a row in a batch file, supplies `Time`, `V1`–`V28`, and `Amount`.

2. The saved XGBoost model returns a score.

3. Under 95% the desk says Allow. At 95% or above it says Review and files the case on the local queue.

4. At Review, the phone alert and the email are a preview. Nothing is sent. `blocks_payment` stays false.

5. The model record page shows the holdout precision, recall, and F1. It does not lead with accuracy.
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

st.header("What the holdout supports")

for item in project["proof"]:
    st.markdown(f"- {item}")

st.caption(
    "These figures are the holdout notes in the Finance Shield README. "
    "They are not a production loss estimate."
)

st.divider()

# -------------------------------------------------------
# Future Roadmap
# -------------------------------------------------------

st.header("Future Enhancements")

st.markdown("""
Already in the repository: the Streamlit desk, the FastAPI `POST /predict` endpoint, the saved model, and the operating-rules page.

Not in this build: SHAP explanations, a live card network, a message that is actually sent, or a claim about money saved.
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
project_links(project)