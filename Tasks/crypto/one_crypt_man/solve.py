def xor_bytes(b1, b2):
    """Выполняет операцию XOR между двумя байтовыми строками."""
    return bytes([a ^ b for a, b in zip(b1, b2)])


def find_key(ciphertext1, known_plaintext):
    """
    Восстанавливает ключ на основе зашифрованного сообщения и известного открытого текста.
    :param ciphertext1: Зашифрованное сообщение (в байтах).
    :param known_plaintext: Известная часть открытого текста (в байтах).
    :return: Восстановленный ключ (в байтах).
    """
    return xor_bytes(ciphertext1[:len(known_plaintext)], known_plaintext)


def decrypt(ciphertext, key):
    """
    Расшифровывает сообщение с использованием ключа.
    :param ciphertext: Зашифрованное сообщение (в байтах).
    :param key: Ключ (в байтах).
    :return: Расшифрованное сообщение (в байтах).
    """
    repeated_key = (key * (len(ciphertext) // len(key) + 1))[:len(ciphertext)]
    return xor_bytes(ciphertext, repeated_key)


def main():
    # Два зашифрованных сообщения в hex-формате
    hex_ciphertext1 = "090909343761180d312b610516783961070021"
    hex_ciphertext2 = "2700043f231219353d0a200000207c240f373d2c0a291c25"

    # Преобразуем hex-строки в байты
    ciphertext1 = bytes.fromhex(hex_ciphertext1)
    ciphertext2 = bytes.fromhex(hex_ciphertext2)

    # Известное начало первого сообщения
    known_plaintext = b"Hello"

    # Восстанавливаем ключ
    key = find_key(ciphertext1, known_plaintext)
    print(f"Восстановленный ключ: {key.decode('utf-8', errors='replace')}")

    # Расшифровываем второе сообщение
    decrypted_message2 = decrypt(ciphertext2, key)
    print(f"Расшифрованное второе сообщение: {decrypted_message2.decode('utf-8', errors='replace')}")


if __name__ == "__main__":
    main()