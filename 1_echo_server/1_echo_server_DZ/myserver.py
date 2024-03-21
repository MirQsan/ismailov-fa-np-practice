import socket
import sys
import time

s = socket.socket()
try:
    s.bind(('localhost', 9090))
    print('(Запуск сервера)')
    try:
        s.listen(1)
        print('(Начало прослушивания порта)')
        try:
            client, address = s.accept()
            print('(Подключение клиента)')
            print(f"------CLIENT'S ADDRESS: {address}")
            while True:
                msg = ''
                try:
                    data = client.recv(1024)
                    print('(Прием данных от клиента)')
                    if not data:
                        break
                    msg += data.decode()
                    print(f"CLIENT'S MESSAGE: {msg}")
                    try:
                        client.send(data)
                        print('(Отправка данных клиенту)')
                        if msg=='exit':
                            break
                            client.close()
                    except:
                        print('(Не удалось отправить данные клиенту)')
                except:
                    print('(Не удалось получить данные от клиента)')
                    break
                

        except:
            print('(Не удалось подключить клиента)')
    except:
        print('(Не удалось начать прослушивание порта)')
except:
    print('Ошибка запуска сервера')


print('(Отключение клиента) ')
print('(Остановка сервера) ')