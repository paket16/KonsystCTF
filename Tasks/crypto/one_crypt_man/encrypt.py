def encrypt(plaintext, key):
    """Шифрование сообщения с использованием XOR."""
    # Повторяем ключ до длины сообщения
    repeated_key = (key * (len(plaintext) // len(key) + 1))[:len(plaintext)]
    return bytes([p ^ k for p, k in zip(plaintext, repeated_key)])


def bytes_to_hex(ciphertext):
    """Преобразование байтов в строку шестнадцатеричных значений."""
    return ''.join(f"{byte:02x}" for byte in ciphertext)


def main():
    # Фиксированный ключ
    key = b"AleXX"

    # Ввод сообщения
    message = input("Введите сообщение для шифрования: ").encode('utf-8')

    # Шифрование
    ciphertext = encrypt(message, key)

    # Преобразование в шестнадцатеричный формат
    hex_ciphertext = bytes_to_hex(ciphertext)
    print(f"Зашифрованное сообщение (в hex): {hex_ciphertext}")


if __name__ == "__main__":
    main()