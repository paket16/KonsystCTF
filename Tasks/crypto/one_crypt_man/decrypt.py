def hex_to_bytes(hex_string):
    """Преобразование строки hex в байты."""
    return bytes.fromhex(hex_string)

def decrypt(ciphertext, key):
    """Дешифрование сообщения с использованием XOR."""
    repeated_key = (key * (len(ciphertext) // len(key) + 1))[:len(ciphertext)]
    return bytes([c ^ k for c, k in zip(ciphertext, repeated_key)])

# Ваше зашифрованное сообщение
hex_ciphertext = "090909343761180d312b610516783961070021"
key = b"AleXX"

# Преобразование hex в байты
ciphertext = hex_to_bytes(hex_ciphertext)

# Дешифрование
decrypted_message = decrypt(ciphertext, key)
print(f"Расшифрованное сообщение: {decrypted_message.decode('utf-8')}")