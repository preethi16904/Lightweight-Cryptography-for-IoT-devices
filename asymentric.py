# crypto_methods/asymmetric.py
def asymmetric_encrypt(data):
    return ''.join([chr((ord(char) * 3) % 256) for char in data])

def asymmetric_decrypt(data):
    return ''.join([chr((ord(char) * pow(3, -1, 257)) % 256) for char in data])
