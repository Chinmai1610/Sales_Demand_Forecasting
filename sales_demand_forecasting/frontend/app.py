import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import os

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Sales Demand Forecast",
    page_icon="📊",
    layout="centered"
)

# --- 2. ADAPTIVE CSS FOR STYLE ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    [data-testid="stMetric"] {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border-bottom: 4px solid #3B82F6;
    }
    h1, h2, h3 { color: #1E3A8A; font-family: 'Inter', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. ROBUST DATA LOADING ---
@st.cache_data
def load_data(path):
    if not os.path.exists(path):
        return None
    
    df = pd.read_csv(path)
    
    # Standardize column names
    df.columns = df.columns.str.strip().str.lower()
    
    # Try to find the date column
    date_options = ['date', 'timestamp', 'ds', 'time', 'period', 'unnamed: 0']
    found_date = next((c for c in date_options if c in df.columns), None)
    
    if found_date:
        df[found_date] = pd.to_datetime(df[found_date])
        df = df.rename(columns={found_date: 'date'})
        df = df.sort_values('date')
    else:
        df['date'] = pd.date_range(start=pd.Timestamp.now().date(), periods=len(df))
    
    # Handle sales column name
    if 'forecast_sales' not in df.columns and 'sales' in df.columns:
        df = df.rename(columns={'sales': 'forecast_sales'})
    elif 'forecast_sales' not in df.columns:
        # If still not found, assume the first numerical column is sales
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            df = df.rename(columns={numeric_cols[0]: 'forecast_sales'})
            
    return df

file_path = "outputs/forecast_results.csv"
df = load_data(file_path)

if df is None:
    st.error("📂 **File Not Found:** Please run your model script first to generate `outputs/forecast_results.csv`.")
    st.stop()

# --- 4. SIDEBAR CONTROLS ---
with st.sidebar:
    st.title("🛠 Settings")
    st.markdown("---")
    # Consolidating window slider to one location to avoid DuplicateWidgetID errors
    window = st.slider("Moving Average Window", 3, 60, 15)
    st.info("Higher values smooth the trend more.")
    st.markdown("---")
    st.write("✅ Model: **ARIMA (v1.2)**")
    st.write(f"📅 Run Date: {pd.Timestamp.now().strftime('%Y-%m-%d')}")
    
# --- 5. HEADER ---
st.title("📊 Sales Demand Analysis Report")
st.markdown("Vertical breakdown of sales performance and model projections.")
st.divider()

# --- 6. KPI METRICS ---
# Fixed the col4 error by creating 4 columns
m1, m2, m3, m4 = st.columns(4)
m1.metric("Total Projected", f"{df['forecast_sales'].sum():,.0f}")
m2.metric("Avg Demand", f"{df['forecast_sales'].mean():,.1f}")
m3.metric("Peak Value", f"{df['forecast_sales'].max():,.0f}")
m4.metric("95% Quantile", f"{df['forecast_sales'].quantile(0.95):,.1f}")

st.markdown("---")

# --- 7. VERTICAL GRAPHS SECTION ---

# GRAPH 1: Trend & Moving Average
st.subheader("1️⃣ Sales Trend & Moving Average")
df['moving_avg'] = df['forecast_sales'].rolling(window=window).mean()

fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=df['date'], y=df['forecast_sales'], name='Actual/Forecast', line=dict(color='#cbd5e1', width=1.5)))
fig1.add_trace(go.Scatter(x=df['date'], y=df['moving_avg'], name=f'{window}-Day Avg', line=dict(color='#2563eb', width=3)))
fig1.update_layout(template="simple_white", height=450, hovermode="x unified", legend=dict(orientation="h", y=1.1))
st.plotly_chart(fig1, use_container_width=True)

st.markdown("---")

# GRAPH 2: Monthly Analysis
st.subheader("2️⃣ Average Monthly Sales")
df['month_name'] = df['date'].dt.month_name()
months_order = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# Only include months present in data
available_months = [m for m in months_order if m in df['month_name'].unique()]
monthly_avg = df.groupby('month_name')['forecast_sales'].mean().reindex(available_months)

fig2 = px.bar(monthly_avg, x=monthly_avg.index, y='forecast_sales', 
             color='forecast_sales', color_continuous_scale='Blues')
fig2.update_layout(template="simple_white", height=400, showlegend=False)
st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

# GRAPH 3: Distribution
st.subheader("3️⃣ Distribution of Sales Values")
fig3 = px.histogram(df, x="forecast_sales", nbins=25, color_discrete_sequence=['#6366f1'], marginal="box")
fig3.update_layout(template="simple_white", height=400, bargap=0.1)
st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")

# GRAPH 4: Correlation Matrix
st.subheader("4️⃣ Feature Correlation")
df['day_num'] = df['date'].dt.day
df['month_num'] = df['date'].dt.month
corr_data = df[['forecast_sales', 'month_num', 'day_num']].corr()

fig4 = px.imshow(corr_data, text_auto=".2f", color_continuous_scale='RdBu_r', aspect="auto")
fig4.update_layout(height=400)
st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")

# --- 8. DATA TABLE & DOWNLOAD ---
st.subheader("📋 Detailed Data View")
st.dataframe(df[['date', 'forecast_sales', 'moving_avg']].sort_values('date', ascending=False), use_container_width=True)

# Prepare download data
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="⬇️ Download Forecast CSV",
    data=csv,
    file_name="forecast_results_clean.csv",
    mime="text/csv"
)

st.success("Report Generated Successfully!")