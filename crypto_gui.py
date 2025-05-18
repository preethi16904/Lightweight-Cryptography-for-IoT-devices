import tkinter as tk
from tkinter import ttk, messagebox
from ml_selector import CryptoSelector
import symmentric
import asymentric

def run_encryption():
    battery = battery_scale.get()
    memory = memory_scale.get()
    throughput = throughput_scale.get()
    threat = int(threat_dropdown.get())
    data = entry_data.get()

    if not data:
        messagebox.showerror("Input Error", "Please enter data to encrypt.")
        return

    selector = CryptoSelector()
    mode = selector.predict_mode(battery, memory, throughput, threat)

    if mode == 0:
        mode_label.config(text="Mode: 0 (Skip - Trusted Zone)")
        encrypted = data
        decrypted = data
    elif mode == 1:
        mode_label.config(text="Mode: 1 (Symmetric Encryption)")
        encrypted = symmentric.symmetric_encrypt(data)
        decrypted = symmentric.symmetric_decrypt(encrypted)
    elif mode == 2:
        mode_label.config(text="Mode: 2 (Asymmetric Encryption)")
        encrypted = asymentric.asymmetric_encrypt(data)
        decrypted = asymentric.asymmetric_decrypt(encrypted)
    else:
        encrypted = "Unknown"
        decrypted = "Unknown"

    result_enc.config(text=f"Encrypted: {encrypted}")
    result_dec.config(text=f"Decrypted: {decrypted}")

# --- GUI Setup ---
window = tk.Tk()
window.title("AI-Powered IoT Crypto Mode Selector")

# Battery
tk.Label(window, text="Battery Level (%)").grid(row=0, column=0, sticky='w')
battery_scale = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL)
battery_scale.set(50)
battery_scale.grid(row=0, column=1)

# Memory
tk.Label(window, text="Memory (KB)").grid(row=1, column=0, sticky='w')
memory_scale = tk.Scale(window, from_=128, to=2048, orient=tk.HORIZONTAL, resolution=128)
memory_scale.set(512)
memory_scale.grid(row=1, column=1)

# Throughput
tk.Label(window, text="Throughput (kbps)").grid(row=2, column=0, sticky='w')
throughput_scale = tk.Scale(window, from_=30, to=1000, orient=tk.HORIZONTAL, resolution=10)
throughput_scale.set(200)
throughput_scale.grid(row=2, column=1)

# Threat Level
tk.Label(window, text="Threat Level (0=Low, 3=Critical)").grid(row=3, column=0, sticky='w')
threat_dropdown = ttk.Combobox(window, values=["0", "1", "2", "3"], state="readonly")
threat_dropdown.current(1)
threat_dropdown.grid(row=3, column=1)

# Data
tk.Label(window, text="Data to Encrypt").grid(row=4, column=0, sticky='w')
entry_data = tk.Entry(window, width=30)
entry_data.insert(0, "secret_payload")
entry_data.grid(row=4, column=1)

# Run Button
tk.Button(window, text="Encrypt", command=run_encryption).grid(row=5, columnspan=2, pady=10)

# Results
mode_label = tk.Label(window, text="Mode: ")
mode_label.grid(row=6, columnspan=2)

result_enc = tk.Label(window, text="Encrypted: ")
result_enc.grid(row=7, columnspan=2)

result_dec = tk.Label(window, text="Decrypted: ")
result_dec.grid(row=8, columnspan=2)

window.mainloop()

