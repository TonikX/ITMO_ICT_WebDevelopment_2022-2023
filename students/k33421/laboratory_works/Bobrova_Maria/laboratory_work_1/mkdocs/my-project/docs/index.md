#Лабораторные работы

##Лабораторная работа №1

### Задание №1

Реализовать клиентскую и серверную часть приложения. Клиент отсылает серверу
сообщение «Hello, server». Сообщение должно отразиться на стороне сервера.
Сервер в ответ отсылает клиенту сообщение «Hello, client». Сообщение должно
отобразиться у клиента.

Создаем два файла - для клиента и сервера.
#### client.py
Клиентское приложение, в котором создается сокет, производится подключение к серверу, посылаются ему данные, принимаются данные и закрывается соединение.

    import socket #импорт библиотеки

    conn = socket.socket(socket.SOCK_DGRAM) #создание сокета для сервера UDP
    conn.connect((socket.gethostname(), 1234)) #подключение к хосту (IP-адрес и порт)
    msg = 'Hello, server' #сообщение для сервера
    conn.send(msg.encode("utf-8")) #
    data = b"" #создание пустой байтовой строки
    tmp = conn.recv(16384) #отсюда все как обычно
    while tmp:
        data += tmp
        tmp = conn.recv(16384)
    print(data.decode("utf-8"))
    conn.close()
    
#### server.py
Сервер принимает соединение, принимает от клиента данные, возвращает их в виде строки в верхнем регистре и закрывает соединение. 

    import socket #импорт библиотеки
    sock = socket.socket(socket.SOCK_DGRAM) #создание сокета для сервера UDP
    # Для привязки используется функция bind сокета, которая принимает массив, содержащий два элемента: хост и порт.
    sock.bind((socket.gethostname(), 1234))
    sock.listen(1) #максимальное число соединений
    while True:
        try: #пока верно, выполняется блок инструкицй
        #Ф-ция ждёт появление входящего соединения и возвращает связанный с ним сокет и адрес подключившегося.
        #Адрес — массив, состоящий из IP-адреса и порта.
            conn, addr = sock.accept()
            data = conn.recv(16384) #чтение данных с определенным кол-м байт
            udata = data.decode("utf-8") #декодирование данных из bytes в строку
            print(udata)
            msg = "Hello, client" #строка для клиента
            conn.send(msg.encode("utf-8")) #отправка данных в закодированном виде, т.к. ф-ция send принимает тип bytes
            conn.close() #закрытие сокета
        except KeyboardInterrupt: #в случае ошибки, выполняется блок инструкицй
            sock.close() #закрытие сокета
        break
#### Commands

* `py -3.8 server.py` - Запуск в первом терминале.
* `py -3.8 client.py` - Запуск во втором терминале.
* `>>Hello, server` - Вывод в первом терминале.
* `>>Hello, client` - Вывод во втором терминале.

### Задание №2

Реализовать клиентскую и серверную часть приложения. Клиент запрашивает у
сервера выполнение математической операции, параметры, которые вводятся с
клавиатуры. Сервер обрабатывает полученные данные и возвращает результат
клиенту. 

Вариант:

a. Теорема Пифагора

#### client.py
Клиентское приложение, в котором создается сокет, производится подключение к серверу, посылаются ему данные, принимаются данные и закрывается соединение.

    import socket

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((socket.gethostname(), 1234))
    while True:
        data = sock.recv(1024)
        print(f"server: {data.decode()}")
        msg = input("Client: ")
        sock.send(str.encode(msg))
#### server.py
Сервер принимает соединение, принимает от клиента данные (катеты треугольника), возвращает их в виде строки в верхнем регистре (гипотенуза) и закрывает соединение. 


    import socket


    def pifagor(a, b): #функия, которая возвращает гипотенузу
        return a**2 + b**2


    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #создание сокета для сервера TCP
    sock.bind((socket.gethostname(), 1234))
    # Для привязки используется функция bind сокета, которая принимает массив, содержащий два элемента: хост и порт.
    sock.listen(1) #максимальное число соединений
    #Ф-ция ждёт появление входящего соединения и возвращает связанный с ним сокет и адрес подключившегося.
    #Адрес — массив, состоящий из IP-адреса и порта.
    conn, addr = sock.accept()
    #отправка данных в закодированном виде, т.к. ф-ция send принимает тип bytes
    conn.send(str.encode(f"Hello, client\n"
                        f"I solve Pythagorean theorem\n"
                        f"Enter A as a number\n"))
    a = "" #катет
    b = "" #катет
    c = "" #гипотенуза

    while not c:
        while not a: #первый катет
            data = conn.recv(1024).decode() #чтение данных с определенным кол-м байт
            if data.isdigit(): #если данные числовые
                a = int(data) #перевод в тип данных integer
                conn.send(b"Enter B as a number\n") #сообщение появляется в терминале
            else:
                conn.send(b"Not a number\n" 
                        b"Enter A as a number\n") #сообщение появляется в терминале, если данные не числовые

        while not b: #второй катет
            data = conn.recv(1024).decode()
            if data.isdigit():
                b = int(data)
            else:
                conn.send(b"Not a number\n"
                        b"Enter B as a number\n")

        c = pifagor(a, b) #функция принимает два введенных числа и считает гипотенузу
        conn.send(str.encode(f"Ответ: {c}")) #отправка ответа

    conn.close() #закрытие сокета


