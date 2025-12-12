import os
import pandas as pd
from joblib import load


MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.joblib")




# Lazy load model saat modul diimport
_model = None


def _load_model():
global _model
if _model is None:
if not os.path.exists(MODEL_PATH):
raise FileNotFoundError(
f"Model tidak ditemukan. Jalankan 'python model.py' untuk melatih dan menyimpan model ke: {MODEL_PATH}"
)
_model = load(MODEL_PATH)
return _model




def cek_video_populer(views: int, likes: int) -> str:
"""Mengembalikan 'Populer' atau 'Tidak Populer' berdasarkan prediksi model.


Fungsi menerima angka integer untuk views dan likes.
"""
model = _load_model()
input_df = pd.DataFrame({"views": [int(views)], "likes": [int(likes)]})
pred = model.predict(input_df)[0]
return "Populer" if int(pred) == 1 else "Tidak Populer"




if __name__ == "__main__":
# Demo cepat
try:
v = int(input("Masukkan jumlah views: "))
l = int(input("Masukkan jumlah likes: "))
print("Hasil:", cek_video_populer(v, l))
except Exception as e:
print("Error:", e)
