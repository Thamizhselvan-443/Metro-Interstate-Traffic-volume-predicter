
# 🚦 Traffic Volume Prediction Project

A complete **end-to-end machine learning project** that predicts **traffic volume** based on weather, time, and holiday features.
This project integrates:

* **Data Exploration & Model Training** (Jupyter Notebook)
* **Backend API** (FastAPI)
* **Frontend Client** (Streamlit / Python UI)

---

## 📑 Table of Contents

* [📌 Project Overview](#-project-overview)
* [📂 Project Structure](#-project-structure)
* [🧑‍💻 Files Explained](#-files-explained)

  * [1️⃣ `notebook.ipynb`](#1️⃣-notebookipynb---model-training--experimentation)
  * [2️⃣ `api.py`](#2️⃣-apipy---backend-api-service)
  * [3️⃣ `frontend.py`](#3️⃣-frontendpy---user-interface)
* [⚙️ Installation & Setup](#️-installation--setup)
* [🚀 Running the Project](#-running-the-project)
* [📡 API Endpoints](#-api-endpoints)
* [📊 Example Usage](#-example-usage)
* [🛠️ Tech Stack](#️-tech-stack)
* [📌 Future Improvements](#-future-improvements)

---

## 📌 Project Overview

This project predicts **traffic volume** for a given set of inputs like weather, holiday, time, and rush hour.

* 🧪 Train and evaluate ML models inside **Jupyter Notebook**.
* ⚡ Serve predictions via a **FastAPI backend**.
* 🎨 Provide a simple **frontend interface** for users to test predictions.

---

## 📂 Project Structure

```
📦 traffic-prediction
├── api.py               # FastAPI backend service
├── frontend.py          # Frontend client (Streamlit/CLI)
├── notebook.ipynb       # Model training & experimentation
├── traffic_model_pipeline.joblib  # Saved ML pipeline (after training)
└── README.md            # Project documentation
└── data\
        └── Metro_Interstate_Traffic_Volume.csv  # The dataset shared in whatsapp group
```

---

## 🧑‍💻 Files Explained

### 1️⃣ `notebook.ipynb` - Model Training & Experimentation

This is where all the **data science magic** happens:

* Loads and preprocesses traffic/weather dataset.
* Performs **EDA (Exploratory Data Analysis)**.
* Feature engineering: creates features like `is_rush_hour`, `day_of_week`, etc.
* Trains ML models (e.g., RandomForest, GradientBoosting, or XGBoost).
* Exports the **trained pipeline** as `traffic_model_pipeline.joblib` (used by API).

👉 Run this first to generate the model file.

---

### 2️⃣ `api.py` - Backend API Service

The **FastAPI** server that exposes a REST API for predictions.

**Key Features:**

* Loads trained ML pipeline (`traffic_model_pipeline.joblib`).
* Provides a **health check endpoint** (`/`).
* Provides a **prediction endpoint** (`/predict`).

#### 🔍 Code Walkthrough

```python
app = FastAPI(title="Traffic Volume Prediction API")
```

Initializes FastAPI application.

```python
model_pipeline = joblib.load('traffic_model_pipeline.joblib')
```

Loads the trained model pipeline saved from the notebook.

```python
class TrafficData(BaseModel):
    holiday: str
    temp: float
    rain_1h: float
    snow_1h: float
    clouds_all: int
    weather_main: str
    hour: int
    day_of_week: int
    month: int
    is_rush_hour: int
```

Defines input schema for validation (using **Pydantic**).

```python
@app.post("/predict")
def predict_traffic_volume(data: TrafficData):
    input_df = pd.DataFrame([data.model_dump()])
    prediction = model_pipeline.predict(input_df)
    return {"predicted_traffic_volume": int(prediction[0])}
```

Handles prediction requests and returns traffic volume.

---

### 3️⃣ `frontend.py` - User Interface

Provides a simple **frontend interface** to interact with the API.

Possible implementations (depending on your setup):

* **Streamlit Web App** → allows users to enter features (holiday, weather, etc.) and get predictions.
* **CLI Client** → sends requests to FastAPI and prints predictions.

👉 Useful for non-technical users who don’t want to use API endpoints directly.

---

## ⚙️ Installation & Setup

1. **Clone repo**

   ```bash
   git clone https://github.com/yourusername/traffic-prediction.git
   cd traffic-prediction
   ```

2. **Create virtual environment & install dependencies**

   ```bash
   python -m venv venv
   source venv/bin/activate   # (Linux/Mac)
   venv\Scripts\activate      # (Windows)
   pip install -r requirements.txt
   ```

3. **Run Jupyter Notebook (to train model)**

   ```bash
   jupyter notebook notebook.ipynb
   ```

   → This saves `traffic_model_pipeline.joblib`

---

## 🚀 Running the Project

### Start API Server

```bash
uvicorn api:app --reload
```

### Start Frontend (if Streamlit)

```bash
streamlit run frontend.py
```

---

## 📡 API Endpoints

### ✅ Health Check

`GET /`
Response:

```json
{"message": "Welcome to the Traffic Prediction API. Go to /docs for details."}
```

### 🔮 Predict Traffic Volume

`POST /predict`

**Request Body:**

```json
{
  "holiday": "None",
  "temp": 295.15,
  "rain_1h": 0.0,
  "snow_1h": 0.0,
  "clouds_all": 75,
  "weather_main": "Clouds",
  "hour": 17,
  "day_of_week": 0,
  "month": 6,
  "is_rush_hour": 1
}
```

**Response:**

```json
{
  "predicted_traffic_volume": 4720
}
```

---

## 📊 Example Usage

Python request:

```python
import requests

url = "http://127.0.0.1:8000/predict"
data = {
    "holiday": "None",
    "temp": 295.15,
    "rain_1h": 0.0,
    "snow_1h": 0.0,
    "clouds_all": 75,
    "weather_main": "Clouds",
    "hour": 17,
    "day_of_week": 0,
    "month": 6,
    "is_rush_hour": 1
}
response = requests.post(url, json=data)
print(response.json())
```

---

## 🛠️ Tech Stack

* **Python 3.9+**
* **Pandas, Scikit-learn** (ML pipeline)
* **FastAPI** (Backend API)
* **Streamlit** (Frontend UI)
* **Joblib** (Model persistence)

---

## 📌 Future Improvements

* 📈 Deploy API on **Docker + Cloud (AWS/GCP/Heroku)**
* 🎨 Improve **frontend UI/UX**
* ⚡ Add support for **real-time traffic feeds**
* 📊 Add **model monitoring & retraining pipeline**

---

* By AI Club
