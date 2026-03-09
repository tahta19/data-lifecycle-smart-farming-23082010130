import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

st.set_page_config(page_title="Smart Farming Dashboard", layout="wide")

st.title("🌱 Smart Farming Sensor Dashboard")

# =========================
# LOAD DATA
# =========================
@st.cache_data
def load_data():
    possible_paths = [
        Path("outputs/cleaned_data.csv"),
        Path("../outputs/cleaned_data.csv"),
        Path("cleaned_data.csv")
    ]
    for path in possible_paths:
        if path.exists():
            df = pd.read_csv(path)
            break
    else:
        st.error("File cleaned_data.csv tidak ditemukan.")
        st.stop()

    # pastikan datetime jadi index
    if "datetime" in df.columns:
        df["datetime"] = pd.to_datetime(df["datetime"])
        df = df.set_index("datetime")
    return df

df = load_data()

# =========================
# SIDEBAR FILTER
# =========================
st.sidebar.title("Filter Dashboard")

crop_options = ["All"] + sorted(df["crop_id"].dropna().unique().tolist())
soil_options = ["All"] + sorted(df["soil_type"].dropna().unique().tolist())
stage_options = ["All"] + sorted(df["seedling_stage"].dropna().unique().tolist())

selected_crop = st.sidebar.selectbox("Crop ID", crop_options)
selected_soil = st.sidebar.selectbox("Soil Type", soil_options)
selected_stage = st.sidebar.selectbox("Seedling Stage", stage_options)

date_min = df.index.min().date()
date_max = df.index.max().date()
selected_date = st.sidebar.date_input("Date Range", value=(date_min, date_max), min_value=date_min, max_value=date_max)

if isinstance(selected_date, tuple) and len(selected_date) == 2:
    start_date, end_date = selected_date
else:
    start_date, end_date = date_min, date_max

# filter dataframe
filtered_df = df.copy()
if selected_crop != "All":
    filtered_df = filtered_df[filtered_df["crop_id"] == selected_crop]
if selected_soil != "All":
    filtered_df = filtered_df[filtered_df["soil_type"] == selected_soil]
if selected_stage != "All":
    filtered_df = filtered_df[filtered_df["seedling_stage"] == selected_stage]

filtered_df = filtered_df[(filtered_df.index.date >= start_date) & (filtered_df.index.date <= end_date)]

if filtered_df.empty:
    st.warning("Tidak ada data untuk kombinasi filter yang dipilih.")
    st.stop()

# =========================
# KPI SECTION
# =========================
latest = filtered_df.iloc[-1]

avg_moi = filtered_df["moi"].mean()
avg_temp = filtered_df["temp"].mean()
avg_humidity = filtered_df["humidity"].mean()
dominant_result = filtered_df["result"].mode()[0]

col1, col2, col3, col4 = st.columns(4)
col1.metric("Average MOI", f"{avg_moi:.2f}")
col2.metric("Average Temperature", f"{avg_temp:.2f} °C")
col3.metric("Average Humidity", f"{avg_humidity:.2f} %")
col4.metric("Dominant Result", f"{dominant_result}")

# =========================
# ALERT SYSTEM
# =========================
st.subheader("🚨 Smart Alert System")

alert_messages = []

moi_threshold = df["moi"].quantile(0.25)
humidity_threshold = df["humidity"].quantile(0.25)
temp_high_threshold = df["temp"].quantile(0.75)

if latest["moi"] < moi_threshold:
    alert_messages.append(f"MOI rendah ({latest['moi']:.2f})")
if latest["humidity"] < humidity_threshold:
    alert_messages.append(f"Humidity rendah ({latest['humidity']:.2f}%)")
if latest["temp"] > temp_high_threshold:
    alert_messages.append(f"Temperature tinggi ({latest['temp']:.2f}°C)")

if alert_messages:
    for msg in alert_messages:
        st.error(msg)
else:
    st.success("Semua sensor dalam rentang aman.")

# =========================
# GAUGE METERS
# =========================
st.subheader("📟 Real-Time Gauge")

g1, g2, g3 = st.columns(3)

with g1:
    fig_moi = go.Figure(go.Indicator(
        mode="gauge+number",
        value=float(latest["moi"]),
        title={"text": "Current MOI"},
        gauge={"axis":{"range":[0,100]}},
    ))
    st.plotly_chart(fig_moi, use_container_width=True)

with g2:
    fig_temp = go.Figure(go.Indicator(
        mode="gauge+number",
        value=float(latest["temp"]),
        title={"text": "Current Temperature"},
        gauge={"axis":{"range":[0,50]}},
    ))
    st.plotly_chart(fig_temp, use_container_width=True)

with g3:
    fig_humidity = go.Figure(go.Indicator(
        mode="gauge+number",
        value=float(latest["humidity"]),
        title={"text": "Current Humidity"},
        gauge={"axis":{"range":[0,100]}},
    ))
    st.plotly_chart(fig_humidity, use_container_width=True)

# =========================
# TIME SERIES TREND
# =========================
st.subheader("📈 Time Series Trend")
ts_df = filtered_df[["moi","temp","humidity"]].resample("D").mean().reset_index()
fig_ts = px.line(ts_df, x="datetime", y=["moi","temp","humidity"], title="Sensor Trend Over Time")
st.plotly_chart(fig_ts, use_container_width=True)

# =========================
# CORRELATION HEATMAP
# =========================
st.subheader("🔥 Correlation Heatmap")
corr = filtered_df[["moi","temp","humidity","result"]].corr()
fig_corr = px.imshow(corr, text_auto=".2f", color_continuous_scale="RdBu_r")
st.plotly_chart(fig_corr, use_container_width=True)

# =========================
# RESULT DISTRIBUTION
# =========================
st.subheader("📊 Target Distribution")
result_counts = filtered_df["result"].value_counts().sort_index().reset_index()
result_counts.columns = ["result","count"]
fig_result = px.bar(result_counts, x="result", y="count", text="count")
st.plotly_chart(fig_result, use_container_width=True)

# =========================
# DATA PREVIEW
# =========================
st.subheader("🗂 Data Preview")
st.dataframe(filtered_df.tail(20))