#### Commands

* `py -3.8 server.py` - Запуск в первом терминале.
* `py -3.8 client.py` - Запуск во втором терминале.
* `>>server: Hello, client`
*  `>>I solve Pythagorean theorem` 
*  `>>Enter A as a number`  
*  `2` 
*  `>>Client: 2` 
*  `>>server: Enter B as a number`  
*  `3` 
*  `>>server: Ответ: 13` - Вывод во втором терминале.

### Задание №3
Реализовать серверную часть приложения. Клиент подключается к серверу. В ответ
клиент получает http-сообщение, содержащее html-страницу, которую сервер
подгружает из файла index.html.

#### client.py
Клиентское приложение, в котором создается сокет, производится подключение к серверу, посылаются ему данные, принимаются 
данные и закрывается соединение. Клиент получает на выходе http-сообщение с html-страницей.

    import socket

    with socket.socket() as sock:
        sock.connect((socket.gethostname(), 1234))
        sock.settimeout(5)
        sock.send(b"GET / HTTP/1.1\n")
        data = sock.recv(16384)
        udata = data.decode('utf-8')
        print(udata)
        
##### server.py
Сервер принимает соединение, принимает от клиента данные, возвращает их в виде строки в верхнем регистре и закрывает соединение. 

    import socket
    with socket.socket() as sock:
        sock.bind((socket.gethostname(), 1234))
        sock.listen(1)
        conn, addr = sock.accept()
        with conn:
            with open('C:/Users/work11pro1/.virtualenvs/ITMO_ICT_WebDevelopment_2022-2023/students/k33421/laboratory_works/Bobrova_Maria/laboratory_work_1/task_3/index.html') as f:
                msg = f.read()
            print(conn.recv(16348).decode('utf-8'))
            response = 'HTTP/1.0 200 OK\n\n' + msg
            conn.sendall(response.encode('utf-8'))

#### index.html
Из этого html файла сервер подгружает страницу, которую отправляет клиенту.

    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>CandyShop</title>
    </head>   

    <body>
        <center>
            <h1>CandyShop</h1>
        </center>
        <p>Hi there! Please, buy candies</p>
    </body>
    </html>
    
#### Commands

* `py -3.8 server.py` - Запуск в первом терминале.
* `>>GET / HTTP/1.1` - Вывод в первом терминале.
* `py -3.8 client.py` - Запуск во втором терминале.
* `>>HTTP/1.0 200 OK` - Вывод во втором терминале. 
* `>>`  - Вывод во втором терминале:
* `<!DOCTYPE html>`
*    `<html>`
*    `<head>`
*    `<meta charset="UTF-8">`
*    `<title>CandyShop</title>`
*    `</head>`  

*    `<body>`
*    `<center>`
*    `<h1>CandyShop</h1>`
*    `</center>`
*    `<p>Hi there! Please, buy candies</p>`
*    `</body>`
*    `</html>` 
      
###Задание №4
Реализовать многопользовательский чат с помощью протокола TCP. Для применения с TCP необходимо запускать клиентские 
подключения и прием и отправку сообщений всем юзерам на сервере в потоках. Не забудьте сохранять юзеров,
чтобы потом отправлять им сообщения.

#### client.py
Thread — это отдельный поток выполнения. Это означает, что в вашей программе могут работать две и более 
подпрограммы одновременно. Но разные потоки на самом деле не работают одновременно: это просто кажется.

