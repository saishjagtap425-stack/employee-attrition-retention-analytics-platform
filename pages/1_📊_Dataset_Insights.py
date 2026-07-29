import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from style import apply_global_style
apply_global_style()

# ==================================================
# PAGE CONFIG
# ==================================================

st.title("📊 Dataset Insights")

df = pd.read_csv("attrition_dataset.csv")

# ==================================================
# EXECUTIVE SUMMARY
# ==================================================

st.success("""
### Executive Summary

• Attrition Rate : 47.5%

• Dataset is balanced and suitable for machine learning.

• Major drivers of attrition identified through EDA:

    - Work-Life Balance
    - Job Satisfaction
    - Company Reputation
    - Career Growth Opportunities (Promotions)

These factors should be prioritized by HR teams to improve retention.
""")

st.divider()

# ==================================================
# ATTRITION DISTRIBUTION
# ==================================================

st.subheader("📌 Employee Attrition Distribution")

col1, col2 = st.columns(2)

stayed = len(df[df["Attrition"] == "Stayed"])
left = len(df[df["Attrition"] == "Left"])
total = len(df)

with col1:
    st.metric(
        "Employees Stayed",
        f"{stayed:,}"
    )

with col2:
    st.metric(
        "Employees Left",
        f"{left:,}"
    )

st.progress(left / total)

st.info(f"""
### Business Insight

The dataset is relatively balanced.

• Stayed : {(stayed/total)*100:.1f}%

• Left : {(left/total)*100:.1f}%

A balanced dataset reduces model bias and improves prediction reliability.
""")

st.divider()

# ==================================================
# WORK LIFE BALANCE
# ==================================================

st.subheader("1️⃣ Work-Life Balance vs Attrition")

fig, ax = plt.subplots(figsize=(7,4))

sns.countplot(
    data=df,
    x="Work-Life Balance",
    hue="Attrition",
    order=["Poor","Fair","Good","Excellent"],
    palette=["#4C78A8","#E45756"],
    ax=ax
)

ax.set_xlabel("")
ax.set_ylabel("Employees")

st.pyplot(fig)

st.info("""
### Business Insight

Employees reporting Poor or Fair work-life balance show noticeably higher attrition.

Employees with Good or Excellent work-life balance are significantly more likely to stay.

### Recommendation

• Flexible work arrangements

• Hybrid work options

• Wellness initiatives

• Better workload management
""")

st.divider()

# ==================================================
# JOB SATISFACTION
# ==================================================

st.subheader("2️⃣ Job Satisfaction vs Attrition")

fig, ax = plt.subplots(figsize=(7,4))

sns.countplot(
    data=df,
    x="Job Satisfaction",
    hue="Attrition",
    order=["Low","Medium","High","Very High"],
    palette=["#4C78A8","#E45756"],
    ax=ax
)

ax.set_xlabel("")
ax.set_ylabel("Employees")

st.pyplot(fig)

st.info("""
### Business Insight

Employees with low job satisfaction are more likely to leave the organization.

Higher satisfaction levels are associated with stronger employee retention.

### Recommendation

• Employee engagement programs

• Regular feedback sessions

• Career development planning

• Better manager-employee communication
""")

st.divider()

# ==================================================
# COMPANY REPUTATION
# ==================================================

st.subheader("3️⃣ Company Reputation vs Attrition")

fig, ax = plt.subplots(figsize=(7,4))

sns.countplot(
    data=df,
    x="Company Reputation",
    hue="Attrition",
    order=["Poor","Fair","Good","Excellent"],
    palette=["#4C78A8","#E45756"],
    ax=ax
)

ax.set_xlabel("")
ax.set_ylabel("Employees")

st.pyplot(fig)

st.info("""
### Business Insight

Employees who perceive the company positively are more likely to remain.

Negative perceptions correlate with higher attrition rates.

### Recommendation

• Strengthen employer branding

• Improve workplace culture

• Increase transparency

• Enhance employee experience initiatives
""")

st.divider()

# ==================================================
# PROMOTIONS
# ==================================================

st.subheader("4️⃣ Promotions vs Attrition")

fig, ax = plt.subplots(figsize=(7,4))

sns.boxplot(
    data=df,
    x="Attrition",
    y="Number of Promotions",
    palette=["#6BAED6","#F28E8E"],
    ax=ax
)

ax.set_xlabel("")
ax.set_ylabel("Number of Promotions")

st.pyplot(fig)

st.info("""
### Business Insight

Employees who stay generally receive more promotions than employees who leave.

Career growth opportunities appear to play an important role in retention.

### Recommendation

• Transparent promotion policies

• Internal mobility programs

• Leadership development pathways

• Defined career progression plans
""")

st.divider()

# ==================================================
# FINAL CONCLUSION
# ==================================================

st.success("""
## 🎯 Final Conclusion

Exploratory Data Analysis indicates that employee attrition is primarily influenced by:

1. Work-Life Balance
2. Job Satisfaction
3. Company Reputation
4. Career Growth Opportunities

Organizations focusing on these areas are more likely to improve retention and reduce employee turnover.
""")