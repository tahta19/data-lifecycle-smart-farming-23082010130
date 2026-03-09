# Smart Farming Data Lifecycle Dashboard

Proyek ini berisi analisis data sensor pertanian cerdas (Smart Farming) dari berbagai tanaman, dengan fokus pada monitoring kelembaban tanah (MOI), suhu udara, dan kelembaban udara. Dashboard dibuat menggunakan Python, Pandas, Plotly, dan Streamlit untuk membantu memonitor kondisi lingkungan tanaman serta memperkirakan kebutuhan irigasi.

---

## Dashboard Link

https://data-lifecycle-smart-farming-23082010130-tahta.streamlit.app/

---

## Deskripsi Dataset

Dataset berisi pengukuran sensor pertanian yang digunakan untuk memonitor kondisi lingkungan tanaman.

- **crop_id**: Jenis tanaman  
- **soil_type**: Tipe tanah  
- **seedling_stage**: Tahap pertumbuhan bibit  
- **moi**: Moisture Index (indikator kelembaban tanah)  
- **temp**: Temperature (°C)  
- **humidity**: Kelembaban udara (%)  
- **result**: Indikator kebutuhan irigasi (0 = rendah, 1 = sedang, 2 = tinggi)  
- **datetime**: Timestamp pengukuran  

Jumlah data awal: **16.411 baris**, tanpa missing values.

---

## Data Lifecycle

Proyek ini menerapkan tahapan **Data Lifecycle** yang meliputi:

1. **Data Collection** – Menggunakan dataset sensor pertanian.  
2. **Data Cleaning** – Menghapus duplikasi dan menangani outlier menggunakan metode IQR.  
3. **Data Transformation** – Menyesuaikan format kolom dan timestamp untuk analisis.  
4. **Data Analysis** – Melakukan analisis statistik dan korelasi antar sensor.  
5. **Data Visualization** – Menampilkan hasil analisis dalam dashboard interaktif.

---

## Struktur Project
DATA-LIFECYCLE-SMART-FARMING
│
├── .devcontainer/
│
├── .streamlit/
│ └── config.toml
│
├── dashboard/
│ └── streamlit_app.py
│
├── data_raw/
│ └── cropdata_updated.csv
│
├── outputs/
│ ├── cleaned_data.csv
│ └── dashboard_screenshot.png
│
├── Data_Lifecycle_Smart_Farming.ipynb
├── requirements.txt
└── README.md

## Fitur Dashboard

- Time Series Sensor Trend (MOI, Temperature, Humidity)
- Gauge Meter Monitoring
- Heatmap Korelasi
- Alert System
- Data Preview
- Filter: Crop ID, Soil Type, Seedling Stage, dan rentang tanggal

---

## Data Quality Score

- Accuracy: 100%
- Completeness: 100%
- Timeliness: 100%

---

## Technology Used

Python, Pandas, NumPy, Matplotlib, Seaborn, Plotly, Streamlit