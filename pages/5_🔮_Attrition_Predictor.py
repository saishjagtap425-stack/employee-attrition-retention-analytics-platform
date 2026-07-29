import streamlit as st
import pandas as pd
import joblib

from style import apply_global_style
apply_global_style()

st.title("🔮 Employee Attrition Predictor")

st.markdown("""
<style>

.high-risk {
    background-color: #4A1E1E;
    padding: 20px;
    border-radius: 12px;
    border-left: 5px solid #EF4444;
    margin-top: 15px;
}

.medium-risk {
    background-color: #4A3715;
    padding: 20px;
    border-radius: 12px;
    border-left: 5px solid #F59E0B;
    margin-top: 15px;
}

.low-risk {
    background-color: #183B2B;
    padding: 20px;
    border-radius: 12px;
    border-left: 5px solid #22C55E;
    margin-top: 15px;
}

</style>
""", unsafe_allow_html=True)

model = joblib.load("employee_attrition_model.pkl")

col1, col2 = st.columns(2)

with col1:

    age = st.number_input("Age",18,65,30)

    gender = st.selectbox(
        "Gender",
        ["Male","Female"]
    )

    years_company = st.number_input(
        "Years at Company",
        0,40,5
    )

    monthly_income = st.number_input(
        "Monthly Income",
        1000,50000,7000
    )

    performance_rating = st.selectbox(
        "Performance Rating",
        ["Low","Below Average","Average","High"]
    )

    overtime = st.selectbox(
        "Overtime",
        ["No","Yes"]
    )

    education = st.selectbox(
        "Education Level",
        [
            "High School",
            "Associate Degree",
            "Bachelor's Degree",
            "Master's Degree",
            "PhD"
        ]
    )

    dependents = st.number_input(
        "Number of Dependents",
        0,10,1
    )

    company_tenure = st.number_input(
        "Company Tenure",
        0,40,5
    )

    leadership = st.selectbox(
        "Leadership Opportunities",
        ["No","Yes"]
    )

    innovation = st.selectbox(
        "Innovation Opportunities",
        ["No","Yes"]
    )

with col2:

    distance = st.number_input(
        "Distance from Home",
        0,100,10
    )

    job_level = st.selectbox(
        "Job Level",
        ["Entry","Mid","Senior"]
    )

    remote_work = st.selectbox(
        "Remote Work",
        ["No","Yes"]
    )

    work_life = st.selectbox(
        "Work-Life Balance",
        ["Poor","Fair","Good","Excellent"]
    )

    job_satisfaction = st.selectbox(
        "Job Satisfaction",
        ["Low","Medium","High","Very High"]
    )

    company_size = st.selectbox(
        "Company Size",
        ["Small","Medium","Large"]
    )

    company_reputation = st.selectbox(
        "Company Reputation",
        ["Poor","Fair","Good","Excellent"]
    )

    recognition = st.selectbox(
        "Employee Recognition",
        ["Low","Medium","High","Very High"]
    )

    job_role = st.selectbox(
        "Job Role",
        [
            "Education",
            "Finance",
            "Healthcare",
            "Media",
            "Technology"
        ]
    )

    marital_status = st.selectbox(
        "Marital Status",
        [
            "Divorced",
            "Married",
            "Single"
        ]
    )

    promotions = st.number_input(
        "Number of Promotions",
        0,10,0
    )

