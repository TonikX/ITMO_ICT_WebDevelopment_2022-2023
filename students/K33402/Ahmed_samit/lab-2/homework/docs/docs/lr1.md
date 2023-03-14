Лабораторная работа 1

Задание 1

* client.py 
``` py
import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 1010))
conn.send(b"Hello, server! \n")
data = conn.recv(16384).decode("utf-8")
print("data: ", data)
conn.close()

#server
import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 1010))
conn.listen(10)
while True:
    try:
        clientsocket, address = conn.accept()
        data = clientsocket.recv(16384).decode("utf-8")
        print("data: ", data)
        clientsocket.send(b"Hello, client! \n")
    except KeyboardInterrupt:
        conn.close()
        break
```

Задание 2
``` py
#client
import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 8000))
data = input("Введите a и b через пробел: ")
conn.send(data.encode("utf-8"))
result = conn.recv(16384).decode("utf-8")
print("c = ", result)
conn.close()

#server

import socket
from math import sqrt

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 8000))
conn.listen(10)
while True:
    try:
        clientsocket, address = conn.accept()
        data = clientsocket.recv(16384).decode("utf-8")
        a, b = map(lambda x: int(x), data.split())
        print("a = ", a, ", b = ", b)
        c = sqrt(a ** 2 + b ** 2)
        c = str(c).encode()
        clientsocket.send(c)
    except KeyboardInterrupt:
        conn.close()
        break
```
Задание 3
``` py
# client
import socket
 
port = 1025
host = socket.gethostbyname("localhost")
mess="Hello, server"
message = bytes(mess, 'utf-8')
#host="127.0.0.1"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #_stream for tcp dgram udp
 
sock.connect((host, port))
sock.send(message)
 
data = sock.recv(1024)
print(data.decode())
#print (message)
sock.close()

#server
import socket

port = 1025
host = socket.gethostbyname("localhost")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
sock.bind((host, port))

sock.listen(10)
sock, addr = sock.accept()
sock.recv(16384)

response_type = "HTTP/1.0 200 OK\n"
headers = "Content-Type: text/html\n\n"
page = open('index.html','r')
body = page.read()
resp = response_type + headers + body
sock.send(resp.encode("utf-8"))
page.close()
sock.close()
#index.html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1><span style="color:rgb(255, 97, 163)"><b> ITMO_ICT_WebDevelopment_2022-2023</b></span></h1>
    <p></p>
    <ul>
        <li><a href="#inf">Infos </a></li>
        <li><a href="#Compétences">lab</a></li>
        <li><a href="#rapport"></a></li>
    </ul>
    <hr>    
    <h2><a name="inf"><span style="color:#7B68EE"><b>Django</b></span></a></h2>
    <hr>
    <p>Salut!  <span style="color:#C71585">Django</span>Je suis front-end developer</p> 

    <p>Je suis front-end developer<br></p> 
    <hr>
    <h2><a name="Compétences"><span style="color:#7B68EE"><b>Vue.js</b></span></a></h2>
    <p><hr>Tu peux aussi me connecter si tu as besoin de:
        <ul type="circle">
            <li>Django<<span style="color:#C71585">Django</span></li>
            <li>Django<<span style="color:#C71585">Django</span></spqn></li>
            <li>Django< <span style="color:#C71585">Django</span></li>
        </ul> <hr>
    </p>
    <h2><a name="Centre d'interêts"><span style="color:#7B68EE"><b>Vue.js</b></span></a></h2>
    <hr>
        <ul type="circle">
            <li>python <span style="color:#C71585">Html</span></li>
            <li>python <span style="color:#C71585">Css</span></li>
            <li>python <span style="color:#c71515">Css</span></li>   
        </ul>
    <hr>
```
Задание 4
```  py
#client
import socket
import threading

username = input("your username: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5011))


def receive():
    while True:
        try:
            message = client.recv(4096).decode('utf-8')
            if message == 'NICKNAME':
                client.send(username.encode('utf-8'))
            elif username in message:
                print(message.replace(f"{username} >", 'You >', 1))
            else:

                print(message)

        except Exception as e:
            print(e)
            client.close()
            break


def send():
    while True:
        message = input('')
        client.send(f'{username} > {message}'.encode('utf-8'))


send_thread = threading.Thread(target=send)
recv_thread = threading.Thread(target=receive)
send_thread.start()
recv_thread.start()
#server
import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 5011))
server.listen()

clients = []
usernames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(4096)

            if "exit" in message.decode('utf-8'):
                exitclient(client)
                break

            broadcast(message)

        except Exception as e:
            exitclient(client)
            break


def exitclient(client):
    index = clients.index(client)
    clients.remove(client)
    client.close()
    username = usernames[index]
    broadcast(f'{username} left'.encode('utf-8'))
    usernames.remove(username)


def receive():
    while True:
        try:
            client, client_address = server.accept()
            print(f'Accepted connection from {client_address}')

            client.send('NICKNAME'.encode('utf-8'))
            username = client.recv(4096).decode('utf-8')
            clients.append(client)
            usernames.append(username)
            broadcast(f'{username} joined'.encode('utf-8'))

            handle_thread = threading.Thread(target=handle, args=(client,))
            handle_thread.start()

        except KeyboardInterrupt:
            print ("Closing server")
            server.close()
            break
        except Exception as e:
            print('Exception:', e)
            broadcast(f'')


receive()
```
Задание 5
``` py
import socket


class MyHTTPServer:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.mark = []

    def serve_forever(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.host, self.port))
        sock.listen(8)
        print(f"\nThe server is running : http://{host}:{port}\n")
        while True:
            client_socket, _ = sock.accept()
            self.serve_client(client_socket)

    def serve_client(self, client_socket):
        data = client_socket.recv(4096).decode('utf-8')
        request = self.parse_request(data)
        response = self.handle_request(request)
        if response:
            client_socket.send(response.encode('utf-8'))
            client_socket.close()

    def parse_request(self, data):
        data_split = data.split('\r\n')
        print(f"data split : {data_split}")
        headers = data_split[0].split()
        print(f"Headers : {headers}")
        body = data_split[-1]
        request = dict()

        if len(headers) == 3:

            request.update(
                {"method": headers[0], "url": headers[1], "version": headers[2]})

            if "&" in body:
                parametre = body.split("&")
                request.update({"parametrs": parametre})
                return request
            else:
                request.update({"parametrs": {}})
                return request
        else:
            raise Exception("Malformed request line")

    def handle_request(self, request):
        print(request)
        response = f"{request['version']} 200 OK\n\n"
        if request["url"] == "/":
            if request["method"] == "POST":
                 self.mark.extend(request["parametrs"])
            if request["method"] == "GET" or "POST":
                with open('index.html') as f:
                    response += f.read()
                    return response
        if request["url"] == "/list":
            response += "<html><head><title>List grades</title></head><body>"
            for s in self.mark:
                response += f"<p>{s} </p>"
            response += "</body></html>"
            return response


if __name__ == "__main__":
    host = 'localhost'
    port = 7890
    myserver = MyHTTPServer(host, port)
    try:
        myserver.serve_forever()
    except KeyboardInterrupt:
        pass
```
