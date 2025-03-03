import base64
import socket
import threading

def transform_string(input_string):
    # Применяем ROT13
    rot13_string = input_string.translate(str.maketrans(
        'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
        'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    ))

    # Кодируем в Base64
    base64_bytes = base64.b64encode(rot13_string.encode('utf-8'))
    base64_string = base64_bytes.decode('utf-8')

    # Преобразуем Base64-строку в шестнадцатеричный формат
    hex_string = base64_string.encode('utf-8').hex()

    return hex_string

def handle_client(client_socket, client_address):
    print(f"Подключен клиент: {client_address}")

    try:
        # Получаем данные от клиента
        data = client_socket.recv(1024).decode('utf-8').strip()
        print(f"Получены данные от {client_address}: {data}")

        # Обрабатываем команду
        if data.startswith("transform "):
            # Режим преобразования
            input_string = data[len("transform "):]
            result = transform_string(input_string)
        else:
            result = "Неверная команда. Используйте 'transform <строка>'."

        # Отправляем результат клиенту
        client_socket.send(result.encode('utf-8'))
        print(f"Отправлен результат клиенту {client_address}: {result}")

    except Exception as e:
        print(f"Ошибка при работе с клиентом {client_address}: {e}")

    finally:
        # Закрываем соединение с клиентом
        client_socket.close()
        print(f"Соединение с клиентом {client_address} закрыто")

def start_server(host='0.0.0.0', port=9999):
    # Создаем сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)  # Очередь из 5 клиентов
    print(f"Сервер запущен на {host}:{port}")

    try:
        while True:
            # Принимаем подключение
            client_socket, client_address = server_socket.accept()
            print(f"Новое подключение от {client_address}")

            # Создаем поток для обработки клиента
            client_thread = threading.Thread(
                target=handle_client,
                args=(client_socket, client_address)
            )
            client_thread.start()

    except KeyboardInterrupt:
        print("Сервер остановлен.")

    finally:
        # Закрываем серверный сокет
        server_socket.close()
        print("Серверный сокет закрыт.")

if __name__ == "__main__":
    start_server()
