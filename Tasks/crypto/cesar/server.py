# coding=utf-8

import socket
import random
import string

def generate_random_flag():
    random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return f"Flag{{{random_chars}}}"

def handle_client(client_socket):
    request = client_socket.recv(1024).decode('utf-8').strip()
    
    if request == "Svyatoslav":
        response = "Flag{it_is_eazy_FlaGG}"
    else:
        response = generate_random_flag()
    
    client_socket.send(response.encode('utf-8'))
    client_socket.close()

def start_server(host='0.0.0.0', port=5555):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[*] Listening on {host}:{port}")

    while True:
        client_socket, addr = server.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
        handle_client(client_socket)

if __name__ == "__main__":
    start_server()
