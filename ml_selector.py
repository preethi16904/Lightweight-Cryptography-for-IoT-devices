# ml_selector.py
import numpy as np
import joblib
import warnings
warnings.filterwarnings("ignore", category=UserWarning)


class CryptoSelector:
    def __init__(self, model_path="ml_model/crypto_switch_model.joblib"):
        self.model = joblib.load(model_path)

    def predict_mode(self, battery_level, memory_kb, throughput_kbps, threat_level):
        X = np.array([[battery_level, memory_kb, throughput_kbps, threat_level]])
        mode = self.model.predict(X)[0]
        return mode  # 0: Skip, 1: Symmetric, 2: Asymmetric
