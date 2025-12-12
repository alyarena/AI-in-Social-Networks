import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from joblib import dump

# Lokasi file dataset sample
DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "sample_dataset.csv")
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.joblib")

def train_and_save_model(data_path: str = DATA_PATH, model_path: str = MODEL_PATH):
"""Latih model Logistic Regression dari dataset CSV dan simpan ke file joblib."""
df = pd.read_csv(data_path)

X = df[["views", "likes"]]
y = df["label"]

# Split (untuk demonstrasi; kita latih menggunakan X dan y penuh setelah split sederhana)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

# Simpan model
dump(model, model_path)

print(f"Model berhasil dilatih dan disimpan ke: {model_path}")

if __name__ == "__main__":
# buat folder data jika tidak ada (hanya safety)
if not os.path.exists(os.path.dirname(DATA_PATH)):
os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)

if not os.path.exists(DATA_PATH):
# buat sample dataset jika tidak ada
sample = """views,likes,label
500000,100000,0
1500000,300000,1
800000,150000,0
3000000,500000,1
2000000,250000,1
900000,100000,0
1200000,220000,1
2500000,400000,1
"""
with open(DATA_PATH, "w") as f:
f.write(sample)
print(f"Sample dataset dibuat di: {DATA_PATH}")

train_and_save_model()
