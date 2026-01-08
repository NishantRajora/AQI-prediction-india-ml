# AQI Prediction in India using Machine Learning

## 📌 Project Overview
Air pollution is a major public health concern in India.  
This project builds a **time-series machine learning pipeline** to predict the **daily Air Quality Index (AQI)** across multiple Indian cities using historical pollutant data.

Two ensemble models — **Random Forest Regressor** and **XGBoost Regressor** — were trained using a strict time-based split and deployed as an **interactive Streamlit web application**.

🌐 Live App: https://nj-aqi-prediction.streamlit.app/

---

## 📊 Dataset
**Source:** Kaggle  
🔗 https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india  

**Time Period:** 2015 – 2020  
**Granularity:** Daily, city-wise

### Key Features
- PM2.5, PM10
- NO2, NH3, SO2, CO, Ozone
- City
- Date

### Target Variable
- **Air Quality Index (AQI)**

---

## 🔍 Exploratory Data Analysis (EDA)
EDA was performed using **Python and Tableau** to uncover key patterns:
- **Seasonality:** AQI peaks during winter (Dec–Jan) and drops during monsoon (Aug–Sep)
- **Skewness:** Pollutant distributions are heavily right-skewed
- **Autocorrelation:** Strong dependency on previous-day AQI

---

## 🛠 Data Preprocessing
To handle real-world data challenges:
- **Feature Selection:** Removed highly correlated features (e.g., PM2.5, NOx, Benzene)
- **Time-Series Imputation:** Forward-fill imputation grouped by city
- **Log Transformation:** `log1p` applied to reduce skewness and stabilize variance

---

## 🧠 Feature Engineering
Performance improvements were driven by:
- **Lag Features:**  
  - `AQI_lag_1`  
  - `PM10_lag_1`
- **Temporal Features:** Month, Year, Day of Week
- **Spatial Encoding:** One-hot encoding of city names

---

## 🤖 Model Development

### Training Strategy
A **time-based train-test split** was used to prevent data leakage:
- **Train:** 2015 – 2018
- **Test:** 2019 – 2020

### Algorithms Used
- **Random Forest Regressor**
- **XGBoost Regressor**

---

## 📈 Results
Both models achieved strong predictive performance:

| Model | R² Score |
|------|---------|
| Random Forest | 0.9021 |
| XGBoost | 0.9011 |

### Feature Importance Insights
- `AQI_lag_1` was the most influential feature
- Seasonal features (Month) ranked consistently high
- PM10 and NO2 were key pollutant drivers

---

## 🚀 Deployment
The final model was deployed as a **Streamlit dashboard**:
- Interactive visualizations
- Model performance metrics
- AQI prediction insights

**Deployment Stack:**
- Streamlit
- Docker
- Streamlit Community Cloud

🌐 App Link: https://nj-aqi-prediction.streamlit.app/

---

## 📁 Repository Structure
├── data/
│ └── air_quality_data.csv
├── notebooks/
│ └── eda_and_modeling.ipynb
├── app/
│ └── streamlit_app.py
├── models/
│ └── trained_models.pkl
├── README.md


---

## 🎯 Key Learnings
- Time-series aware preprocessing is critical
- Lag features significantly boost predictive power
- Preventing data leakage improves real-world reliability
- Ensemble models perform exceptionally well on structured data

---

## 📌 Future Improvements
- Multi-step AQI forecasting
- City-specific models
- Real-time data integration
- Explainability using SHAP

---

📌 *Feel free to star ⭐ the repository if you find it useful!*
