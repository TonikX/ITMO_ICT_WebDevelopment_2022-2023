#This is Laboratory work #1

> Quick links to needed tasks are on your right
 
`server.py` - server side of the task

`client.py` - client side of the task

`*.html` - html files for tasks

---

##**Task 1**

- `server.py`

```python
import socket
import time

LOCALHOST = "127.0.0.1"
PORT = 3000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
server.listen(1)
server.setblocking(False)
print("Сервер запущен!")

while True:
    try:
        clientSock, clientAddress = server.accept()
        server.setblocking(True)
        data = clientSock.recv(4096)
        msg = data.decode("utf-8")
        print(msg)
        server.close()
        break
    except socket.error:
        print("Ожидаю")
        time.sleep(1)
    except KeyboardInterrupt:
        server.close()
        break
```

- `client.py`

```python
import socket

LOCALHOST = "127.0.0.1"
PORT = 3000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((LOCALHOST, PORT))
client.send(b"Hello, world!")
client.close()
```

---

##**Task 2**

- `server.py`

```python
import socket
import time

LOCALHOST = "127.0.0.1"
PORT = 3000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
server.listen(5)
print("Сервер запущен!")

while True:
    try:
        clientSock, clientAddress = server.accept()
        print('Клиент подключился с IP ' + str(clientAddress))
        while True:
            data = clientSock.recv(4096)
            msg = data.decode("utf-8")
            if msg == "989796":
                clientSock.send(
                    "Введите длинны оснований трапеции и высоту трапеции в таком формате 'a b h'\n".encode()
                )
                continue
            req = msg.split()
            res = (int(req[0]) + int(req[1])) * int(req[2]) / 2
            res = str.encode(str(res))
            clientSock.send(res)
            break
        server.close()
        break
    except socket.error:
        print("Ожидаю")
        time.sleep(1)
```

- `client.py`

```python
from socket import *
import sys

LOCALHOST = "127.0.0.1"
PORT = 3000

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.connect((LOCALHOST, PORT))
tcp_socket.send("989796".encode())
res = tcp_socket.recv(4096)
res = res.decode('utf-8')


data = input(res)
if not data:
    tcp_socket.close()
    sys.exit(1)

while True:
    data = str.encode(data)
    tcp_socket.send(data)
    data = tcp_socket.recv(4096)
    data = data.decode("utf-8")
    print(data)
    tcp_socket.close()
    break
```

---

##**Task 3**

- `server.py`

```python
import socket

LOCALHOST = "127.0.0.1"
PORT = 3000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))
response_type = 'HTTP/1.1 200 OK\n'
headers = 'Content/Type: text/html\n'
server.listen(1)
print("Сервер запущен!")

while True:
    client, (clientSock, clientAddress) = server.accept()
    print('Клиент подключился с IP "' + str(clientSock) + ':' + str(clientAddress) + '"')
    while True:
        data = client.recv(4096)
        req = data.decode()
        if req == "989796":
            client.send(
                response_type.encode()
            )
            continue
        elif req == 'exit':
            client.close()
            print("Отключение от клиента")
            break
        elif req == 'index.html':
            f = open('file_test_1.html', 'r')
            body = f.read()
            res = response_type + headers + body
            client.send(res.encode())
        else:
            client.send('Я не понимаю твой запрос'.encode())
    print("Выключение сервера")
    break
server.close()
```

- `client.py`

```python
from socket import *
import webbrowser

LOCALHOST = "127.0.0.1"
PORT = 3000

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.connect((LOCALHOST, PORT))
tcp_socket.send("989796".encode())


while True:
    res = tcp_socket.recv(4096)
    res = res.decode()
    if res == '':
        tcp_socket.close()
        break
    data = res.split('\n')
    print(data)
    if data[0].split()[1] == '200' and len(data) == 2:
        data = input("Что вы хотите?\n")
        tcp_socket.send(data.encode())
        continue
    elif data[0].split()[1] == '200' and len(data) > 2:
        f = open('file_test_2.html', 'wb')
        f.write(data[2].encode())
        f.close()
        url = 'file://C:/Users/Никита/PycharmProjects/ITMO_ICT_WebDevelopment_2022-2023/students/K33412/Beryoza_Nikita/laboratory_work_1/file_test_2.html'
        webbrowser.open(url, new=2)
        tcp_socket.close()
        break
```

