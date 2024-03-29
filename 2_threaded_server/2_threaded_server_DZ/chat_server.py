import socket
import threading


clients = {}


message_history = []

def handle_client(client_socket, client_address):
    # Запрос имени пользователя
    client_socket.sendall("Введите ваше имя: ".encode())
    username = client_socket.recv(1024).decode().strip()

    # Добавление пользователя в словарь клиентов
    clients[client_socket] = username

    # Приветствие нового пользователя
    welcome_message = f"Добро пожаловать, {username}! Для выхода из чата введите 'quit'."
    client_socket.sendall(welcome_message.encode())

    # Отправка истории сообщений новому пользователю
    for message in message_history:
        client_socket.sendall(message.encode())

    while True:
        try:
            # Получение сообщения от клиента
            message = client_socket.recv(1024).decode().strip()
            if message == 'quit':
                client_socket.sendall("quit".encode())
                del clients[client_socket]
                client_socket.close()
                break
            else:
                # Добавление сообщения в историю
                message_history.append(f"{username}: {message}")

                # Рассылка сообщения всем клиентам, кроме отправителя
                for sock, name in clients.items():
                    if sock != client_socket:
                        sock.sendall(f"{username}: {message}".encode())

        except ConnectionResetError:
            # Обработка случая, когда клиент неожиданно отключается
            del clients[client_socket]
            client_socket.close()
            break

def main():
    # Создание сокета
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Привязка сокета к адресу и порту
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    # Начало прослушивания
    server_socket.listen(5)
    print("Сервер запущен и ожидает подключения...")

    while True:
        # Принятие входящего подключения
        client_socket, client_address = server_socket.accept()

        # Создание нового потока для обработки клиента
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    main()