Клиентское приложение, в котором создается сокет, производится подключение к серверу, посылаются ему данные, принимаются 
данные и закрывается соединение. В терминалах клиентов отображаются сообщения и юзеры, от кого сообщения приходят.

    import socket, threading

    # Создать клиентский объект
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    while True:
        name = input('Пожалуйста, введите личный ник, не более десяти символов, не менее одного символа: ')
        if 1 < len(name) < 10:
            break

    # Подключить клиента
    client.connect((socket.gethostname(), 1234))
    print('-' * 5 + 'подключился к серверу' + '-' * 5)
    print('-' * 5 + 'Enter, чтобы закрыть соединение с сервером' + '-' * 5)


    def outdatas():
        while True:

            # Введите информацию, которая будет отправлена на сервер
            outdata = input('')
            print()
            if outdata == 'enter':
                break
                # Отправить на сервер
            client.send(f'{name}:{outdata}'.encode('utf-8'))
            print('%s:%s' % (name, outdata))


    def indatas():
        while True:
            # Принимаем информацию с сервера
            indata = client.recv(1024)

            # Закодировать полученную информацию
            print(indata.decode('utf-8'))


    # Создать многопоточность
    # Установить получение информации, объект потока
    t1 = threading.Thread(target=indatas, name='input')

    # Создание выходной информации, объект потока
    t2 = threading.Thread(target=outdatas, name='out')

    # Начать многопоточность
    t1.start()
    t2.start()

    # Заблокировать поток, основной поток не может завершиться, пока не завершится выполнение дочернего потока.
    # t1.join()
    t2.join()

    # Закрыть соединение
    print('-' * 5 + 'сервер отключен' + '-' * 5)
    client.close()

#### server.py
Сервер принимает соединение, принимает от клиента данные, возвращает их в виде строки в верхнем регистре и закрывает соединение. 

    import socket, threading

    # Создаем объект сокета
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Укажите IP и порт сервера
    server.bind((socket.gethostname(), 1234))
    # Максимальное количество подключений
    server.listen(5)
    print('Enter Enter для выхода с сервера')
    # Создайте список клиентов
    clients = list()
    # Хранить клиентов, которые создали потоки
    end = list()
    # Блокировка ожидания подключения клиента, возврата объекта подключения и адреса косвенного объекта
    def accept():
        while True:
            client, addr = server.accept()
            clients.append(client)
            print("\ r" + '-' * 5 + f'сервер подключен через {addr}: текущее количество подключений: ----- {len (clients)}' + '-' * 5, end = '') #Взаимодействие с другими людьми
    def recv_data(client):
        while True:
            # Принимаем информацию от клиента
            try:
                indata = client.recv(1024)
            except Exception as e:
                clients.remove(client)
                end.remove(client)
                print("\ r" + '-' * 5 + f'Сервер отключен: текущее количество подключений: ----- {len (clients)}' + '-' * 5, end = '')
                break
            print(indata.decode('utf-8'))
            for clien in clients:
                # Перенаправить информацию от клиента и отправить ее другим клиентам
                if clien != client:
                    clien.send(indata)
    
    
    def outdatas():
        while True:
            # Введите информацию, которая будет предоставлена клиенту
            print('')
            outdata = input('')
            print()
            if outdata == 'enter':
                break
            print('Отправить всем:% s' % outdata)
                # Отправлять информацию каждому клиенту
        for client in clients:
            client.send(f"Сервер: {outdata}".encode('utf-8'))
    
    def indatas():
        while True:
            # Выполните цикл подключенных клиентов и создайте соответствующий поток
            for clien in clients:
                # Если поток уже существует, пропустить
                if clien in end:
                    continue
                index = threading.Thread(target=recv_data, args=(clien,))
                index.start()
                end.append(clien)
    
    # Создать многопоточность
    # Создать получающую информацию, объект потока
    t1 = threading.Thread(target=indatas, name='input')
    t1.start()
    
    # Создать отправляемое сообщение, объект потока
    
    t2 = threading.Thread(target=outdatas, name='out')
    t2.start()
    
    # Ожидание подключения клиента, объект потока
    
    t3 = threading.Thread(target=accept(), name='accept')
    t3.start()
    
    # Блокировать округ, пока подпоток не будет завершен, и основной поток не может закончиться
    # t1.join()
    t2.join()
    
    # Выключите все серверы
    for client in clients:
        client.close()
    print('-' * 5 + 'сервер отключен' + '-' * 5)
    

#### Commands

* `py -3.8 server.py` - Запуск в первом терминале.
* `Enter Enter для выхода с сервера` - Вывод в первом терминале.
* `py -3.8 client.py` - Запуск во втором терминале.
* `Пожалуйста, введите личный ник, не более десяти символов, не менее одного символа:` - Вывод во втором терминале.      
* `>>Maria` - Вводим во втором терминале.
* `-----подключился к серверу-----`
* `-----Enter, чтобы закрыть соединение с сервером-----` - Вывод во втором терминале
* `>>Hi!` - Вводим сообщение.
* `Maria:Hi!` - Вывод во втором терминале.
* `\ r-----сервер подключен через ('192.168.56.1', 49653): текущее количество подключений: ----- 1-----Maria:Hi!` - Вывод в первом терминале.
* `py -3.8 client.py` - Запуск в третьем терминале.
* `Пожалуйста, введите личный ник, не более десяти символов, не менее одного символа:` - Вывод во втором терминале.      
* `>>Sofia` - Вводим во втором терминале.
* `-----подключился к серверу-----`
* `-----Enter, чтобы закрыть соединение с сервером-----` - Вывод во втором терминале
* `>>Hello, Mary)` - Вводим сообщение.
* `Sofia:Hello, Mary)` - Вывод в третьем и втором терминалах.
* `\ r-----сервер подключен через ('192.168.56.1', 49766): текущее количество подключений: ----- 2-----Sofia:Hello, Mary)` - Вывод в первом терминале.