- `file_test_1.html`

```html
<html><body><h1>Works</h1></body></html>
```

---

##**Task 4**

> I made two versions of this task
> - **Without** library `Threading`
> - **With** library `Threading`

- `Task v4.1/server.py`

```python
import socket
import select

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((IP, PORT))
server_socket.listen()

sockets_list = [server_socket]
clients = {}

print(f'Сервер запущен на IP {IP}:{PORT}')


def receive_message(c_socket):
    try:
        message_header = c_socket.recv(HEADER_LENGTH)
        if not len(message_header):
            return False
        message_length = int(message_header.decode('utf-8').strip())
        return {'header': message_header, 'data': c_socket.recv(message_length)}
    except Exception as e:
        print(e)
        return False


while True:
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)
    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()
            user = receive_message(client_socket)
            if user is False:
                continue
            sockets_list.append(client_socket)
            clients[client_socket] = user
            print('Новое подключение из {}:{}, клиент: {}'.format(*client_address, user['data'].decode('utf-8')))
        else:
            message = receive_message(notified_socket)
            if message is False:
                print('Клиент {} отключился'.format(clients[notified_socket]['data'].decode('utf-8')))
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue
            user = clients[notified_socket]
            print(f'Сообщение получено от {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')
            for client_socket in clients:
                if client_socket != notified_socket:
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])
    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]
```

- `Task v4.1/client.py`

```python
import socket
import errno
import sys

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234
my_username = input("Username: ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)
username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)

while True:

    message = input(f'{my_username} > ')

    if message:
        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(message_header + message)
    try:
        while True:
            username_header = client_socket.recv(HEADER_LENGTH)
            if not len(username_header):
                print('Connection closed by the server')
                sys.exit()

            username_length = int(username_header.decode('utf-8').strip())
            username = client_socket.recv(username_length).decode('utf-8')

            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')
            print(f'{username} > {message}')

    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error: {}'.format(str(e)))
            sys.exit()
        continue

    except Exception as e:
        print('Reading error: '.format(str(e)))
        sys.exit()
```

- `Task v4.2/server.py`

```python
import socket
import select
import threading

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((IP, PORT))
server_socket.listen()

connections = []
addresses = []

print(f'Сервер запущен на IP {IP}:{PORT}')


def accept_connections():
    global server_socket
    while True:
        new_connection, new_address = server_socket.accept()
        connections.append(new_connection)
        addresses.append(new_address)
        print("[!] Подключение " + str(new_address[0]) + ":" + str(new_address[1]))


def handler(connection):
    while True:
        msg = input("[+] Type your message > ")
        if len(msg) > 0:
            try:
                connection.send(msg.encode())
            except Exception as error:
                print("Невозможно отправить сообщение из-за:\n" + str(error))
        if msg == "back":
            main()
            break


def recv():
    while True:
        for i, x in enumerate(connections):
            try:
                print(x.recv(1024).decode())
            except:
                del connections[i]
                del addresses[i]


def list_connections():
    global connections
    res = ""
    for i, cc in enumerate(connections):
        try:
            cc.send("Новое подключение".encode())
            res = str(addresses[i][0]) + ":" + str(addresses[0][1]) + "\n"
        except Exception as error:
            print(str(error))
            pass
    return res


def main():
    t1 = threading.Thread(target=accept_connections)
    t1.daemon = True
    t2 = threading.Thread(target=recv)
    t1.start()
    t2.start()
    while True:
        req = input("[+] main > ")
        if req == 'list':
            print(list_connections())
        if req[:7] == "select ":
            handler(connections[int(req[8:])])


main()
```

- `Task v4.2/client.py`

