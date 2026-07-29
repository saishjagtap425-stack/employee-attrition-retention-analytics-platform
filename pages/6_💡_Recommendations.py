# import streamlit as st

# st.title("💡 Employee Retention Recommendations")

# st.markdown("""
# This section provides actionable recommendations based on insights generated from the Employee Attrition Prediction Model.
# """)

# # ---------------------------------------------------
# # High Risk Employees
# # ---------------------------------------------------

# st.subheader("🔴 High Risk Employees")

# st.error("""
# Employees identified as High Risk should be prioritized immediately.
# """)

# st.markdown("""
# ### Recommended Actions

# ✅ Conduct one-on-one HR discussions

# ✅ Review compensation and benefits

# ✅ Create personalized career growth plans

# ✅ Improve employee recognition programs

# ✅ Monitor workload and overtime
# """)

# # ---------------------------------------------------
# # Medium Risk Employees
# # ---------------------------------------------------

# st.subheader("🟠 Medium Risk Employees")

# st.warning("""
# Employees in this group show moderate attrition risk and should be monitored regularly.
# """)

# st.markdown("""
# ### Recommended Actions

# ✅ Monthly check-ins

# ✅ Skill development programs

# ✅ Recognition and rewards

# ✅ Leadership mentoring

# ✅ Flexible work arrangements
# """)

# # ---------------------------------------------------
# # Low Risk Employees
# # ---------------------------------------------------

# st.subheader("🟢 Low Risk Employees")

# st.success("""
# These employees are currently stable.
# """)

# st.markdown("""
# ### Recommended Actions

# ✅ Continue engagement programs

# ✅ Offer growth opportunities

# ✅ Encourage innovation

# ✅ Maintain work-life balance

# ✅ Periodic satisfaction surveys
# """)

# # ---------------------------------------------------
# # Key Findings
# # ---------------------------------------------------

# st.subheader("📊 Key Findings From Analysis")

# st.info("""
# Our analysis indicates that attrition is strongly associated with:

# • Poor Work-Life Balance

# • Lower Job Satisfaction

# • Long Distance from Home

# • Lower Job Levels

# • Fewer Years at Company

# • Lack of Recognition

# • Limited Career Growth Opportunities
# """)

# # ---------------------------------------------------
# # Business Impact
# # ---------------------------------------------------

# st.subheader("🏢 Business Impact")

# st.markdown("""
# Reducing employee attrition can help organizations:

# 💰 Reduce recruitment costs

# 📈 Improve productivity

# 🧠 Retain organizational knowledge

# 🤝 Improve employee morale

# 🚀 Increase long-term business growth
# """)

# # ---------------------------------------------------
# # Final Recommendation
# # ---------------------------------------------------

# st.subheader("🎯 Strategic Recommendation")

# st.success("""
# Focus retention efforts on employees classified as High Risk.

# Implement targeted interventions related to:

# • Work-Life Balance

# • Recognition Programs

# • Career Development

# • Compensation Review

# • Flexible Working Policies

# These initiatives can significantly reduce employee turnover and improve workforce stability.
# """)

import streamlit as st
import pandas as pd

from style import apply_global_style
apply_global_style()

st.title("Employee Retention Recommendations")

st.markdown("""
This section provides strategic recommendations derived from the
Employee Attrition Prediction Model and risk segmentation analysis.
""")

# =====================================================
# EXECUTIVE SUMMARY
# =====================================================

st.markdown("""
<div style="
background-color:#1F2937;
padding:20px;
border-radius:12px;
border-left:4px solid #7C93C3;
margin-bottom:20px;
">

<h3>📌 Executive Summary</h3>

<p>
Analysis indicates that employee attrition is primarily driven by:
</p>

<ul>
<li><b>Work-Life Balance</b></li>
<li><b>Job Satisfaction</b></li>
<li><b>Career Growth Opportunities</b></li>
<li><b>Distance From Home</b></li>
<li><b>Employee Recognition</b></li>
</ul>

<p>
HR teams should prioritize retention efforts around these areas to
reduce employee turnover and improve workforce stability.
</p>

</div>
""", unsafe_allow_html=True)

# =====================================================
# PRIORITY MATRIX
# =====================================================

st.subheader("Priority Action Matrix")

priority_df = pd.DataFrame({
    "Priority": [
        "High",
        "High",
        "Medium",
        "Medium",
        "Low"
    ],
    "Recommendation": [
        "Career Growth Programs",
        "Work-Life Balance Initiatives",
        "Recognition Programs",
        "Flexible Work Arrangements",
        "Employee Satisfaction Surveys"
    ],
    "Expected Impact": [
        "High",
        "High",
        "Medium",
        "Medium",
        "Low"
    ]
})

st.dataframe(
    priority_df,
    use_container_width=True,
    hide_index=True
)

st.divider()

# =====================================================
# HIGH RISK
# =====================================================

with st.expander("🔴 High Risk Employees", expanded=True):

    st.markdown("""
Employees identified as High Risk should be prioritized immediately.

### Recommended Actions

✅ Conduct one-on-one HR discussions

✅ Review compensation and benefits

✅ Create personalized career growth plans

✅ Improve employee recognition programs

✅ Monitor workload and overtime

### Objective

Reduce immediate attrition risk and retain critical talent.
""")

# =====================================================
# MEDIUM RISK
# =====================================================

with st.expander("🟡 Medium Risk Employees"):

    st.markdown("""
Employees in this segment require proactive engagement and monitoring.

### Recommended Actions

✅ Monthly manager check-ins

✅ Skill development initiatives

✅ Recognition and rewards programs

✅ Leadership mentoring

✅ Flexible work arrangements

### Objective

Prevent migration into the High Risk category.
""")

# =====================================================
# LOW RISK
# =====================================================

with st.expander("🟢 Low Risk Employees"):

    st.markdown("""
These employees currently demonstrate strong retention potential.

### Recommended Actions

✅ Continue engagement programs

✅ Offer growth opportunities

✅ Encourage innovation and participation

✅ Maintain work-life balance

✅ Periodic satisfaction surveys

### Objective

Sustain long-term employee satisfaction and loyalty.
""")

st.divider()

# =====================================================
# KEY FINDINGS
# =====================================================

st.markdown("""
<div style="
background-color:#1F2937;
padding:20px;
border-radius:12px;
border-left:4px solid #7C93C3;
margin-bottom:20px;
">

<h3>📈 Key Findings From Analysis</h3>

<ul>
<li>Poor Work-Life Balance is strongly associated with attrition.</li>
<li>Employees with lower Job Satisfaction are more likely to leave.</li>
<li>Long commuting distances increase turnover risk.</li>
<li>Lower Job Levels experience higher attrition rates.</li>
<li>Limited career growth opportunities impact retention.</li>
<li>Employee recognition contributes positively to workforce stability.</li>
</ul>

</div>
""", unsafe_allow_html=True)

# =====================================================
# BUSINESS IMPACT
# =====================================================

st.subheader("Business Impact")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Recruitment Costs",
        "↓"
    )

with col2:
    st.metric(
        "Productivity",
        "↑"
    )

with col3:
    st.metric(
        "Retention",
        "↑"
    )

with col4:
    st.metric(
        "Workforce Stability",
        "↑"
    )

st.markdown("""
Reducing employee attrition enables organizations to lower hiring costs,
improve productivity, preserve organizational knowledge, and strengthen
long-term business growth.
""")