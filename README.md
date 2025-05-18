# Lightweight-Cryptography-for-IoT-devices
This project implements a smart, lightweight, and secure cryptographic system designed for **IoT environments**, combining **machine learning** with real-world **hybrid encryption** using AES and ECC.

🧠 **Overview**
Traditional encryption methods like RSA and even AES are often too heavy for constrained IoT devices. This project solves that by:

- Using a trained **Decision Tree AI model** to intelligently select an encryption mode.
- Dynamically choosing between:
  - **Skip encryption** (trusted zones)
  - **AES (symmetric)** for lightweight fast encryption
  - **ECC-AES hybrid (asymmetric)** for high-security situations
 
🚀 **Features**

- 🧠 **AI-powered encryption mode selector** (trained on synthetic IoT profiles)
- 🔐 **AES-128** for fast, resource-efficient symmetric encryption
- 🟣 **ECC-based key exchange** + AES (true hybrid model)
- 📊 **Energy, RAM, and delay estimators** for each mode
- 🖥️ **Interactive GUI** (Tkinter) to test profiles live
- 📡 **Real-time client-server simulation** of IoT communication using sockets

🧩 **Tech Stack**

| Component        | Library / Tool       |
|------------------|-----------------------|
| AI Model         | scikit-learn          |
| Symmetric Crypto | pycryptodome (AES)    |
| Asymmetric Crypto| cryptography (ECC)    |
| GUI              | Tkinter               |
| Sockets          | Python standard lib   |
| Dataset          | Synthetic CSV (battery, memory, threat level, etc.) |