if st.button("Predict Attrition Risk"):

    # ==========================
    # Binary Encoding
    # ==========================

    gender = 1 if gender == "Male" else 0

    overtime = 1 if overtime == "Yes" else 0
    remote_work = 1 if remote_work == "Yes" else 0
    leadership = 1 if leadership == "Yes" else 0
    innovation = 1 if innovation == "Yes" else 0

    # ==========================
    # Ordinal Encoding
    # ==========================

    work_life = {
        "Poor":0,
        "Fair":1,
        "Good":2,
        "Excellent":3
    }[work_life]

    job_satisfaction = {
        "Low":0,
        "Medium":1,
        "High":2,
        "Very High":3
    }[job_satisfaction]

    performance_rating = {
        "Low":0,
        "Below Average":1,
        "Average":2,
        "High":3
    }[performance_rating]

    education = {
        "High School":0,
        "Associate Degree":1,
        "Bachelor's Degree":2,
        "Master's Degree":3,
        "PhD":4
    }[education]

    job_level = {
        "Entry":0,
        "Mid":1,
        "Senior":2
    }[job_level]

    company_size = {
        "Small":0,
        "Medium":1,
        "Large":2
    }[company_size]

    company_reputation = {
        "Poor":0,
        "Fair":1,
        "Good":2,
        "Excellent":3
    }[company_reputation]

    recognition = {
        "Low":0,
        "Medium":1,
        "High":2,
        "Very High":3
    }[recognition]

    # ==========================
    # One Hot Encoding
    # ==========================

    job_finance = 0
    job_healthcare = 0
    job_media = 0
    job_technology = 0

    if job_role == "Finance":
        job_finance = 1

    elif job_role == "Healthcare":
        job_healthcare = 1

    elif job_role == "Media":
        job_media = 1

    elif job_role == "Technology":
        job_technology = 1

    married = 0
    single = 0

    if marital_status == "Married":
        married = 1

    elif marital_status == "Single":
        single = 1

    # ==========================
    # Create Input DataFrame
    # ==========================

    input_data = pd.DataFrame({

        "Age":[age],
        "Gender":[gender],
        "Years at Company":[years_company],
        "Monthly Income":[monthly_income],
        "Work-Life Balance":[work_life],
        "Job Satisfaction":[job_satisfaction],
        "Performance Rating":[performance_rating],
        "Number of Promotions":[promotions],
        "Overtime":[overtime],
        "Distance from Home":[distance],
        "Education Level":[education],
        "Number of Dependents":[dependents],
        "Job Level":[job_level],
        "Company Size":[company_size],
        "Company Tenure":[company_tenure],
        "Remote Work":[remote_work],
        "Leadership Opportunities":[leadership],
        "Innovation Opportunities":[innovation],
        "Company Reputation":[company_reputation],
        "Employee Recognition":[recognition],
        "Job Role_Finance":[job_finance],
        "Job Role_Healthcare":[job_healthcare],
        "Job Role_Media":[job_media],
        "Job Role_Technology":[job_technology],
        "Marital Status_Married":[married],
        "Marital Status_Single":[single]

    })

    # ==========================
    # Prediction
    # ==========================

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]

    # ==========================
    # Risk Classification
    # ==========================

    if probability < 0.4:
        risk = "🟢 Low Risk"

    elif probability < 0.7:
        risk = "🟠 Medium Risk"

    else:
        risk = "🔴 High Risk"

    # ==========================
    # Display Results
    # ==========================

    st.subheader("Prediction Result")

    st.metric(
        "Attrition Probability",
        f"{probability*100:.2f}%"
    )

    #st.success(f"Risk Level : {risk}")

    # ==========================
    # Recommendations
    # ==========================

    if probability >= 0.7:

     st.markdown(f"""
     <div class="high-risk">

     <h3>🔴 High Risk Employee</h3>

     <p>
     Attrition Probability: <b>{probability*100:.2f}%</b>
     </p>

     <h4>Recommended Actions</h4>

     <ul>
     <li>Immediate HR Discussion</li>
     <li>Review Compensation</li>
     <li>Improve Work-Life Balance</li>
     <li>Career Growth Planning</li>
     </ul>

     </div>
     """, unsafe_allow_html=True)

    elif probability >= 0.4:

     st.markdown(f"""
     <div class="medium-risk">

     <h3>🟠 Medium Risk Employee</h3>

     <p>
     Attrition Probability: <b>{probability*100:.2f}%</b>
     </p>

     <h4>Recommended Actions</h4>

     <ul>
     <li>Regular Check-ins</li>
     <li>Monitor Satisfaction</li>
     <li>Provide Recognition</li>
     <li>Offer Development Opportunities</li>
     </ul>

     </div>
     """, unsafe_allow_html=True)

    else:

     st.markdown(f"""
     <div class="low-risk">

     <h3>🟢 Low Risk Employee</h3>

     <p>
     Attrition Probability: <b>{probability*100:.2f}%</b>
     </p>

     <h4>Recommended Actions</h4>

     <ul>
     <li>Continue Employee Engagement</li>
     <li>Maintain Growth Opportunities</li>
     <li>Encourage Skill Development</li>
     <li>Conduct Periodic Feedback Sessions</li>
     </ul>

     </div>
     """, unsafe_allow_html=True)