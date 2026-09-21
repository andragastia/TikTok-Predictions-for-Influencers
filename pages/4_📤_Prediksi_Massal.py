"""
Batch Prediction Page
CSV upload interface for bulk predictions
(Updated: Added Advanced Visualizations & Feature Importance)
"""
import streamlit as st
import pandas as pd
import numpy as np
import sys
from pathlib import Path
from datetime import datetime
from io import BytesIO

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

from utils.model_handler import get_model_handler
from utils.data_processor import get_data_processor
from utils.visualizations import create_pie_chart, create_bar_chart, create_heatmap

# Page config
st.set_page_config(
    page_title="Prediksi Massal - Sistem Prediksi TikTok",
    page_icon="📤",
    layout="wide"
)

# Header
st.title("📤 Prediksi Massal")
st.markdown("Upload file CSV untuk memprediksi potensi *Trending* banyak video sekaligus.")

# Load model
@st.cache_resource
def load_model():
    """Load and cache model"""
    return get_model_handler()

model_handler = load_model()

st.markdown("---")

# --- PANDUAN PENGGUNAAN ---
with st.expander("ℹ️ Panduan Penggunaan"):
    st.markdown("""
    ### Cara Menggunakan:
    1. **Upload CSV:** Unggah file yang memiliki fitur lengkap (gunakan *Preproses Data* jika punya data mentah).
    2. **Jalankan Prediksi:** Klik tombol untuk memproses seluruh data.
    3. **Analisis Visual:** Lihat grafik faktor penentu dan perbandingan performa.
    4. **Ekspor Data:** Unduh hasil prediksi dalam format Excel/CSV.
    """)

st.markdown("---")

# --- TEMPLATE DOWNLOAD ---
st.subheader("📥 Download Template CSV")

# Template Data (EXACT 29 fitur model + metadata; ponytail: tanpa alias lama)
template_data = {
    'Video_ID': [1, 2], 'Caption': ['Video Gaming', 'Video Masak'],
    'Suka': [2000, 100],  # metadata untuk Interaksi (model baca Interaksi_*, bukan Suka)
    'Durasi_Video': [45, 15], 'Jumlah_Hashtag': [5, 2], 'Panjang_Caption': [50, 20],
    'Jam_Posting': [18, 10], 'Is_Weekend': [1, 0],
    'Kat_Gaming': [1, 0], 'Kat_Kuliner': [0, 1], 'Kat_Fashion': [0, 0],
    'Kat_Daily': [0, 0], 'Kat_Edukasi_Karir': [0, 0], 'Kat_Religi': [0, 0],
    'Kat_Beauty': [0, 0], 'Kat_Hiburan': [0, 0],
    'Kat_Musik_Konser': [0, 0], 'Kat_Jedag Jedug': [0, 0],
    'Audio_Audio Populer': [1, 0], 'Audio_Audio Original': [0, 1],
    'Audio_Audio Lainnya': [0, 0], 'Audio_Tanpa Audio': [0, 0],
    'Interaksi_Gaming_Suka': [2000, 0], 'Interaksi_Kuliner_Suka': [0, 100],
    'Interaksi_Fashion_Suka': [0, 0], 'Interaksi_Daily_Suka': [0, 0],
    'Interaksi_Edukasi_Karir_Suka': [0, 0], 'Interaksi_Religi_Suka': [0, 0],
    'Interaksi_Beauty_Suka': [0, 0], 'Interaksi_Hiburan_Suka': [0, 0],
    'Interaksi_Musik_Konser_Suka': [0, 0], 'Interaksi_Jedag Jedug_Suka': [0, 0],
    'Actual': [1, 0]  # opsional, untuk evaluasi
}

template_df = pd.DataFrame(template_data)
csv_template = template_df.to_csv(index=False)

col1, col2 = st.columns([1, 3])
with col1:
    st.download_button("📥 Unduh Template CSV", csv_template, "template_prediksi_batch.csv", "text/csv", use_container_width=True)
with col2:
    st.info("💡 Gunakan halaman **Preproses Data** untuk membuat file CSV secara otomatis dari data mentah.")

st.markdown("---")

# --- FILE UPLOAD ---
st.subheader("📁 Upload File CSV")

uploaded_file = None
df = None

