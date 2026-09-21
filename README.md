# 🎯 TikTok Content Performance Prediction System

Sistem prediksi performa konten TikTok menggunakan Random Forest Classifier untuk membantu content creator @septianndt dalam mengoptimalkan strategi konten.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.51.0-red)
![License](https://img.shields.io/badge/License-Academic-green)

---

## 📚 Daftar Isi

- [Tentang Proyek](#-tentang-proyek)
- [Fitur Utama](#-fitur-utama)
- [Tech Stack](#-tech-stack)
- [Instalasi](#-instalasi)
- [Cara Penggunaan](#-cara-penggunaan)
- [Struktur Proyek](#-struktur-proyek)
- [Model Information](#-model-information)
- [Dataset Information](#-dataset-information)
- [Screenshots](#-screenshots)
- [Deployment](#-deployment)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)
- [Kontak](#-kontak)

---

## 🎓 Tentang Proyek

**TikTok Content Performance Prediction System** adalah aplikasi web berbasis machine learning yang dirancang untuk:

- Menganalisis performa konten TikTok
- Memprediksi potensi trending suatu video
- Memberikan rekomendasi strategi konten berbasis data

### Academic Context

- **Tugas Akhir Skripsi**: Implementasi Data Mining untuk Prediksi Trending Video TikTok
- **Institution**: UPN Veteran Jakarta - Fakultas Ilmu Komputer, S1 Sistem Informasi
- **Target User**: 15 Small Content Creators
- **Development**: 5 months

---

## ✨ Fitur Utama

### 1. 📊 Dashboard Analitik

Analisis komprehensif performa konten dengan fitur:

- **Overview Metrics**: KPI cards dengan statistik ringkasan
- **Temporal Analysis**: Performa berdasarkan hari dan jam upload
- **Content Type Analysis**: Perbandingan tipe konten (OOTD, Tutorial, Vlog, dll)
- **Audio Analysis**: Performa audio original vs trending
- **Top Performers**: Top 10 video berdasarkan views, likes, comments
- **Engagement Patterns**: Correlation matrix dan scatter plots
- **Key Insights**: Rekomendasi berbasis data untuk optimasi konten

### 2. 🔮 Prediksi Tunggal

Form interaktif untuk prediksi individual dengan:

- **Input Form**: Form hibrida (caption/NLP + metrik estimasi) yang dipetakan ke 29 fitur model
- **Real-time Prediction**: Hasil prediksi Trending/Tidak Trending
- **Confidence Score**: Tingkat keyakinan model dengan probability breakdown
- **Feature Importance**: Visualisasi faktor paling berpengaruh
- **Smart Recommendations**: Saran perbaikan berbasis analisis
- **Comparison Table**: Perbandingan input dengan rata-rata dataset

### 3. 📤 Prediksi Massal

Batch prediction via CSV upload dengan:

- **Template CSV**: Download template dengan format lengkap
- **File Validation**: Pengecekan kolom dan tipe data
- **Bulk Processing**: Prediksi untuk ratusan video sekaligus
- **Comparison Analysis**: Predicted vs Actual dengan confusion matrix
- **Performance Metrics**: Accuracy, Precision, Recall, F1-Score
- **Export Options**: Download hasil dalam CSV atau Excel

---

## 🛠️ Tech Stack

### Framework & Libraries

- **Streamlit** 1.51.0 - Web application framework
- **scikit-learn** 1.5.0 - Machine learning model
- **Pandas** 2.2.2 - Data manipulation
- **NumPy** 1.26.4 - Numerical computing
- **Plotly** 6.4.0 - Interactive visualizations
- **openpyxl** 3.1.5 - Excel file support
- **joblib** 1.4.0 - Model serialization

### Machine Learning

- **Model**: Random Forest Classifier
- **Trees**: 100
- **Max Depth**: 10
- **Features**: 29 (temporal, content, audio, interaction)
- **Classes**: Binary (0=Tidak Trending, 1=Trending)
- **Labeling**: Trending = views di atas persentil ke-75 (~7.455 views)

### Development Tools

- **Python**: 3.8+
- **IDE**: VSCode with Claude Code
- **Documentation**: CLAUDE.md for project context

---

## 📦 Instalasi

### Prerequisites

- Python 3.8 atau lebih tinggi
- pip (Python package manager)
- Git (opsional)

### Step 1: Clone Repository

```bash
git clone <repository-url>
cd tiktok-prediction-system
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Verify Installation

```bash
streamlit --version
```

---

## 🚀 Cara Penggunaan

### Running the Application

#### Method 1: Standard Run

```bash
streamlit run 🏠_Beranda.py
```

#### Method 2: Custom Port

```bash
streamlit run 🏠_Beranda.py --server.port 8502
```

#### Method 3: Headless Mode

```bash
streamlit run 🏠_Beranda.py --server.headless=true
```

### Accessing the Application

Setelah aplikasi berjalan, buka browser dan akses:

- **Local**: http://localhost:8501
- **Network**: http://<your-ip>:8501

---

## 📱 Panduan Penggunaan Lengkap

### 1. Dashboard Analitik

**Langkah-langkah:**

1. Buka halaman **Analytics Dashboard** dari menu sidebar
2. Lihat ringkasan performa di bagian atas (KPI cards)
3. Scroll ke bawah untuk melihat analisis temporal (hari & jam terbaik)
4. Eksplorasi analisis tipe konten dan audio
5. Review top performers untuk inspirasi konten
6. Gunakan filter di sidebar untuk analisis spesifik

**Tips:**

- Hover di atas chart untuk detail lebih lanjut
- Klik dan drag untuk zoom in pada chart
- Gunakan range slider pada time series untuk fokus periode tertentu

### 2. Prediksi Tunggal

**Langkah-langkah:**

1. Buka halaman **Prediction** dari menu sidebar
2. Isi form dengan informasi video:
   - **Engagement Metrics**: Estimasi likes, comments, shares
   - **Video Details**: Durasi, hashtag, caption length
   - **Categories**: Tipe konten, audio, hari & jam upload
3. (Opsional) Buka "Pengaturan Lanjutan" untuk parameter tambahan
4. Klik **"🔮 Prediksi Sekarang"**
5. Lihat hasil prediksi dan confidence score
6. Baca rekomendasi untuk optimasi konten

**Tips:**

- Gunakan nilai rata-rata sebagai panduan (ditampilkan di helper text)
- Default values sudah diset ke nilai optimal berdasarkan analisis
- Fokus pada faktor dengan importance tinggi untuk hasil terbaik

### 3. Prediksi Massal

**Langkah-langkah:**

1. Buka halaman **Batch Prediction** dari menu sidebar
2. Download template CSV menggunakan tombol **"📥 Unduh Template CSV"**
3. Buka template di Excel/Google Sheets
4. Hapus baris contoh dan isi dengan data video Anda
5. Save file CSV
6. Upload file menggunakan file uploader
7. Review preview data (5 baris pertama)
8. Klik **"🚀 Jalankan Prediksi"**
9. Analisis hasil dan visualisasi
10. Download hasil dalam format CSV atau Excel

**Tips:**

- Gunakan kolom `Actual` untuk membandingkan prediksi dengan hasil sebenarnya
- Tambahkan kolom `Video_ID` dan `Caption` untuk identifikasi lebih mudah
- Untuk dataset besar (>100 rows), proses mungkin membutuhkan waktu beberapa detik

---

## 📁 Struktur Proyek

```
tiktok-prediction-system/
├── 🏠_Beranda.py                        # Main application entry point
├── pages/                              # Streamlit pages
│   ├── __init__.py
│   ├── 1_📊_Dashboard_Analitik.py      # Analytics & insights page
│   ├── 2_🔮_Prediksi_Tunggal.py        # Single prediction page
│   ├── 3_🔧_Preproses_Data.py          # Raw data preprocessing page
│   ├── 4_📤_Prediksi_Massal.py         # Batch prediction page
│   └── 5_📝_Input_Data_Baru.py         # Manual data input page
├── utils/                              # Utility modules
│   ├── __init__.py
│   ├── model_handler.py                # Model operations (load, predict)
│   ├── data_processor.py               # Data loading & preprocessing
│   ├── visualizations.py               # Chart creation functions
│   ├── theme_manager.py                # Light/dark theme handling
│   └── input_handler.py                # Manual data append to CSV
├── models/                             # Machine learning models
│   └── tiktok_model_final_CLASSIFIER.pkl  # Pre-trained Random Forest (29 features)
├── data/                               # Datasets
│   └── dataset_tiktok.csv              # TikTok analytics data (998 videos)
├── .streamlit/                         # Streamlit configuration
│   └── config.toml                     # Theme and server settings
├── requirements.txt                    # Python dependencies (pinned)
├── .gitignore                          # Git ignore rules
├── README.md                           # This file
└── UPDATE_SUMMARY.md                   # Development progress
```

---

## 🤖 Model Information

### Model Specifications

- **Type**: RandomForestClassifier
- **Algorithm**: Ensemble learning (bagging)
- **Number of Trees**: 100
- **Max Depth**: 10
- **Classes**: [0, 1] → [Tidak Trending, Trending]
- **Labeling**: Trending = `playCount` di atas persentil ke-75 (~7.455 views)

### Features (29 total, wajib exact — lihat `model_handler.feature_names`)

#### Base Features (5)

1. **Durasi_Video** - Video duration in seconds
2. **Jam_Posting** - Upload hour (0-23)
3. **Is_Weekend** - 1 jika upload Sabtu/Minggu
4. **Panjang_Caption** - Caption length (characters)
5. **Jumlah_Hashtag** - Number of hashtags

#### Content Type (One-hot encoded, 10)

6. **Kat_Beauty**
7. **Kat_Daily**
8. **Kat_Edukasi_Karir**
9. **Kat_Fashion**
10. **Kat_Gaming**
11. **Kat_Hiburan**
12. **Kat_Jedag Jedug**
13. **Kat_Kuliner**
14. **Kat_Musik_Konser**
15. **Kat_Religi**

#### Audio Type (One-hot encoded, 4)

16. **Audio_Audio Lainnya**
17. **Audio_Audio Original**
18. **Audio_Audio Populer**
19. **Audio_Tanpa Audio**

#### Interaction Features (10, Kategori × Suka)

20. **Interaksi_Beauty_Suka**
21. **Interaksi_Daily_Suka**
22. **Interaksi_Edukasi_Karir_Suka**
23. **Interaksi_Fashion_Suka**
24. **Interaksi_Gaming_Suka**
25. **Interaksi_Hiburan_Suka**
26. **Interaksi_Jedag Jedug_Suka**
27. **Interaksi_Kuliner_Suka**
28. **Interaksi_Musik_Konser_Suka**
29. **Interaksi_Religi_Suka**

> Catatan: model TIDAK memakai `Suka` mentah — hanya via `Interaksi_*_Suka`.
> Skema lama (`Tipe_Konten_*`, `Komentar`, `Dibagikan`, `Jam_Sejak_Publikasi`, dll)
> sudah tidak dipakai dan dihapus dari preprocessing/template.

### Feature Importance (Top 5, aktual dari model)

1. **Interaksi_Hiburan_Suka**: 30.49%
2. **Interaksi_Gaming_Suka**: 15.67%
3. **Interaksi_Fashion_Suka**: 13.48%
4. **Kat_Gaming**: 7.02%
5. **Panjang_Caption**: 5.13%

---

## 📊 Dataset Information

### Source

- **Origin**: TikTok Analytics dari akun @septianndt
- **Collection Method**: FreeTikTokScraper
- **Date Range**: 2023-2024
- **File**: `dataset_tiktok.csv`

### Statistics

- **Total Records**: 998 videos (14 kreator)
- **Total Columns**: 19 (raw) + enriched features
- **Total Views**: 32,127,317
- **Average Engagement Rate**: 8.23%
- **Best Video Performance**: 6,600,000 views
- **Date Range**: 2021–2025

### Raw Columns

1. `authorMeta.avatar` - Creator avatar URL
2. `authorMeta.name` - Creator name (@septianndt)
3. `text` - Video caption/description
4. `diggCount` - Number of likes
5. `shareCount` - Number of shares
6. `playCount` - Number of views
7. `commentCount` - Number of comments
8. `videoMeta.duration` - Video duration (seconds)
9. `musicMeta.musicName` - Music track name
10. `musicMeta.musicAuthor` - Music artist
11. `musicMeta.musicOriginal` - Is original audio (boolean)
12. `createTimeISO` - Upload timestamp (ISO format)
13. `webVideoUrl` - TikTok video URL

### Key Insights

- **Best Day to Post**: Tuesday
- **Best Content Type**: Varies by analysis period
- **Avg Duration**: 30 seconds
- **Avg Hashtags**: 3-4 per video

---

## 📸 Screenshots

### 1. Home Page

- Welcome message and overview
- Quick statistics cards
- Navigation to all features

### 2. Analytics Dashboard

- Comprehensive performance analytics
- Multiple visualizations (10+ charts)
- Interactive filters and drill-downs

### 3. Single Prediction

- Interactive form (dipetakan ke 29 fitur model)
- Real-time prediction results
- Confidence scores and recommendations

### 4. Batch Prediction

- CSV upload interface
- Bulk prediction processing
- Comparison analysis and export

---

## 🚢 Deployment

### Option 1: Streamlit Cloud (Recommended)

#### Prerequisites

- GitHub account
- Repository pushed to GitHub

#### Steps

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click "New app"
4. Select your repository
5. Set main file: `🏠_Beranda.py`
6. Click "Deploy"

#### Configuration

No additional configuration needed. The app will automatically:

- Install dependencies from `requirements.txt`
- Use `.streamlit/config.toml` for theme
- Run on Streamlit Cloud servers

### Option 2: Local Server

#### For Development

```bash
streamlit run 🏠_Beranda.py
```

#### For Production (with PM2)

```bash
# Install PM2
npm install -g pm2

# Create ecosystem file
pm2 start 🏠_Beranda.py --interpreter python3 --name tiktok-app

# Save PM2 configuration
pm2 save
pm2 startup
```

### Option 3: Docker (Advanced)

#### Create Dockerfile

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "🏠_Beranda.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

#### Build and Run

```bash
docker build -t tiktok-prediction .
docker run -p 8501:8501 tiktok-prediction
```

---

## 🔧 Troubleshooting

### Common Issues

#### 1. **ModuleNotFoundError**

```bash
# Solution: Install dependencies
pip install -r requirements.txt
```

#### 2. **Port Already in Use**

```bash
# Solution: Use different port
streamlit run app.py --server.port 8502
```

#### 3. **Model Loading Warning**

```
InconsistentVersionWarning: Trying to unpickle estimator from version X when using version Y
```

**Solution**: This is a warning, not an error. The model will still work. To eliminate:

```bash
pip install scikit-learn==1.6.1
```

#### 4. **CSV Upload Error**

**Solution**: Ensure CSV has all 29 required model features. Download template from Batch Prediction page.

#### 5. **Charts Not Displaying**

**Solution**: Clear Streamlit cache

```bash
# In the app, press 'C' then 'Clear cache'
# Or restart the app
```

### Performance Issues

#### Slow Loading

- **Cause**: Large dataset or slow connection
- **Solution**: Data is cached after first load. Subsequent loads will be faster.

#### Memory Issues

- **Cause**: Running batch prediction on very large CSV (>10,000 rows)
- **Solution**: Split CSV into smaller batches

---

## 🤝 Contributing

This is an academic project. Contributions are welcome for:

- Bug fixes
- Performance improvements
- UI/UX enhancements
- Documentation updates

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

---

## 📄 License

**Academic Project**

This project is developed as a final thesis (Tugas Akhir) for academic purposes at UPN Veteran Jakarta.

For educational and non-commercial use only.

---

## 👤 Kontak

### Project Information

- **Developer**: [Your Name]
- **Institution**: UPN Veteran Jakarta
- **Faculty**: Ilmu Komputer
- **Program**: S1 Sistem Informasi

### Support

- **Issues**: [GitHub Issues](your-repo/issues)
- **Email**: your-email@example.com
- **LinkedIn**: [Your Profile]

---

## 🙏 Acknowledgments

### Data & Content

- Content Creator: **@septianndt**
- Data Source: FreeTikTokScraper

### References

- Meiza Alliansa (2025) - Random Forest Implementation Reference
- UPN Veteran Jakarta - Academic Support

### Tools & Technologies

- Streamlit - Web framework
- Anthropic Claude - Development assistance via Claude Code
- scikit-learn - Machine learning library

---

## 📚 Additional Documentation

### For Developers

- [PHASE_COMPLETION_SUMMARY.md](PHASE_COMPLETION_SUMMARY.md) - Development progress

### API Documentation

All utility functions are documented with docstrings. Use Python's `help()` function:

```python
from utils.model_handler import ModelHandler
help(ModelHandler)
```

---

## 🎯 Roadmap

### Version 1.1.0 (Current) — Opsi A schema freeze

- ✅ Analytics Dashboard
- ✅ Single Prediction (exact 29 fitur model)
- ✅ Batch Prediction (template exact 29 fitur)
- ✅ Preprocessing → Batch auto-load (termasuk `Audio_Tanpa Audio`)
- ✅ Export functionality
- ✅ Pinned requirements

### Version 1.0

- ✅ Analytics Dashboard
- ✅ Single Prediction
- ✅ Batch Prediction
- ✅ Export functionality

### Future Enhancements

- 🚧 Real-time TikTok API integration
- 🚧 Advanced visualization options
- 🚧 Model retraining interface
- 🚧 User authentication
- 🚧 Historical tracking
- 🚧 Mobile app version

---

<div align="center">

**Made with ❤️ for Content Creators**

⭐ Star this repo if you find it useful!

[Report Bug](your-repo/issues) · [Request Feature](your-repo/issues)

</div>
