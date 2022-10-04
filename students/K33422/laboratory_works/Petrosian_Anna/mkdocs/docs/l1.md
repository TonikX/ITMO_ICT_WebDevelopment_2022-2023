# Лабораторная работа 1

## Задание 1

Реализовать клиентскую и серверную часть приложения. Клиент отсылает серверу сообщение «Hello, server». Сообщение должно отразиться на стороне сервера. Сервер в ответ отсылает клиенту сообщение «Hello, client». Сообщение должно отобразиться у клиента.

*Клиент и сервер посылают друг другу сообщения. DGRAM заходил в бесконечную загрузку, поэтому выполнено с помощью TCP.*

    #server
    
    import socket
    port = 3968
    host = socket.gethostbyname("localhost")
    mess="Hello, client"
    message = bytes(mess, 'utf-8')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) #use TCP
    #int sock = 1
    sock.bind((host, port)) #связь сокета с хостом и портом
    sock.listen(10) #n listenings
    cl_sock, addr = sock.accept() #приём и посылка данных
    data = cl_sock.recv(1024) #порция данных
    print(data.decode())
    cl_sock.send(message)
    sock.close() #закрыли соединени

    #client
    import socket
    port = 3968
    host = socket.gethostbyname("localhost")
    mess="Hello, server"
    message = bytes(mess, 'utf-8')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #_stream for tcp dgram udp
    sock.connect((host, port))
    sock.send(message)
    data = sock.recv(1024)
    print(data.decode())
    sock.close()


## Задание 2
Реализовать клиентскую и серверную часть приложения. Клиент запрашивает у сервера выполнение математической операции, параметры, которые вводятся с клавиатуры. Сервер обрабатывает полученные данные и возвращает результат клиенту - Решить квадратное уравнение

*Сервер получает от клиента запрос на решение квадратного уравнение, вводя его коэффициенты с клавиатуры. Сервер получает эти данные и передаёт корни уравнения (или сообщение об их отсутствии) в виде сообщения*

    import socket
    from math import sqrt
    port = 3968
    host = socket.gethostbyname("localhost")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) #use TCP
    sock.bind((host, port)) #связь сокета с хостом и портом
    sock.listen(10) #n listenings
    cl_sock, addr = sock.accept() #приём и посылка данных
    data=cl_sock.recv(1024)
    print(data)
    a, b,c = map(lambda x: int(x), data.split())
    #conn.sendall('Wrong input format!\n'.encode())

	D = b**2 - 4 * a * c
	if D > 0:
	x1, x2 = (-b + sqrt(D)) / (2 * a), (-b - sqrt(D)) / (2 * a)
	cl_sock.sendall(f'Корни уравнения: {x1}, {x2}\n'.encode())
	elif D == 0:
	x = (-b) / (2 * a)
	cl_sock.sendall(f'Корень уравнения: {x}\n'.encode())
	else:
	cl_sock.sendall(f'Нет корней'.encode())
	#message = bytes(mess, 'utf-8')
	print(data.decode())
	sock.close() #закрыли соединение

	#client
	import socket
	port = 3968
	host = socket.gethostbyname("localhost")
	#host="127.0.0.1"
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #_stream for tcp dgram udp
	sock.connect((host, port))
	#data = sock.recv(1024)
	a=input('Type the first variable x^2 ')
	b=input('Type the second linear vatiable x ')
	c=input('Type the third variable ')
	#sock.send(int.from_bytes([a,b,c],byteorder='big',signed=True))
	equation=a +" "+ b +" "+ c
	sock.send(equation.encode('utf-8'))
	#sock.send(a,b,c)
	data = (sock.recv(1024)).decode('utf-8')
	print(data)
	sock.close()

## Задание 3
Реализовать серверную часть приложения. Клиент подключается к серверу. В ответ клиент получает http-сообщение, содержащее html-страницу, которую сервер подгружает из файла index.html.

*После подключения к серверу клиент получает в ответ http-странцу, содержание которой подгружается из index.html. Страница доступна по адресу http://localhost:3968*

    #server
	import socket
	port = 3968
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
	
	#client
	import socket
	port = 3968
	host = socket.gethostbyname("localhost")
	mess="Hello, server"
	message = bytes(mess, 'utf-8')
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #_stream for tcp dgram udp
	sock.connect((host, port))
	sock.send(message)
	data = sock.recv(1024)
	print(data.decode())
	sock.close()
	
	#index
	<!DOCTYPE html>
	<html lang="fr">
	<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	</head>
	<body>
	<h1><span style="color:rgb(255, 97, 163)"><b>Mon premier site</b></span></h1>
	<p>Pour naviguer sur la page veiller cliquer:</p>
	<ul>
	<li><a href="#inf">Infos personnelles</a></li>
	<li><a href="#Compétences">Compétences</a></li>
	<li><a href="#Centre d'interêts">Centre d'interêts</a></li>
	</ul>
	<hr>
	<h2><a name="inf"><span style="color:#7B68EE"><b>Infos personnelles</b></span></a></h2>
	<hr>
	<p>Salut! Je m'appelle <span style="color:#C71585">Anne</span>, j'ai 19 ans.</p>
	<p>Je fais mes études à l'université de filière technique et j'aime retoucher les photos, surtout des photos des patineurs artistiques.<br></p>
	<hr>
	<h2><a name="Compétences"><span style="color:#7B68EE"><b>Compétences</b></span></a></h2>
	<p><hr>Tu peux aussi me connecter si tu as besoin de:
	<ul type="circle">
	<li>construire <span style="color:#C71585">les sites</span></li>
	<li>consulter sur <span style="color:#C71585">les devoirs à domicile</span></spqn></li>
	<li>retoucher <span style="color:#C71585">les photos</span></li>
	</ul> <hr>
	</p>
	<h2><a name="Centre d'interêts"><span style="color:#7B68EE"><b>Centre d'interêts</b></span></a></h2>
	<hr>
	<ul type="circle">
	<li>Composition de <span style="color:#C71585">la musique</span></li>
	<li>Apprentissage <span style="color:#C71585">des langues étrangères</span></li>
	<li>Application <span style="color:#C71585">d'intélligence artificielle à la médecine</span></li>
	</ul>
	<hr>