И так далее.

###Задание №5
Необходимо написать простой web-сервер для обработки GET и POST http
запросов средствами Python и библиотеки socket.

#### server.py
Сервер, который может принять и записать информацию о дисциплине 
и оценке по дисциплине и отдать информацию обо всех оценах по дсициплине в виде html-страницы.

    import socket
    
    class Response:
        def __init__(self, status, reason, headers=None, body=None):
            self.status = status
            self.reason = reason
            self.headers = headers
            self.body = body
    
    
    class MyHTTPServer:
        def __init__(self, host, port, name):
            self.host = host
            self.port = port
            self.name = name
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Создаем объект сокета
            self.points = {"Maths": ["4"]}
    
        def serve_forever(self):
            try:
                self.server.bind((self.host, self.port)) # Укажите IP и порт сервера
                self.server.listen() # Максимальное количество подключений
                while True:
                    client, address = self.server.accept() #Создает новый объект Socket для заново созданного подключения.
                    self.serve_client(client)
                    print(f"Сервер запущен на порту > {self.host}:{self.port}")
            except KeyboardInterrupt: #Исключение, возникающее когда пользователь нажимает определённые клавиши прерывания процесса
                self.server.close()
    
        def serve_client(self, client):
            try:
                data = client.recv(1024).decode()
                req = self.parse_request(data)
                res = self.handle_request(req)
                self.send_response(client, res)
                print(f'Клиент подключился')
            except Exception:
                print(f'Клиент неожиданно отключился')
            client.close()
    
        #Чтение и разбор (синтаксический анализе) HTTP-запроса
        def parse_request(self, data):
            #из соединения необходимо прочитать строку, т.е. последовательность байт, заканчивающуюся комбинацией \r\n
            req = data.rstrip('\r\n')
            text = req[:data.index("\n")].split()
            if len(text) != 3:
                raise Exception('Malformed request line')
    
            method, target, version = text
            if version != 'HTTP/1.1':
                raise Exception('Unexpected HTTP version')
    
            req = {'data': {}, 'method': method}
            if '?' in target:
                req['method'] = 'POST'
                data = target.split('?')[1].split('&')
                for value in data:
                    index, info = value.split('=')
                    req['data'][index] = info
    
            return req
    
        # Обработка запросов
        def handle_request(self, req):
            if req['method'] == 'POST':
                return self.handle_post(req)
            else:
                return self.handle_get()
    
        def handle_post(self, req):
            course = req["data"]["course"]
            points = req["data"]["points"]
            if course not in self.points:
                self.points[course] = []
            if int(points) < 1 or int(points) > 5:
                raise Exception(f"Неправильное значение оценки")
            self.points[course].append(points)
            return self.handle_get()
    
        def handle_get(self):
            type = "text/html; charset=utf-8"
            first_settings = "<html><head><style></style></head><body>"
            course = "<form><label>Subject: </label><input name='course' /><br><br>"
            points = "<label>Grade: </label><input name='points' /><br><br>"
            button = "<input type='submit'></form>"
            body = first_settings + course + points + button
            for course_name in self.points:
                body += f"<div><span>{course_name}: {self.points[course_name]}</span></div>"
            second_settings = "</body></html>"
            body += second_settings
            body = body.encode("utf-8")
            headers = [("Content-Type", type),
                       ("Content-Length", len(body))]
            return Response(200, "OK", headers, body)
    
        #Отправка ответа
        def send_response(self, client, res): #отправка ответа
            file = client.makefile('wb')
            status_line = f"HTTP/1.1 {res.status} {res.reason}\r\n"
            status_line = status_line.encode("utf-8")
            file.write(status_line)
            if res.headers:
                for (index, info) in res.headers:
                    header_line = f"{index}: {info}\r\n"
                    file.write(header_line.encode("utf-8"))
            file.write(b"\r\n")
            if res.body:
                file.write(res.body)
            file.flush()
            file.close()
    
        #В случае ошибки на любом из этапов, обработка заканчивается отправкой сообщения об ошибке
        def get_error(self, code, text):
            return Response(code, "OK", "Content-Type: text/html; charset=utf-8", text)
    
    
    if __name__ == "__main__":
        MyHTTPServer("localhost", 9095, "example.com").serve_forever()
        
#### Commands

* `py -3.8 server.py` - Запуск в первом терминале.
* 'localhost:9095' - Вписать в поисковик