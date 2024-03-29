import socket

# Создание сокета
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключение к серверу
server_address = ('localhost', 12345)
client_socket.connect(server_address)

try:
    # Отправка данных серверу
    message = input("Введите сообщение для сервера: ")
    client_socket.sendall(message.encode())

    # Получение ответа от сервера
    data = client_socket.recv(1024)
    print(f"Получено от сервера: {data.decode()}")

finally:
    # Закрытие соединения
    client_socket.close()
