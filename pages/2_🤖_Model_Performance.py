import streamlit as st
import pandas as pd

from style import apply_global_style
apply_global_style()

st.title("🤖 Model Performance")

st.write("""
Different machine learning models were evaluated to identify the most effective solution for employee attrition prediction.
""")

st.markdown("""
<style>

.card {
    background-color: #1F2937;
    padding: 24px;
    border-radius: 12px;
    margin-bottom: 20px;
    border-left: 4px solid #7C93C3;
}

.card-title {
    font-size: 24px;
    font-weight: 700;
    margin-bottom: 12px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# MODEL COMPARISON
# =====================================================

st.subheader("📊 Model Comparison")

comparison_df = pd.DataFrame({
    "Model": [
        "Logistic Regression",
        "Decision Tree",
        "Random Forest"
    ],
    "Accuracy": [
        0.7375,
        0.7382,
        0.7498
    ],
    "Precision": [
        0.7275,
        0.7250,
        0.7379
    ],
    "Recall": [
        0.7149,
        0.7226,
        0.7335
    ],
    "F1 Score": [
        0.7211,
        0.7238,
        0.7357
    ]
})

st.dataframe(
    comparison_df,
    use_container_width=True,
    hide_index=True
)

st.divider()

# =====================================================
# SELECTED MODEL
# =====================================================

st.subheader("🏆 Selected Model - Random Forest")

st.success("""
Random Forest was selected as the final production model because it achieved the best overall balance between Accuracy, Precision, Recall and F1 Score.
""")


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Accuracy",
        "74.98%"
    )

with col2:
    st.metric(
        "Precision",
        "73.79%"
    )

with col3:
    st.metric(
        "Recall",
        "73.35%"
    )

with col4:
    st.metric(
        "F1 Score",
        "73.57%"
    )

st.divider()

# =====================================================
# GENERALIZATION PERFORMANCE
# =====================================================

st.subheader("📈 Generalization Performance")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Train Accuracy",
        "79.10%"
    )

with col2:
    st.metric(
        "Test Accuracy",
        "74.98%"
    )

st.info("""
The gap between training and testing accuracy is relatively small, indicating that the model generalizes well to unseen employee data and does not suffer from severe overfitting.
""")

st.divider()

# =====================================================
# CONFUSION MATRIX
# =====================================================

st.subheader("🎯 Confusion Matrix")

# REPLACE THESE VALUES WITH YOUR ACTUAL VALUES
TN = 5600
FP = 1100
FN = 900
TP = 5200

cm_df = pd.DataFrame(
    [
        [TN, FP],
        [FN, TP]
    ],
    columns=[
        "Predicted Stay",
        "Predicted Leave"
    ],
    index=[
        "Actual Stay",
        "Actual Leave"
    ]
)



st.dataframe(
    cm_df,
    use_container_width=True
)

st.info("""
The confusion matrix shows how effectively the model classifies employees who stay and employees who leave. A high number of correct predictions indicates strong predictive capability for employee attrition risk assessment.
""")

st.divider()

# # =====================================================
# # TOP FEATURES
# # =====================================================

# st.subheader("🔍 Most Influential Features")

# feature_df = pd.DataFrame({
#     "Rank":[1,2,3,4,5],
#     "Feature":[
#         "Job Level",
#         "Marital Status",
#         "Remote Work",
#         "Work-Life Balance",
#         "Distance from Home"
#     ]
# })

# st.dataframe(
#     feature_df,
#     use_container_width=True,
#     hide_index=True
# )

# st.info("""
# These variables contributed most strongly to the model's predictions and provide valuable insight into employee retention behaviour.
# """)

# st.divider()

# =====================================================
# WHY RANDOM FOREST
# =====================================================

# st.subheader("✅ Why Random Forest?")

# st.info("""
# • Highest Accuracy among evaluated models

# • Highest F1 Score

# • Strong Generalization Performance

# • Handles Non-Linear Relationships Effectively

# • Robust Against Noise and Outliers

# • Provides Reliable Attrition Predictions
# """)

# st.subheader("✅ Why Random Forest?")

st.markdown("""
<div class="card">

<div class="card-title">
✅ Why Random Forest?
</div>

<ul style="line-height:1.8; margin-top:10px;">

<li><b>Highest Accuracy</b> among all evaluated models.</li>

<li><b>Highest F1 Score</b>, providing a strong balance between Precision and Recall.</li>

<li>Demonstrated strong <b>Generalization Performance</b> on unseen employee data.</li>

<li>Effectively captures <b>complex and non-linear relationships</b> between HR attributes.</li>

<li>Robust against <b>noise and outliers</b> compared to individual decision trees.</li>

<li>Provides reliable and consistent predictions for <b>employee attrition risk assessment</b>.</li>

</ul>

</div>
""", unsafe_allow_html=True)

# st.divider()

# # =====================================================
# # BUSINESS VALUE
# # =====================================================

# st.subheader("💼 Business Value")

# st.info("""
# • Identify employees at risk of attrition early.

# • Support proactive retention planning.

# • Improve workforce stability.

# • Reduce employee replacement costs.

# • Enable data-driven HR decision making.

# • Improve long-term organizational performance.
# """)