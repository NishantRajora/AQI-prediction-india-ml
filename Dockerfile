FROM python:3.10-slim

WORKDIR /app

COPY AQI_Prediction_Project/main_project/requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt --no-cache-dir

COPY AQI_Prediction_Project /app/AQI_Prediction_Project

WORKDIR /app/AQI_Prediction_Project/main_project

EXPOSE 7860

ENTRYPOINT ["python", "-m", "streamlit", "run", "web_app.py", "--server.port=7860", "--server.address=0.0.0.0"]