# AI in Social Networks
Klasifikasi Konten Populer
# ✨ CLASSIFICATION PROJECT: POPULARITAS KONTEN MEDIA SOSIAL ✨

## 🚀 TEAM BASED PROJECT UAS

Kami mengembangkan model Machine Learning untuk secara otomatis menentukan apakah sebuah konten video akan menjadi **Populer** atau **Tidak Populer** berdasarkan metrik interaksi.

| 🎯 Aspek Proyek | ⚙️ Detail Implementasi |
| :--- | :--- |
| **Bidang AI** | Social Networks Analysis / Klasifikasi Biner |
| **Model Utama** | Regresi Logistik (Logistic Regression) |
| **Fitur Input** | `Views` dan `Likes` |
| **Kriteria Populer** | Konten Populer jika **Views $\ge 1.000.000$** **DAN** **Likes $\ge 200.000$** |
| **Output Akhir** | Skrip Python interaktif (`src/predict_classifier.py`) |

---

## 🔬 METODOLOGI DAN MODEL

### 1. Definisi dan Pelabelan Data

Model dilatih pada data yang dilabeli berdasarkan kriteria popularitas tim. 

### 2. Pilihan Model: Regresi Logistik

Model Regresi Logistik dipilih karena efisiensi dan kemampuannya yang sangat baik untuk memisahkan data dalam masalah klasifikasi biner linier.

---

## 💻 PANDUAN EKSEKUSI (EXECUTABLE MODEL)

### 1. Kebutuhan (Requirements)

Instal library yang diperlukan:

```bash
pip install -r requirements.txt
