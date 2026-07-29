# import streamlit as st

# st.set_page_config(
#     page_title="Employee Attrition Platform",
#     page_icon="📊",
#     layout="wide"
# )

# st.markdown("""
# <style>

# .block-container{
#     max-width:97%;
#     padding-top:1rem;
# }

# </style>
# """, unsafe_allow_html=True)

# # ---------------------------
# # TITLE
# # ---------------------------

# st.title("📊 Employee Attrition & Retention Analytics Platform")

# st.markdown("""
# This platform helps HR teams identify employees at risk of attrition,
# understand key drivers behind employee turnover, and take proactive
# retention actions.
# """)

# # ---------------------------
# # KPI CARDS
# # ---------------------------

# col1, col2, col3, col4 = st.columns(4)

# with col1:
#     st.metric("Dataset Size", "74,498")

# with col2:
#     st.metric("Final Model", "Random Forest")

# with col3:
#     st.metric("Accuracy", "74.98%")

# with col4:
#     st.metric("ROC-AUC", "84.28%")

# st.divider()

# # ---------------------------
# # BUSINESS PROBLEM
# # ---------------------------

# st.header("🎯 Business Problem")

# st.write("""
# Employee attrition leads to:

# - Increased recruitment costs
# - Loss of organizational knowledge
# - Reduced productivity
# - Additional training expenses

# This platform predicts employee attrition risk and helps HR teams
# implement targeted retention strategies.
# """)

# st.divider()

# # ---------------------------
# # PROJECT FLOW
# # ---------------------------

# st.header("🔄 Project Workflow")

# st.write("""
# Employee Data
# → Data Cleaning
# → Feature Engineering
# → Random Forest Model
# → Attrition Probability
# → Risk Segmentation
# → HR Recommendations
# """)

# import streamlit as st

# # =====================================================
# # PAGE CONFIG
# # =====================================================

# st.set_page_config(
#     page_title="Employee Attrition Platform",
#     layout="wide"
# )

# # =====================================================
# # CARD CSS
# # =====================================================

# st.markdown("""
# <style>

# .card {
#     background-color: #1F2937;
#     padding: 24px;
#     border-radius: 12px;
#     border-left: 4px solid #7C93C3;
#     margin-bottom: 20px;
# }

# .card-title {
#     font-size: 24px;
#     font-weight: 700;
#     margin-bottom: 12px;
# }

# </style>
# """, unsafe_allow_html=True)

# # =====================================================
# # TITLE
# # =====================================================

# st.title("📊 Employee Attrition & Retention Analytics Platform")

# st.markdown("""
# Machine Learning powered HR Analytics platform designed to predict employee attrition,
# identify high-risk employees, and support proactive retention strategies.
# """)

# st.divider()

# # =====================================================
# # KPI SECTION
# # =====================================================

# col1, col2, col3, col4 = st.columns(4)

# with col1:
#     st.metric(
#         "Employees",
#         "74,498"
#     )

# with col2:
#     st.metric(
#         "Accuracy",
#         "74.98%"
#     )

# with col3:
#     st.metric(
#         "ROC-AUC",
#         "84.28%"
#     )

# with col4:
#     st.metric(
#         "Final Model",
#         "Random Forest"
#     )

# st.divider()

# # =====================================================
# # EXECUTIVE SUMMARY
# # =====================================================

# st.markdown("""
# <div class="card">

# <div class="card-title">
# 📌 Executive Summary
# </div>

# This platform predicts employee attrition using Machine Learning and classifies employees into risk categories based on their likelihood of leaving the organization.

# The system enables HR teams to identify high-risk employees early and implement targeted retention strategies before attrition occurs.

# </div>
# """, unsafe_allow_html=True)

# # =====================================================
# # KEY CAPABILITIES
# # =====================================================

# st.markdown("""
# <div class="card">

# <div class="card-title">
# 🚀 Key Capabilities
# </div>

# <ul style="line-height:1.8">

# <li><b>Employee Attrition Prediction</b> using a trained Random Forest model.</li>

# <li><b>Risk Segmentation</b> into Low, Medium and High Risk employee groups.</li>

# <li><b>Feature Importance Analysis</b> to identify key attrition drivers.</li>

# <li><b>HR Recommendations</b> tailored to employee risk profiles.</li>

# <li><b>Interactive Analytics Dashboard</b> for workforce insights.</li>

