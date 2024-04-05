import socket

# Создание сокета
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязка сокета к адресу и порту
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Начало прослушивания
server_socket.listen(1)

print("Сервер запущен и ожидает подключения...")

while True:
    # Принятие входящего подключения
    connection, client_address = server_socket.accept()
    print(f"Подключение от {client_address}")

    try:
        while True:
            # Чтение данных от клиента
            data = connection.recv(1024)
            if data:
                print(f"Получено: {data.decode()}")

                # Отправка данных обратно клиенту
                connection.sendall(data)
            else:
                break
    finally:
        # Закрытие соединения
        connection.close()
