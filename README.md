 **Sales Demand Forecasting Project**
---

# 📄 README.md

```markdown
# 📊 Sales & Demand Forecasting for Businesses

An AI-powered project that predicts future sales using **Time Series Forecasting (ARIMA)** and provides an interactive dashboard built with **Streamlit**.

---

## 🚀 Project Overview

This project helps businesses forecast future sales using historical data.  
It applies **time-series analysis** techniques and provides **business-friendly visual insights** through an interactive dashboard.

---

## 🎯 Features

- 📈 Sales forecasting using ARIMA model  
- 📊 Interactive dashboard using Streamlit  
- 📅 Date filtering and category filtering  
- 📉 Sales distribution analysis  
- 📊 Animated charts with Plotly  
- 📥 Download forecast results  
- 🌙 Dark mode UI  
- 🎨 Gradient KPI cards  
- 📋 Forecast data table  

---

## 🧠 Tech Stack

- Python  
- Pandas  
- NumPy  
- Statsmodels (ARIMA)  
- Plotly  
- Streamlit  

---

## 📂 Project Structure

```

sales_demand_forecasting/
│
├── data/
│   └── sales_data.csv
│
├── frontend/
│   └── app.py
│
├── notebooks/
│   └── exploratory_analysis.ipynb
│
├── outputs/
│   ├── forecast_results.csv
│   └── forecast_plot.png
│
├── src/
│   ├── data_loader.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   ├── forecast.py
│   ├── evaluation.py
│   ├── visualization.py
│   └── save_plot.py
│
├── main.py
├── requirements.txt
└── README.md

```

---

## ⚙️ Installation

Install dependencies:

```

pip install -r requirements.txt

```

---

## ▶️ How to Run

### 1️⃣ Run Model (Generate Forecast)

```

python main.py

```

This will generate:
- `outputs/forecast_results.csv`
- `outputs/forecast_plot.png`

---

### 2️⃣ Run Dashboard

```

python -m streamlit run frontend/app.py

```

Open in browser:
```

[http://localhost:8501](http://localhost:8501)

```

---

## 📊 Input Data Format

CSV file should contain:

| date | sales |
|------|------|
| 2024-01-01 | 200 |
| 2024-01-02 | 220 |

---

## 📈 Output

- Forecasted sales values  
- Interactive dashboard visualization  
- Downloadable CSV results  

---

## 📸 Project Screenshots

### 🔹 Dashboard Overview
<p align="center">
  <img width="1847" height="795" alt="Screenshot 2026-03-21 192841" src="https://github.com/user-attachments/assets/8fddf2a7-8e7a-41e0-8bc1-7b4d8a3321d8" />

</p>

### 🔹 Forecast Metrics
<p align="center">
  <img width="1721" height="805" alt="Screenshot 2026-03-21 192917" src="https://github.com/user-attachments/assets/943177ba-2f2c-42d6-a8f4-3bdff82817bf" />

</p>

### 🔹 Sales Forecast Trend
<p align="center">
 <img width="1721" height="805" alt="Screenshot 2026-03-21 192917" src="https://github.com/user-attachments/assets/8a4e8c31-609a-42eb-9320-b04f35fa81fb" />

</p>

### 🔹 Animated Chart View
<p align="center">
  <img width="1762" height="756" alt="Screenshot 2026-03-21 192931" src="https://github.com/user-attachments/assets/f54e3427-10d9-4399-bd58-80a4f303e5d7" />

</p>

### 🔹 Distribution Analysis
<p align="center">
  <img src="https://github.com/user-attachments/assets/8d0617ca-2cc6-4465-b113-cbf0538de7f6" width="800"/>
</p>

### 🔹 Data Table View
<p align="center">
  <img src="https://github.com/user-attachments/assets/38ec0f07-84fe-437d-b5d4-324694d6fa01" width="800"/>
</p>

### 🔹 Download Feature
<p align="center">
  <img width="1734" height="683" alt="Screenshot 2026-03-21 193023" src="https://github.com/user-attachments/assets/6806bcce-ec91-4f60-82d7-42950a9593f6" />

</p>
---

## 🔮 Future Improvements

- Prophet model integration  
- Deep learning (LSTM) forecasting  
- Real-time data integration  
- Deployment on cloud (Streamlit Cloud / AWS)  

---