## Задание 4
Реализовать многопользовательский чат

*В список заносятся клиенты: подключаясь к серверу, клиент получает сообщение о необходимости ввести имя, после чего появляется сообщение о том, что пользователь присоединился. С этого момента этот пользователь может отправлять сообщения. Далее новый пользователь проходит те же этапы.*

*Функция broadcast - посылает сообщение подключённым клиентам
Функция handle и exitclient - отключает клиент при вводе exit и прощается с клиентом
Функция receive -  выводит сообщения с именем отправителя или выводит сообщение об отключении клиента
Функция send - посылает серверу данные о сообщении*

    #server
    import socket
    import threading

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 3968))
    sock.listen()

    interlocuteurs = []
    usernames = []

    def broadcast(message):
        for sock_int in interlocuteurs:
            sock_int.send(message)

    def handle(sock_int):
        while True:
            try:
                message = sock_int.recv(4096)

            if "exit" in message.decode('utf-8'):
                exitclient(sock_int)
                break

            broadcast(message)

        except Exception as e:
            exitclient(sock_int)
            break

    def exitclient(sock_int):
        index = interlocuteurs.index(sock_int)
        interlocuteurs.remove(sock_int)
        sock_int.close()
        username = usernames[index]
        broadcast(f'bye, {username}'.encode('utf-8'))
        usernames.remove(username)

    def receive():
        while True:
            try:
                sock_int, client_address = sock.accept()
                print(f'connection established {client_address}')

                sock_int.send('NICKNAME'.encode('utf-8'))
                username = sock_int.recv(4096).decode('utf-8')
                interlocuteurs.append(sock_int)
                usernames.append(username)
                broadcast(f'{username} joined'.encode('utf-8'))

                handle_thread = threading.Thread(target=handle, args=(sock_int,))
                handle_thread.start()

        except KeyboardInterrupt:
            print ("server closed")
            sock.close()
            break

        except Exception as e:
            print('Exception:', e)
            broadcast(f'')

    receive()
	
	#client
	import socket
    import threading

    username = input("your username: ")

    sock_int = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_int.connect(('127.0.0.1', 3968))


    def receive():
        while True:
            try:
                message = sock_int.recv(4096).decode('utf-8')
                if message == 'NICKNAME':
                    sock_int.send(username.encode('utf-8'))
                elif username in message:
                    print(message.replace(f"{username} >", 'You >', 1))
                else:

                    print(message)

            except Exception as e:
                print(e)
                sock_int.close()
                break


    def send():
        while True:
            message = input()
            sock_int.send(f'{username} > {message}'.encode('utf-8'))

    send_thread = threading.Thread(target=send)
    recv_thread = threading.Thread(target=receive)
    send_thread.start()
    recv_thread.start()


## Задание 5
Необходимо написать простой web-сервер для обработки GET и POST http запросов средствами Python и библиотеки socket

*server.py Сначала задаются параметры сервера, далее запуск на сокете и обработка клиентского подключения и обработка нужной формы*
*insert.html - форма для записи и отображения информации и оценок по дисциплине. Чтобы запросить журнал оценок, нужно добавить /journal в адресе формы*

    #server.py
    import socket
    class MyHTTPServer:
    # Параметры сервера
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.grade = []

    # 1. Запуск сервера на сокете, обработка входящих соединений
    def serve_forever(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.host, self.port))
        sock.listen()
        while True:
            client_socket, _ = sock.accept()
            self.serve_client(client_socket)

    # 2. Обработка клиентского подключения
    def serve_client(self, client_socket):
        data = client_socket.recv(4096).decode('utf-8')
        request = self.parse_request(data)
        response = self.handle_request(request)
        if response:
            client_socket.send(response.encode('utf-8'))
            client_socket.close()

    # 3. функция для обработки заголовка http+запроса
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

    # 4. Функция для обработки url в соответствии с нужным методом
    def handle_request(self, request):
        print(request)
        response = f"{request['version']} 200 OK\n\n"
        if request["url"] == "/":
            if request["method"] == "POST":
                 self.grade.extend(request["parametrs"])
            if request["method"] == "GET" or "POST":
                with open('insert.html') as f:
                    response += f.read()
                    return response
        if request["url"] == "/journal":
            response += "<html><head><title>List grades</title></head><body>"
            for s in self.grade:
                response += f"<p>{s} </p>"
            response += "</body></html>"
            return response


    if __name__ == "__main__":
    host = 'localhost'
    port = 3968
    #name
    myserver = MyHTTPServer(host, port)
    try:
        myserver.serve_forever()
    except KeyboardInterrupt:
        pass

    #insert.py
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <p>Enter data to fill out the journal:
            <form action="/" method="post">
                <label for="subject">Enter the name of the subject:</label>
                <input type="text" placeholder="subject" name="subject" id="subject"/>
                <label for="grade">Enter the mark:</label>
                <input type="number" placeholder="mark" name="grade" id="grade"/>
                <button>Send</button>
            </form>
        </p>
    </body>
    </html>



    
