# server_ai.py
import socket
import json
from ml_selector import CryptoSelector
import symmentric
import asymentric

HOST = 'localhost'
PORT = 9999

selector = CryptoSelector()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"[SERVER] Listening on {HOST}:{PORT}...")

while True:
    conn, addr = server.accept()
    print(f"[SERVER] Connected to {addr}")
    data = conn.recv(1024).decode()
    profile = json.loads(data)

    mode = selector.predict_mode(
        profile["battery"],
        profile["memory"],
        profile["throughput"],
        profile["threat"]
    )

    response = {
        "mode": mode,
        "encrypted_data": ""
    }

    if mode == 0:
        response["encrypted_data"] = profile["data"]
    elif mode == 1:
        response["encrypted_data"] = symmentric.symmetric_encrypt(profile["data"])
    elif mode == 2:
        response["encrypted_data"] = asymentric.asymmetric_encrypt(profile["data"])

    response = {
    "mode": int(mode),
    "encrypted_data": response["encrypted_data"]
}

    conn.send(json.dumps(response).encode())
    conn.close()
