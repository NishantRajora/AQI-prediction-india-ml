import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image # PIL is used to open images
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# -----------------------------------------------------------------
# PAGE CONFIG
# This sets the title and icon for your browser tab
# -----------------------------------------------------------------
st.set_page_config(
    page_title="AQI Prediction Project",
    page_icon="💨",
    layout="wide"
)

# -----------------------------------------------------------------
# TITLE
# -----------------------------------------------------------------
st.title('💨 Air Quality Index (AQI) Prediction Project')
st.write('By: Nipun Juneja (23csu215),' \
'             Nishant Rajora (23csu220),' \
'             Monika (23csu203)' \
'             | Course: AI & ML')
st.markdown("---") # Adds a horizontal line

# -----------------------------------------------------------------
# TABS
# This is the best way to organize your project.
# -----------------------------------------------------------------
tab1, tab2, tab3 = st.tabs([
    "1. 📈 Introduction & EDA", 
    "2. 🛠️ Preprocessing & Feature Engineering", 
    "3. 🤖 Model Results & Conclusion"
])


# -----------------------------------------------------------------
# TAB 1: INTRODUCTION & EDA
# -----------------------------------------------------------------
with tab1:
    st.header('1. Project Introduction')
    st.write(
        """
        The goal of this project was to predict the Air Quality Index (AQI) 
        using real-world data from various Indian cities. The dataset
        included daily pollutant levels, allowing for a time-series approach.
        """
    )

    st.header('2. Exploratory Data Analysis (EDA)')
    st.write(
        """
        My first step was to understand the data. I immediately found two
        critical patterns:
        """
    )
    
    st.subheader('Insight 1: Strong Seasonality')
    st.write(
        """
        Using Tableau, I plotted the 7-day moving average of AQI. 
        I discovered a clear seasonal pattern: AQI peaks in the winter 
        (Dec-Jan) and is lowest during the monsoon (Aug-Sep). 
        This discovery was the key to my feature engineering.
        """
    )
    try:
        img = Image.open(os.path.join(SCRIPT_DIR, 'AQI_7_Day_Moving_Average.png'))
        st.image(img, caption='7-Day Moving Average of AQI Over Time')
    except FileNotFoundError:
        st.warning("Image 'your_tableau_seasonal_plot.png' not found.")


    st.subheader('Insight 2: Skewed Data Distributions')
    st.write(
        """
        The histograms for all pollutants (and AQI itself) were heavily 
        right-skewed. This means most days have 'low' pollution, but a few 
        days have 'extreme' values. This would harm model performance.
        """
    )
    try:
        img = os.path.join(SCRIPT_DIR, 'histograms_collage.png')
        st.image(img, caption='Histograms of all pollutant features')
    except FileNotFoundError:
        st.warning("Image 'histogramz_collage.png' not found.")


# -----------------------------------------------------------------
# TAB 2: PREPROCESSING
# -----------------------------------------------------------------
with tab2:
    st.header('3. Preprocessing & Feature Engineering')
    st.write("This was the most critical part of the project.")

    st.subheader('3.1 Correlation & Feature Selection')
    st.write(
        """
        The correlation heatmap showed high multicollinearity. For example:
        - `PM2.5` and `PM10` (0.85)
        - `NOx` and `NO2` (0.8)
        I kept the feature in each pair that had a higher correlation with `AQI`. 
        This led me to **drop PM2.5, NOx, and Benzene.**
        """
    )
    try:
        img = os.path.join(SCRIPT_DIR, 'correlation_heatmap.png')
        st.image(img, caption=' Correlation Heatmap of Pollutants')
    except FileNotFoundError:
        st.warning("Image 'correlation_heatmap.png' not found.")

    st.subheader('3.2 Imputation & Transformation')
    st.write(
        """
        **1. Imputation:** I filled missing data using a `groupby('City').ffill()` 
        (forward-fill) approach. This is crucial for time-series data, as it assumes 
        today's missing value is the same as yesterday's—a much safer bet than 
        using a global average.
        
        **2. Log Transformation:** To fix the skew identified in the EDA, I applied 
        a `np.log1p()` transformation to all skewed features and the target (AQI). 
        This "squashes" the extreme values and helps the model learn.
        """
    )

    st.subheader('3.3 Feature Engineering')
    st.write(
        """
        Based on my insights, I engineered new features:
        - **Date Features:** `month`, `year`, `day_of_week` (to capture seasonality).
        - **Categorical Features:** One-hot encoded `City` (e.g., `City_Delhi`).
        - **Lag Features:** `AQI_lag_1` and `PM10_lag_1`. This was the most 
          powerful feature, as it gives the model "yesterday's" data to 
          predict "today's."
        """
    )


# -----------------------------------------------------------------
# TAB 3: MODEL RESULTS
# -----------------------------------------------------------------
with tab3:
    st.header('4. Model Training & Evaluation')
    st.write(
        """
        To prevent data leakage, I split the data by time, not randomly.
        - **Training Set:** All data <= 2018
        - **Testing Set:** All data > 2018
        
        I trained two powerful models: Random Forest and XGBoost.
        """
    )
    
    st.subheader('Final R-squared ($R^2$) Scores:')
    # Use st.metric to show off your scores!
    col1, col2 = st.columns(2)
    col1.metric("Random Forest", "0.9021", "Slightly better")
    col2.metric("XGBoost", "0.9011", "Slightly faster")

    st.header('5. Feature Importance')
    st.write(
        """
        This is the *'why'*. The models confirmed my hypotheses. Both models
        agreed on the top important features:
        """
    )
    
    # --- ADD YOUR IMPORTANCE PLOTS ---
    col1, col2 = st.columns(2)
    try:
        img_rf = os.path.join(SCRIPT_DIR, 'random_forest_feature_importance.png')
        col1.image(img_rf, caption='Random Forest Importance')
    except FileNotFoundError:
        col1.warning("Image 'random_forest_feature_importance.png' not found.")
    
    try:
        img_xgb = os.path.join(SCRIPT_DIR, 'xgboost_feature_importance.png')
        col2.image(img_xgb, caption='XGBoost Importance')
    except FileNotFoundError:
        col2.warning("Image 'xgboost_feature_importance.png' not found.")


    st.header('6. Conclusion')
    st.success(
        """
        The project was a success, achieving an R-squared score of **~0.90**.
        
        The analysis clearly shows that AQI is driven by three main factors:
        1.  **Short-term Trends:** The most important predictor was `AQI_lag_1`.
        2.  **Seasonality:** The `month` was also a really important predictor.
        3.  **Current Pollutants:** `PM10` and `CO` were also highly influential.
        
        This project demonstrates the power of combining time-series analysis, 
        exploratory data analysis, and feature engineering to build a
        highly accurate predictive model.
        """
    )