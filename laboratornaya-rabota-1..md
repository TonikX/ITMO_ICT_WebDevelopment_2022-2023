---
description: 'Лабораторная работа 1: Исползавание Сокетов.'
---

# Лабораторная работа 1.

### Часть 1: Connexion to the server

* server.py

```
import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = ":(DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Hello, Client".encode(FORMAT))

    conn.close()
        

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start() 
```

* client.py

```
import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = ":(DISCONNECT"
SERVER = "192.168.1.5"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("Hello, server")
input()
send("Fine and you ?")
input()
send("Good")

send(DISCONNECT_MESSAGE)
```

### Часть 2: Математические операции

* server.py

```
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

* client.py

```
import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 8000))
data = input("Введите a и b через пробел: ")
conn.send(data.encode("utf-8"))
result = conn.recv(16384).decode("utf-8")
print("c = ", result)
conn.close()
```

### Часть 3: HTML-страница

* server.py

```
import socket

conn = socket.socket()

conn.connect(("192.168.1.5", 8000))
result = conn.recv(10000)
print(result.decode())
conn.close()
```

* client.py

```
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.1.5'
port = 8000
server.bind((host, port))
server.listen(1)

while True:
    conn, addr = server.accept()

    page = open('index.html')
    content = page.read()
    page.close()

    response = 'HTTP/1.0 200 OK\n\n' + content
    conn.sendall(response.encode())
    conn.close()
```

* index.html

```
<!DOCTYPE html>

<head>
    <title>My Website</title>
    <style>
        *,
        html {
            margin: 0;
            padding: 0;
            border: 0;
        }

        html {
            width: 100%;
            height: 100%;
        }

        body {
            width: 100%;
            height: 100%;
            position: relative;
            background-color: rgb(236, 152, 42);
        }

        .center {
            width: 100%;
            height: 50%;
            margin: 0;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            color: white;
            font-family: "Trebuchet MS", Helvetica, sans-serif;
            text-align: center;
        }

        h1 {
            font-size: 144px;
        }

        p {
            font-size: 64px;
        }
    </style>
</head>

<body>
    <div class="center">
        <h1>Hello Again!</h1>
        <p>This is served from a file</p>
    </div>
</body>

</html>
```

### Часть 4: Многоползоваческий чат

* server.py

```
import socket, time

host = socket.gethostbyname(socket.gethostname())
port = 9090

clients = []

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))

quit = False
print("[ Server Started ]")

while not quit:
	try:
		data, addr = s.recvfrom(1024)

		if addr not in clients:
			clients.append(addr)

		itsatime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())

		print("["+addr[0]+"]=["+str(addr[1])+"]=["+itsatime+"]/",end="")
		print(data.decode("utf-8"))

		for client in clients:
			if addr != client:
				s.sendto(data,client)
	except:	
		print("\n[ Server Stopped ]")
		quit = True
		
s.close()
```

* client.py

```
import socket, threading, time

key = 8194

shutdown = False
join = False

def receving (name, sock):
	while not shutdown:
		try:
			while True:
				data, addr = sock.recvfrom(1024)
				#print(data.decode("utf-8"))

				# Begin
				decrypt = ""; k = False
				for i in data.decode("utf-8"):
					if i == ":":
						k = True
						decrypt += i
					elif k == False or i == " ":
						decrypt += i
					else:
						decrypt += chr(ord(i)^key)
				print(decrypt)
				# End

				time.sleep(0.2)
		except:
			pass
host = socket.gethostbyname(socket.gethostname())
port = 0

server = ("192.168.1.5",9090)

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)

alias = input("Name: ")

rT = threading.Thread(target = receving, args = ("RecvThread",s))
rT.start()

while shutdown == False:
	if join == False:
		s.sendto(("["+alias + "] => join chat ").encode("utf-8"),server)
		join = True
	else:
		try:
			message = input()

			# Begin
			crypt = ""
			for i in message:
				crypt += chr(ord(i)^key)
			message = crypt
			# End

			if message != "":
				s.sendto(("["+alias + "] :: "+message).encode("utf-8"),server)
			
			time.sleep(0.2)
		except:
			s.sendto(("["+alias + "] <= left chat ").encode("utf-8"),server)
			shutdown = True

rT.join()
s.close()
```

### Часть: GET и POST запросы

* server.py

```
import socket

lessons = [
  {'name': 'Python', 'desc': 'Client/Server', 'marks' : [4,5]}
]

def post_func(post_msg):
  info = post_msg.split('&')
  return [info[0][7:], info[1][5:], [int(i) for i in info[2][6:].split('%2C')]]

def get():
  html = '<ol>'
  for lesson in lessons:
    html += '<li>'
    html += f'<h1>Lesson: {lesson["name"]}</h1>'
    for mark in lesson['marks']:
      html += f'<p>grade: {mark}</p>'
    html += '</li>'
  html += '</ol>'
  return html

def add():
  form = """
  <form action="/" method="post">
    <P>Lesson: </p>
    <input type="text" name="lesson" value="math"/>
    <P>Description: </p>
    <input type="text" name="desc" value="numbers"/>
    <P>Grades: </p>
    <input type="text" name="marks" value="5,5,5"/>
    <br/>
    <input type="submit" value="Add lesson"/>
  </form>"""
  return form

def start_server():
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind(('127.0.0.1', 4245))
  server.listen()

  while True:
    client, addr = server.accept()

    with client:
      request = client.recv(1024).decode()
      method = request.split(' ')[0]
      message = request.split(' ')[1][1:-1]
      setting = 'HTTP/1.1 200 OK\r\nContent-Type: text.html; charset=UTF-8\r\n\r\n'
      html = '<html><head><title>Website</title></head><body>'
      html += """
      <form method="get">
        <input type="submit" formaction="add" value="Add" />
        <input type="submit" formaction="get" value="Show" />
      </form>
      """
      if method == 'GET':
        if message == 'get':
          html += get()
        elif message == 'add':
          html += add()
      else:
        post = post_func(request.split(' ')[-1].split('\r\n\r\n')[1])
        lessons.append({'name': post[0], 'desc': post[1], 'marks' : post[2]})

      html += "</body></html>"
      client.send(setting.encode('utf-8') + html.encode('utf-8'))  

start_server();
```
