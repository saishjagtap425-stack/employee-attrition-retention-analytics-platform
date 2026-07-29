import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from style import apply_global_style
apply_global_style()

st.title("🔍 Feature Importance")

st.markdown("""
<style>

.card {
    background-color: #1F2937;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 20px;
    border-left: 5px solid #3B82F6;
    border-left: 4px solid #7C93C3;
    border-left: 4px solid #64748B
}

.card-title {
    font-size: 22px;
    font-weight: bold;
    margin-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
This page highlights the most influential factors used by the Random Forest model
to predict employee attrition.
""")

# =====================================================
# FEATURE IMPORTANCE DATA
# =====================================================

feature_df = pd.DataFrame(
{
    "Feature":[
        "Job Level",
        "Single Employee",
        "Remote Work",
        "Work-Life Balance",
        "Distance from Home",
        "Married Employee",
        "Monthly Income",
        "Years at Company",
        "Company Tenure",
        "Age"
    ],

    "Importance":[
        0.195,
        0.115,
        0.100,
        0.080,
        0.060,
        0.052,
        0.045,
        0.041,
        0.039,
        0.037
    ]
}
)

# =====================================================
# CHART
# =====================================================

fig, ax = plt.subplots(figsize=(10, 5))

sns.barplot(
    data=feature_df,
    x="Importance",
    y="Feature",
    palette="Blues_r",
    ax=ax
)

ax.set_title(
    "Top Factors Influencing Employee Attrition",
    fontsize=15,
    fontweight="bold"
)

# ax.set_xlabel("Feature Importance Score")
# ax.set_ylabel("")

ax.set_xlabel(
    "Feature Importance Score",
    fontsize=14, 
    fontweight = "bold"
)

ax.set_ylabel(
    "Features",
    fontsize=14, 
    fontweight = "bold"
)

ax.tick_params(
    axis="y",
    labelsize=12.5
)

ax.tick_params(
    axis="x",
    labelsize=12.5
)

plt.tight_layout()

st.pyplot(
    fig,
    use_container_width=True
)

# =====================================================
# BUSINESS INSIGHTS
# =====================================================

# st.markdown("""
# <div class="card">

# <div class="card-title">
# 🔍 Business Insights
# </div>

# <ul style="line-height:1.8; margin-top:10px;">

# <li><b>Job Level</b> emerged as the most influential factor affecting employee attrition.</li>

# <li><b>Marital Status</b> and <b>Remote Work</b> arrangements show a strong relationship with employee retention.</li>

# <li>Employees reporting <b>Poor Work-Life Balance</b> are more likely to leave the organization.</li>

# <li>Long commuting distances increase attrition risk and may reduce employee satisfaction.</li>

# <li>Compensation contributes to retention, but <b>career progression</b> and <b>employee experience</b> appear to have a greater impact.</li>

# </ul>

# </div>
# """, unsafe_allow_html=True)

st.markdown("""
<div class="card">

<div class="card-title">
🔍 Business Insights
</div>

<ul style="line-height:1.8; margin-top:10px;">

<li><b>Job Level</b> emerged as the most influential factor affecting employee attrition.</li>

<li><b>Marital Status</b> and <b>Remote Work</b> arrangements show a strong relationship with employee retention.</li>

<li>Employees reporting <b>Poor Work-Life Balance</b> are more likely to leave the organization.</li>

<li>Long commuting distances increase attrition risk and may reduce employee satisfaction.</li>

<li>Compensation contributes to retention, but <b>career progression</b> and <b>employee experience</b> appear to have a greater impact.</li>

</ul>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">

<div class="card-title">
💼 Strategic Recommendations
</div>

<ul style="line-height:1.8; margin-top:10px;">

<li>Develop clear <b>career growth</b> and <b>promotion pathways</b> for employees.</li>

<li>Strengthen employee engagement programs and <b>work-life balance initiatives</b>.</li>

<li>Expand <b>hybrid and flexible work arrangements</b> where operationally feasible.</li>

<li>Implement targeted retention strategies for <b>high-risk employee groups</b>.</li>

<li>Leverage <b>predictive analytics</b> to proactively identify employees who may require intervention.</li>

<li>Invest in long-term <b>employee development</b>, mentoring, and skill enhancement programs.</li>

</ul>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">

<div class="card-title">
🎯 Interpretation
</div>

<p style="line-height:1.8; margin-top:10px;">

Feature importance scores represent the relative contribution of each variable to the
<b>Random Forest</b> model's predictions.


Features with higher importance values have a stronger influence on determining whether an employee is likely to
<b>remain with the organization</b> or <b>leave the company</b>.


These insights help HR teams understand the key drivers of attrition and prioritize retention strategies more effectively.

</p>

</div>
""", unsafe_allow_html=True)

# st.subheader("📊 Business Insights")

# st.info("""
# • Job Level emerged as the most influential factor affecting employee attrition.

# • Marital Status and Remote Work arrangements show a strong relationship with employee retention.

# • Employees reporting poor work-life balance are more likely to leave the organization.

# • Long commuting distances increase attrition risk and may reduce employee satisfaction.

# • Compensation contributes to retention, but career progression and employee experience appear to have a greater impact.
# """)

# =====================================================
# HR RECOMMENDATIONS
# =====================================================

# st.subheader("💼 Strategic Recommendations")

# st.info("""
# • Develop clear career growth and promotion pathways.

# • Strengthen employee engagement and work-life balance initiatives.

# • Expand flexible and hybrid work opportunities where feasible.

# • Provide targeted retention programs for high-risk employee groups.

# • Use predictive analytics to proactively identify employees who may require intervention.

# • Focus on long-term employee development rather than compensation alone.
# """)

# =====================================================
# MODEL INTERPRETATION
# =====================================================

# st.subheader("🎯 Interpretation")

# st.info("""
# Feature importance values indicate the relative contribution of each variable to the Random Forest model's predictions.

# Higher importance scores suggest that the feature plays a stronger role in determining whether an employee is likely to stay or leave.
# """)