# Auto-load check
if st.session_state.get('auto_load_preprocessed', False) and st.session_state.get('preprocessed_data_ready', False):
    df = st.session_state.get('preprocessed_data')
    if df is not None:
        st.info("ℹ️ Data otomatis dimuat dari hasil Preproses.")
        st.session_state['auto_load_preprocessed'] = False

if df is None:
    uploaded_file = st.file_uploader("Pilih file CSV", type=['csv'])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.success(f"✅ File dimuat! Total: {len(df)} baris")
    except Exception as e:
        st.error(f"Gagal membaca file: {e}")
        st.stop()

# --- PREDICTION LOGIC ---
if df is not None:
    # Validasi Kolom
    required_features = model_handler.feature_names
    missing = [c for c in required_features if c not in df.columns]
    
    if missing:
        st.error("❌ Format File Tidak Sesuai")
        st.warning(f"Kolom hilang: {', '.join(missing[:5])}...")
        st.stop()

    with st.expander("👁️ Preview Data Input"):
        st.dataframe(df.head(), use_container_width=True)

    if st.button("🚀 Jalankan Prediksi", type="primary", use_container_width=True):
        with st.spinner("Sedang memproses prediksi massal..."):
            try:
                # Prediksi
                X = df[required_features].copy()
                preds, probs = model_handler.predict_batch(X)
                
                # Simpan Hasil
                df['Prediksi'] = preds
                df['Label_Prediksi'] = df['Prediksi'].map({0: 'Tidak Trending', 1: 'Trending'})
                df['Confidence_Score'] = probs.max(axis=1)
                
                st.success("✅ Prediksi Selesai!")
                st.markdown("---")

                # ==========================================
                # 📊 BAGIAN VISUALISASI UTAMA
                # ==========================================
                st.header("📊 Dashboard Hasil Prediksi")

                # 1. Ringkasan Angka
                c1, c2, c3, c4 = st.columns(4)
                total = len(df)
                trending = (df['Prediksi'] == 1).sum()
                c1.metric("Total Video", total)
                c2.metric("Diprediksi Trending", trending, f"{trending/total*100:.1f}%")
                c3.metric("Tidak Trending", total - trending)
                c4.metric("Rerata Keyakinan", f"{df['Confidence_Score'].mean()*100:.1f}%")

                st.markdown("---")

                # 2. Distribusi & Confidence (Fitur Lama + Update)
                col_left, col_right = st.columns(2)
                
                with col_left:
                    st.subheader("Proporsi Prediksi")
                    counts = df['Label_Prediksi'].value_counts()
                    fig_pie = create_pie_chart(counts.values, counts.index, title="Trending vs Tidak", hole=0.4)
                    st.plotly_chart(fig_pie, use_container_width=True)
                    
                with col_right:
                    st.subheader("Sebaran Keyakinan (Confidence)")
                    conf_bins = pd.cut(df['Confidence_Score'], bins=5).value_counts().sort_index()
                    conf_df = pd.DataFrame({'Range': conf_bins.index.astype(str), 'Jumlah': conf_bins.values})
                    fig_bar = create_bar_chart(conf_df, x='Range', y='Jumlah', title="Histogram Confidence", 
                                             xaxis_title="Rentang", yaxis_title="Jumlah", orientation='v')
                    st.plotly_chart(fig_bar, use_container_width=True)

                st.markdown("---")

                # 3. [FITUR BARU] ANALISIS FAKTOR & KOMPARASI
                st.header("🔍 Analisis Mendalam (Deep Dive)")
                
                col_a, col_b = st.columns(2)
                
                with col_a:
                    st.subheader("🌟 Faktor Penentu (Global)")
                    # Ambil Feature Importance dari Model Handler
                    feature_imp = model_handler.get_feature_importance()
                    
                    if feature_imp is not None:
                        # Mapping nama fitur agar lebih cantik (Sama seperti Prediksi Tunggal)
                        rename_fitur = {
                            'Suka': 'Jml Suka', 'Komentar': 'Jml Komentar', 'Dibagikan': 'Jml Share',
                            'Durasi_Video': 'Durasi', 'Jam_Sejak_Publikasi': 'Usia Video',
                            'Panjang_Caption': 'Panjang Caption', 'Jam_Upload': 'Jam Upload'
                        }
                        # Bersihkan nama
                        feature_imp['feature_clean'] = feature_imp['feature'].apply(
                            lambda x: rename_fitur.get(x, x.replace('Kat_', 'Kategori: ').replace('Audio_', 'Audio: '))
                        )
                        
                        fig_imp = create_bar_chart(
                            feature_imp.head(10), 
                            x='feature_clean', y='importance', 
                            title="10 Faktor Paling Berpengaruh", 
                            xaxis_title="Faktor", yaxis_title="Bobot", 
                            orientation='h'
                        )
                        st.plotly_chart(fig_imp, use_container_width=True)
                    else:
                        st.info("Feature importance tidak tersedia untuk model ini.")

                with col_b:
                    st.subheader("📈 Profil: Trending vs Tidak")
                    # Bandingkan Rata-rata Metrik Utama
                    if 'Suka' in df.columns:
                        avg_stats = df.groupby('Label_Prediksi')[['Suka', 'Komentar', 'Dibagikan']].mean().reset_index()
                        
                        # Tampilkan Chart Sederhana (Likes)
                        fig_comp = create_bar_chart(
                            avg_stats, 
                            x='Label_Prediksi', y='Suka', 
                            title="Rata-rata Likes per Kelompok Prediksi", 
                            xaxis_title="Prediksi", yaxis_title="Avg Likes",
                            orientation='v'
                        )
                        st.plotly_chart(fig_comp, use_container_width=True)
                        
                        # Tampilkan Dataframe kecil
                        st.caption("Rata-rata Metrik:")
                        
                        # --- PERBAIKAN DI SINI ---
                        # Menggunakan parameter 'subset' agar format angka hanya berlaku untuk kolom numerik
                        st.dataframe(
                            avg_stats.style.format("{:.0f}", subset=['Suka', 'Komentar', 'Dibagikan']), 
                            use_container_width=True, 
                            hide_index=True
                        )

                # ==========================================
                # EVALUASI (Jika Ada Kolom Actual)
                # ==========================================
                if 'Actual' in df.columns:
                    st.header("🎯 Evaluasi Akurasi")
                    from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
                    
                    y_true, y_pred = df['Actual'], df['Prediksi']
                    acc = accuracy_score(y_true, y_pred)
                    
                    c1, c2 = st.columns(2)
                    with c1:
                        st.metric("Akurasi Batch Ini", f"{acc*100:.1f}%")
                        cm = confusion_matrix(y_true, y_pred)
                        fig_cm = create_heatmap(cm, x_labels=['Pred: 0', 'Pred: 1'], y_labels=['Act: 0', 'Act: 1'], title="Confusion Matrix")
                        st.plotly_chart(fig_cm, use_container_width=True)
                        
                    with c2:
                        st.text("Detail Laporan:")
                        report = pd.DataFrame(classification_report(y_true, y_pred, output_dict=True)).transpose()
                        st.dataframe(report.style.format("{:.2f}"), use_container_width=True)

                st.markdown("---")

                # ==========================================
                # TABEL & EKSPOR
                # ==========================================
                st.subheader("📋 Data Hasil Prediksi")
                
                cols_show = ['Video_ID', 'Caption', 'Label_Prediksi', 'Confidence_Score']
                cols_show = [c for c in cols_show if c in df.columns]
                st.dataframe(df[cols_show], use_container_width=True)

                st.subheader("💾 Simpan Hasil")
                c1, c2 = st.columns(2)
                tstamp = datetime.now().strftime("%Y%m%d_%H%M")
                
                with c1:
                    st.download_button("📥 Unduh CSV", df.to_csv(index=False), f"prediksi_{tstamp}.csv", "text/csv", use_container_width=True)
                with c2:
                    buffer = BytesIO()
                    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                        df.to_excel(writer, index=False)
                    st.download_button("📥 Unduh Excel", buffer.getvalue(), f"prediksi_{tstamp}.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", use_container_width=True)

            except Exception as e:
                st.error(f"Error proses: {e}")
                st.exception(e)

# Placeholder
if df is None and not uploaded_file:
    st.info("👈 Mulai dengan mengupload file CSV atau hasil preprocessing.")

st.markdown("---")
st.caption("📤 Batch Prediction System - Support Visualisasi Lanjutan")