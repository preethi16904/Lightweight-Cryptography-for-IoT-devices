# main.py
from ml_selector import CryptoSelector
import symmentric 
import asymentric

# Sample IoT device profile
test_profiles = [
    {"battery_level": 85, "memory_kb": 2048, "throughput_kbps": 800, "threat_level": 0},  # Mode 0 (Skip)
    {"battery_level": 25, "memory_kb": 256, "throughput_kbps": 100, "threat_level": 2},   # Mode 1 (Symmetric)
    {"battery_level": 90, "memory_kb": 1024, "throughput_kbps": 300, "threat_level": 3},  # Mode 2 (Asymmetric)
    {"battery_level": 50, "memory_kb": 512, "throughput_kbps": 200, "threat_level": 1},   # Mode 1 (Symmetric)
]

data = "secret_payload"
selector = CryptoSelector()

for i, profile in enumerate(test_profiles):
    print(f"\nTest Profile {i+1}: {profile}")
    mode = selector.predict_mode(**profile)
    print(f"Encryption Mode Selected: {mode}")

    if mode == 0:
        print("Skipped encryption (Trusted zone)")
        print(f"Data: {data}")
    elif mode == 1:
        encrypted = symmentric.symmetric_encrypt(data)
        print(f"Symmetric Encrypted: {encrypted}")
        print(f"Decrypted: {symmentric.symmetric_decrypt(encrypted)}")
    elif mode == 2:
        encrypted = asymentric.asymmetric_encrypt(data)
        print(f"Asymmetric Encrypted: {encrypted}")
        print(f"Decrypted: {asymentric.asymmetric_decrypt(encrypted)}")

