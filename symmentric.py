''''
# crypto_methods/symmetric.py
def symmetric_encrypt(data, key=7):
    return ''.join([chr((ord(char) + key) % 256) for char in data])

def symmetric_decrypt(data, key=7):
    return ''.join([chr((ord(char) - key) % 256) for char in data])

'''
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b'ThisIsA16ByteKey'  # 16-byte key for AES-128

def symmetric_encrypt(data):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pad(data.encode(), AES.block_size)).hex()

def symmetric_decrypt(data_hex):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(bytes.fromhex(data_hex))
    return unpad(decrypted, AES.block_size).decode()