```python
import socket
import threading

host = '127.0.0.1'
port = 1234
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((host, port))


def sender():
    global server
    while True:
        msg = input("[+] Type your message > ")
        if len(msg) > 0:
            server.send(msg.encode())


def recv():
    while True:
        print(server.recv(1024).decode())


if __name__ == "__main__":
    t = threading.Thread(target=recv)
    t.start()
    sender()
```

---

##**Task 5**

- `server.py`

```python
import socket

LOCALHOST = "127.0.0.1"
PORT = 3000
OK_STATUS = "HTTP/1.1 200 OK\n"
BAD_STATUS = "HTTP/1.1 500 BAD\n"
CLOSING_SOCKET = "Socket Closed\n"
database = []


def run_server():
    serv_sock = create_serv_sock()
    while True:
        client_sock = accept_client_conn(serv_sock)
        serve_client(client_sock)


def create_serv_sock():
    serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serv_sock.bind((LOCALHOST, PORT))
    serv_sock.listen(10)
    print(f"Сервер запущен на порту > {LOCALHOST}:{PORT}")
    return serv_sock


def accept_client_conn(serv_sock):
    client_sock, client_addr = serv_sock.accept()
    print(f'Клиент подключился с порта > {client_addr[0]}:{client_addr[1]}')
    return client_sock


def serve_client(client):
    data = client.recv(4096).decode()
    if data is None:
        print(f'Клиент неожиданно отключился')
        return
    response = handle_request(data)
    client.send(response.encode())


def parse_request(data):
    try:
        req = data[:data.index("\r\n")]
    except ValueError:
        req = data
        return req, "", ""
    if "\r\n\r\n" in data:
        headers, body = data[data.index("\r\n") + 1:].split("\r\n\r\n")
    else:
        headers, body = data[data.index("\r\n") + 1:], ""
    return req, headers, body


def parse_body(body):
    body_dict = {}
    for elem in body.split('&'):
        name = elem[:elem.index('=')]
        value = elem[elem.index('=') + 1:].replace('+', ' ')
        body_dict[name] = value
    return body_dict


def handle_request(data):
    req, headers, body = parse_request(data)
    headers += "\nAccess-Control-Allow-Origin: *"
    method, url, ver = req.split()
    response = f"{ver} 200 OK\r\n"
    error_response = f"{ver} 400\r\n\r\nBad request"
    if method == 'GET' and url == '/index':
        with open('index.html') as f:
            response += f.read()
    elif method == 'GET' and url == '/table':
        with open('table.html') as f:
            lines = f.readlines()
        table = [f"<tr><td>{s}</td><td>{g}</td></tr>" for s, g in database]
        # response += headers + '\r\n'.join(lines[:8]) + '\r\n'.join(table) + '\r\n'.join(lines[8:])
        response += headers + '\r\n\r\n' + '\r\n'.join(table)
        print("Response\n", response)
    elif method == 'POST' and url == '/send':
        parsed_body = parse_body(body)
        database.append((parsed_body['subject'], parsed_body['grade']))
        return response
    else:
        return error_response
    return response


if __name__ == '__main__':
    run_server()
```

- `index.html`

```html
<!DOCTYPE html>
<html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Task 5</title>
    </head>
    <body>
        <form method="post" action="#" onsubmit="submitForm();return false;">
            <label for="subject">Предмет</label>
            <input type="text" name="subject" id="subject"/>
            <label for="grade">Оценка</label>
            <input type="number" name="grade" id="grade"/>
            <input type="submit">
        </form>
        <div onclick="fetchTable()">Посмотреть таблицу</div>
        <table align="center" width="20%" border="1" id="tableId"></table>
    </body>
    <script>
        function submitForm() {
            let http = new XMLHttpRequest();
            http.open("POST", "http://127.0.0.1:3000/send", true);
            let params = "grade="
                + document.getElementById("grade").value
                + "&subject=" + document.getElementById("subject").value;
            http.send(params);
        }
        async function fetchTable() {
            await fetch('http://localhost:3000/table')
                .then((response) => {
                    response.text()
                }).then((data) => {
                    console.log(data)
                })
        }
    </script>
</html>
```