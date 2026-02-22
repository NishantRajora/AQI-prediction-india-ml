# AQI Prediction in India using Machine Learning

## Overview

Air pollution remains a significant public health and environmental challenge in India.  
This project develops a time-series machine learning pipeline to predict the daily Air Quality Index (AQI) across multiple Indian cities using historical pollutant data.

Two ensemble regression models — Random Forest Regressor and XGBoost Regressor — were trained using a strict time-based data split and deployed as an interactive Streamlit web application.

Live Application:  
https://nj-aqi-prediction.streamlit.app/

---

## Dataset

Source: Kaggle  
https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india  

Time Period: 2015 – 2020  
Granularity: Daily, city-wise observations  

### Key Features
- PM2.5  
- PM10  
- NO2  
- NH3  
- SO2  
- CO  
- Ozone  
- City  
- Date  

### Target Variable
Air Quality Index (AQI)

---

## Exploratory Data Analysis (EDA)

EDA was conducted using Python and Tableau to identify structural patterns and trends:

- Seasonal variation: AQI peaks during winter (December–January) and declines during the monsoon season (August–September)  
- Distribution characteristics: Pollutant variables exhibit strong right-skewness  
- Temporal dependency: Significant autocorrelation observed in AQI values, particularly previous-day influence  

---

## Data Preprocessing

The dataset required careful preprocessing to ensure reliability and prevent bias:

- Feature Selection: Removal of highly correlated features (e.g., PM2.5, NOx, Benzene)  
- Time-Series Imputation: Forward-fill imputation grouped by city to preserve temporal continuity  
- Log Transformation: `log1p` transformation applied to reduce skewness and stabilize variance  
- Data Leakage Prevention: Strict chronological separation between training and testing data  

---

## Feature Engineering

Model performance was improved using structured feature engineering:

- Lag Features:
  - AQI_lag_1  
  - PM10_lag_1  

- Temporal Features:
  - Month  
  - Year  
  - Day of Week  

- Spatial Encoding:
  - One-hot encoding for city-level differentiation  

These features helped capture temporal patterns, seasonality, and spatial variation across cities.

---

## Model Development

### Training Strategy

A time-based train-test split was implemented to prevent data leakage and simulate real-world forecasting:

- Training Set: 2015 – 2018  
- Testing Set: 2019 – 2020  

### Algorithms Used

- Random Forest Regressor  
- XGBoost Regressor  

Both models were tuned and evaluated using appropriate regression metrics.

---

## Results

Both ensemble models demonstrated strong predictive performance:

| Model            | R² Score |
|------------------|----------|
| Random Forest    | 0.9021   |
| XGBoost          | 0.9011   |

### Feature Importance Insights

- AQI_lag_1 was the most influential predictor  
- Seasonal features (Month) consistently ranked among top contributors  
- PM10 and NO2 were significant pollutant drivers  

The results confirm the importance of temporal dependency and seasonal behavior in AQI forecasting.

---

## Deployment

The final model was deployed as an interactive Streamlit dashboard, enabling:

- Real-time AQI prediction  
- Model performance visualization  
- Interactive exploration of trends  

Deployment Stack:
- Streamlit  
- Docker  
- Streamlit Community Cloud  

Application Link:  
https://nj-aqi-prediction.streamlit.app/

---

## Repository Structure

```
AQI-Prediction/
│
├── data/
│   └── air_quality_data.csv
├── notebooks/
│   └── eda_and_modeling.ipynb
├── app/
│   └── streamlit_app.py
├── models/
│   └── trained_models.pkl
└── README.md
```

---

## Key Learnings

- Time-aware preprocessing is essential in forecasting problems  
- Lag-based features significantly enhance predictive accuracy  
- Preventing data leakage improves real-world model reliability  
- Ensemble models perform effectively on structured environmental data  
- Deployment considerations differ from experimental notebook modeling  

---

## Future Improvements

- Multi-step AQI forecasting  
- City-specific specialized models  
- Integration of real-time pollution APIs  
- Model explainability using SHAP  
- Incorporation of meteorological features such as humidity and wind speed  

---

## Author

Nishant Rajora  
Focused on building practical, deployment-ready machine learning systems
