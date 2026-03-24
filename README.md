# 📄 Sales Demand Forecasting Project

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

## 🔮 Future Improvements

- Prophet model integration  
- Deep learning (LSTM) forecasting  
- Real-time data integration  
- Deployment on cloud (Streamlit Cloud / AWS)  

---
## Screenshots
<img width="1847" height="795" alt="Screenshot 2026-03-21 192841" src="https://github.com/user-attachments/assets/5c8a669f-6b06-47dc-ae74-adcb9d4cc10e" />

<img width="1847" height="795" alt="Screenshot 2026-03-21 192841" src="https://github.com/user-attachments/assets/a6d9c505-86d0-44fc-b060-080c33d7c4af" />

<img width="1721" height="805" alt="Screenshot 2026-03-21 192917" src="https://github.com/user-attachments/assets/cfc10196-6c35-404a-a6f1-3d6d1491edb0" />

<img width="1762" height="756" alt="Screenshot 2026-03-21 192931" src="https://github.com/user-attachments/assets/6a2196a1-2636-44fe-ba76-4822e632b2e3" />

<img width="1716" height="775" alt="Screenshot 2026-03-21 192946" src="https://github.com/user-attachments/assets/820e39c3-679f-45f0-8c5c-72c3ae440b10" />

<img width="1831" height="858" alt="Screenshot 2026-03-21 193005" src="https://github.com/user-attachments/assets/d76dfb0e-b59e-4c4e-893b-459e557d410e" />

<img width="1734" height="683" alt="Screenshot 2026-03-21 193023" src="https://github.com/user-attachments/assets/de9b9c90-c28f-4804-92c9-9dc230bf42f2" />

--

