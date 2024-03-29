import socket
import threading

def handle_client(connection, client_address):
    print(f"Подключение от {client_address}")
    try:
        while True:
            data = connection.recv(1024)
            if data:
                print(f"Получено: {data.decode()}")

                # Отправка данных обратно клиенту
                connection.sendall(data)
            else:
                break
    finally:
        connection.close()

# Создание сокета
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязка сокета к адресу и порту
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Начало прослушивания
server_socket.listen(5)

print("Сервер запущен и ожидает подключения...")

while True:
    connection, client_address = server_socket.accept()
    # Создание нового потока для взаимодействия с клиентом
    client_thread = threading.Thread(target=handle_client, args=(connection, client_address))
    client_thread.start()
