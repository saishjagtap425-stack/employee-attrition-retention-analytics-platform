# 📊 Employee Attrition & Retention Analytics Platform

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)

An end-to-end Machine Learning and HR Analytics platform that predicts employee attrition, identifies high-risk employees, and provides actionable retention insights through an interactive Streamlit dashboard.

---

## 🚀 Project Overview

This project helps HR teams proactively identify employees who are likely to leave the organization using Machine Learning. It combines data analysis, predictive modeling, business insights, and an interactive Streamlit application to support data-driven retention strategies.

---

## ✨ Features

- 📊 Interactive HR Analytics Dashboard
- 📈 Employee Data Analysis (EDA)
- 🤖 Multiple ML Models Comparison
- 🎯 Random Forest Attrition Prediction
- 📊 Feature Importance Analysis
- ⚠️ Employee Risk Segmentation
- 💡 HR Retention Recommendations
- 🔮 Real-Time Attrition Predictor

---

## 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-Learn |
| Models | Logistic Regression, Decision Tree, Random Forest |
| Deployment | Streamlit |
| Version Control | Git, GitHub |

---

## 🔄 Machine Learning Workflow

1. Data Cleaning
2. Exploratory Data Analysis
3. Feature Engineering
4. Data Encoding
5. Model Training
6. Model Evaluation
7. Model Selection
8. Streamlit Deployment

---

## 📂 Dataset

- Employees: **74,498**
- Features: **26**
- Problem Type: **Binary Classification**
- Target Variable:
  - 0 → Stayed
  - 1 → Left

---

## 🏆 Model Performance

| Model | Accuracy | Precision | Recall | F1 Score |
|------|----------:|----------:|--------:|----------:|
| Logistic Regression | 73.75% | 72.75% | 71.49% | 72.11% |
| Decision Tree | 73.82% | 72.50% | 72.26% | 72.38% |
| **Random Forest** | **74.98%** | **73.79%** | **73.35%** | **73.57%** |

**Final Model:** Random Forest Classifier

---

## 📁 Project Structure

```text
employee-attrition-retention-analytics-platform/
│
├── app.py
├── style.py
├── employee_attrition_model.pkl
├── attrition_dataset.csv
├── requirements.txt
├── README.md
├── pages/
└── screenshots/
