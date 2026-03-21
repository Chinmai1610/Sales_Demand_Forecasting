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

## 📸 Dashboard Preview

<img width="1847" height="795" alt="Screenshot 2026-03-21 192841" src="https://github.com/user-attachments/assets/24f52410-a9bb-4d89-a236-5a1e75895b2b" />

<img width="1797" height="787" alt="Screenshot 2026-03-21 192901" src="https://github.com/user-attachments/assets/91bed534-3c21-40fd-bc72-5165c7be940b" />

<img width="1721" height="805" alt="Screenshot 2026-03-21 192917" src="https://github.com/user-attachments/assets/f005bd9d-6527-4ceb-abc5-19ffe65828ce" />

<img width="1762" height="756" alt="Screenshot 2026-03-21 192931" src="https://github.com/user-attachments/assets/cfb2d437-11cf-486f-b53f-12a6c0eec43e" />

<img width="1716" height="775" alt="Screenshot 2026-03-21 192946" src="https://github.com/user-attachments/assets/8d0617ca-2cc6-4465-b113-cbf0538de7f6" />

<img width="1831" height="858" alt="Screenshot 2026-03-21 193005" src="https://github.com/user-attachments/assets/38ec0f07-84fe-437d-b5d4-324694d6fa01" />

<img width="1734" height="683" alt="Screenshot 2026-03-21 193023" src="https://github.com/user-attachments/assets/6194a670-d856-4f59-a602-582e5e2190ad" />

---

## 🔮 Future Improvements

- Prophet model integration  
- Deep learning (LSTM) forecasting  
- Real-time data integration  
- Deployment on cloud (Streamlit Cloud / AWS)  

---


