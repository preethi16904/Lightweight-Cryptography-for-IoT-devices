import socket
import json
from symmentric import symmetric_decrypt
from asymentric import asymmetric_decrypt

HOST = 'localhost'
PORT = 9999

# 🔹 Get user input
battery = int(input("Enter battery level (0–100): "))
memory = int(input("Enter memory (KB): "))
throughput = int(input("Enter throughput (kbps): "))
threat = int(input("Enter threat level (0–3): "))
data = input("Enter message to encrypt: ")

# 🔹 Compose profile
device_profile = {
    "battery": battery,
    "memory": memory,
    "throughput": throughput,
    "threat": threat,
    "data": data
}

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    client.send(json.dumps(device_profile).encode())

    response = client.recv(2048).decode()
    client.close()

    resp = json.loads(response)
    mode = resp["mode"]
    encrypted = resp["encrypted_data"]

    print(f"\n[CLIENT] Encryption Mode Used: {mode}")
    print(f"[CLIENT] Encrypted Message: {encrypted}")

    if mode == 0:
        print(f"[CLIENT] Decrypted (Skipped): {encrypted}")
    elif mode == 1:
        print(f"[CLIENT] Decrypted (AES): {symmetric_decrypt(encrypted)}")
    elif mode == 2:
        print(f"[CLIENT] Decrypted (ECC-AES): {asymmetric_decrypt(encrypted)}")

except Exception as e:
    print(f"[CLIENT] ERROR: {e}")
