import socket
from time import sleep

s = socket.socket()
try:
    s.connect(('localhost', 9090))
    print('(Соединение с сервером)')
    while True:
        msg = input('------CLIENT: ')
        try:
            s.send(msg.encode())
            print('(Отправка данных серверу)')
            try:
                data = s.recv(1024)
                print('(Прием данных от сервера)')
                print(f'------SERVER: {data.decode()}')
                if data.decode()=='exit':
                    s.close()
                    print('(Разрыв соединения с сервером)')
            except:
                print('(Не удалось получить данные от сервера)')
                break
        except:
            print('(Ошибка! Не удалось отправить данные серверу)')
            break
except:
    print('(Не удалось произвести соединение с сервером)')