# </ul>

# </div>
# """, unsafe_allow_html=True)

# # =====================================================
# # BUSINESS VALUE
# # =====================================================

# st.markdown("""
# <div class="card">

# <div class="card-title">
# 💼 Business Value
# </div>

# <ul style="line-height:1.8">

# <li>Reduce employee turnover and replacement costs.</li>

# <li>Improve workforce planning and retention initiatives.</li>

# <li>Support proactive HR interventions.</li>

# <li>Increase employee engagement and satisfaction.</li>

# <li>Enable data-driven decision making.</li>

# </ul>

# </div>
# """, unsafe_allow_html=True)

# # =====================================================
# # FOOTER
# # =====================================================

# st.caption(
#     "Developed using Python, Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn, Joblib and Streamlit."
# )

import streamlit as st

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Employee Attrition Platform",
    layout="wide"
)

# =====================================================
# CSS
# =====================================================

st.markdown("""
<style>

# .block-container{
#     max-width:95% !important;
#     padding-top:2rem;
#     padding-left:2rem;
#     padding-right:2rem;
# }
            
.block-container{
    max-width:85% !important;
    padding-top:2rem;
    margin-left:auto;
    margin-right:auto;
}

/* Summary Card */

.summary-card{
    background-color:#1F2937;
    padding:24px;
    border-radius:12px;
    border-left:4px solid #7C93C3;
    margin-bottom:20px;
}

.summary-title{
    font-size:28px;
    font-weight:700;
    margin-bottom:12px;
}

/* Feature Cards */

.card{
    background-color:#1F2937;
    padding:22px;
    border-radius:12px;
    border-left:4px solid #7C93C3;
    min-height:180px;
    margin-bottom:20px;
}

.card-title{
    font-size:24px;
    font-weight:700;
    margin-bottom:12px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# TITLE
# =====================================================

st.title("📊 Employee Attrition & Retention Analytics Platform")

st.markdown("""
Machine Learning powered HR Analytics platform designed to predict employee attrition,
identify high-risk employees, and support proactive retention strategies.
""")

st.divider()

# =====================================================
# KPI SECTION
# =====================================================

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric(
        "Employees",
        "74,498"
    )

with col2:
    st.metric(
        "Accuracy",
        "74.98%"
    )

with col3:
    st.metric(
        "ROC-AUC",
        "84.28%"
    )

with col4:
    st.metric(
        "Final Model",
        "Random Forest"
    )

st.divider()

# =====================================================
# EXECUTIVE SUMMARY
# =====================================================

st.markdown("""
<div class="summary-card">

<div class="summary-title">
📌 Executive Summary
</div>

This platform predicts employee attrition using Machine Learning,
segments employees into risk categories,
and generates actionable retention recommendations.

HR teams can proactively identify employees at risk,
reduce turnover,
and improve workforce stability through data-driven decision making.

</div>
""", unsafe_allow_html=True)

st.divider()

# =====================================================
# EXPLORE PLATFORM
# =====================================================

st.subheader("🧭 Explore the Platform")

col1,col2,col3 = st.columns(3)

with col1:

    st.markdown("""
    <div class="card">

    <div class="card-title">
    📈 Dataset Insights
    </div>

    Explore employee trends,
    attrition patterns,
    and workforce analytics.

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="card">

    <div class="card-title">
    🤖 Model Performance
    </div>

    Compare ML models and understand why Random Forest was selected.

    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown("""
    <div class="card">

    <div class="card-title">
    🔍 Feature Importance
    </div>

    Discover the strongest drivers of employee attrition.

    </div>
    """, unsafe_allow_html=True)

col4,col5,col6 = st.columns(3)

with col4:

    st.markdown("""
    <div class="card">

    <div class="card-title">
    ⚠️ Risk Analytics
    </div>

    Analyze Low, Medium,
    and High Risk employee groups.

    </div>
    """, unsafe_allow_html=True)

with col5:

    st.markdown("""
    <div class="card">

    <div class="card-title">
    🔮 Attrition Predictor
    </div>

    Predict attrition probability
    for individual employees.

    </div>
    """, unsafe_allow_html=True)

with col6:

    st.markdown("""
    <div class="card">

    <div class="card-title">
    💡 Recommendations
    </div>

    Review retention strategies
    and HR intervention plans.

    </div>
    """, unsafe_allow_html=True)