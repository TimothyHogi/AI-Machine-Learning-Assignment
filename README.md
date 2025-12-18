# 🌍 GreenForecast AI: Machine Learning for SDG 13

## 📌 Project Overview
**Theme:** Machine Learning Meets the UN Sustainable Development Goals (SDGs)  
**SDG Addressed:** Goal 13: Climate Action  
**Objective:** To design a Supervised Learning model that predicts national $CO_2$ emissions based on specific fossil fuel consumption patterns (Coal, Oil, Gas, Cement).

## 🤖 Technical Implementation
This project uses a **Random Forest Regressor** to analyze historical emission data from the Global Carbon Project (1950–2021). 

### Key Features:
- **Supervised Learning:** Regression model trained on multi-source emission data.
- **Data Preprocessing:** Handled missing values, filtered aggregate regions, and used Label Encoding for categorical country data.
- **Evaluation Metrics:** Achieved an R-Squared accuracy of **99.78%** with a Mean Absolute Error (MAE) of **1.98 MtCO2**.

## 📊 Results
The model's performance demonstrates a near-perfect correlation between industrial fuel consumption and total carbon footprint.

![Model Performance](model_results.png)

## ⚖️ Ethical Reflection
- **Data Integrity:** The model relies on self-reported national data. To ensure fairness (SDG 10), we must account for potential under-reporting in specific industries.
- **Sustainability:** By identifying the "Feature Importance" (e.g., Coal vs. Oil), policymakers can prioritize which sectors to decarbonize first for maximum impact.

## 🚀 How to Run
1. Clone the repo: `git clone <your-link>`
2. Install dependencies: `pip install pandas scikit-learn matplotlib seaborn`
3. Run the script: `python main.py`