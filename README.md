# Smart Farming Data Lifecycle Dashboard

Proyek ini berisi analisis data sensor pertanian cerdas (Smart Farming) dari berbagai tanaman, dengan fokus pada monitoring kelembaban tanah (MOI), suhu udara, dan kelembaban udara. Dashboard dibuat menggunakan Python, Pandas, Plotly, dan Streamlit.

---

## Deskripsi Dataset
Dataset berisi pengukuran sensor harian:
- **crop_id**: Jenis tanaman
- **soil_type**: Tipe tanah
- **seedling_stage**: Tahap pertumbuhan bibit
- **moi**: Moisture Index (indikator kelembaban tanah)
- **temp**: Temperature (°C)
- **humidity**: Kelembaban udara (%)
- **result**: Indikator kebutuhan irigasi (0 = rendah, 1 = sedang, 2 = tinggi)
- **datetime**: Timestamp pengukuran

Jumlah data awal: 16.411 baris, tanpa missing values.

---

## Struktur Project


repo_github/
├── app.py # Dashboard Streamlit
├── requirements.txt # Library Python
├── .streamlit/config.toml # Tema dashboard
├── outputs/
│ └── cleaned_data.csv # Data sensor hasil cleaning
│ └── dashboard_screenshot.png # Screenshot dashboard (opsional)
└── BIG DATA.ipynb # Notebook analisis data


---

## Instalasi

1. Clone repository:

```bash
git clone https://github.com/USERNAME/NAMA-REPO.git
cd NAMA-REPO

Install dependencies:

pip install -r requirements.txt
Menjalankan Dashboard
streamlit run app.py

Dashboard terbuka di browser: http://localhost:8501

Untuk publik: gunakan Streamlit Community Cloud atau localtunnel/ngrok

Fitur Dashboard

Time Series Sensor Trend (MOI, Temperature, Humidity)

Gauge Meter

Heatmap Korelasi

Alert System

Data Preview

Filter: Crop ID, Soil Type, Seedling Stage, dan rentang tanggal

Data Quality Score

Accuracy: 100%

Completeness: 100%

Timeliness: 100%

Dashboard Link

https://link-dashboard.streamlit.app


---

### 2️⃣ Cek README.md

```python
!cat README.md

Pastikan teks lengkap muncul

Bisa diedit jika ingin mengganti USERNAME, NAMA-REPO, dan link dashboard final

3️⃣ Push ke GitHub
!git add README.md
!git commit -m "Add README.md for Smart Farming Dashboard"
!git push https://USERNAME:TOKEN@github.com/USERNAME/NAMA-REPO.git

Ganti USERNAME, TOKEN, dan NAMA-REPO sesuai akun GitHub Anda.
