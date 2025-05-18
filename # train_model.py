# train_model.py
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib
import os

df = pd.read_csv("C:\Cryptography\synthetic_crypto_dataset.csv")

X = df[["battery_level", "memory_kb", "throughput_kbps", "threat_level"]]
y = df["crypto_mode"]

clf = DecisionTreeClassifier(max_depth=4, random_state=42)
clf.fit(X, y)

os.makedirs("ml_model", exist_ok=True)
joblib.dump(clf, "ml_model/crypto_switch_model.joblib")
print("Model trained and saved to ml_model/crypto_switch_model.joblib")
