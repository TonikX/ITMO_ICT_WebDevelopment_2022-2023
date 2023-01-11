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

##Лабораторная работа №2 

О домашнем задании должна храниться следующая информация: предмет, преподаватель, дата выдачи, период выполнения, текст задания, информация о штрафах.
Необходимо реализовать следующий функционал:

*	Регистрация новых пользователей.

*	Просмотр домашних заданий по всем дисциплинам (сроки выполнения, описание задания).

*	Сдача домашних заданий в текстовом виде. 

*	Администратор (учитель) должен иметь возможность поставить оценку за задание средствами Django-admin. 

*	В клиентской части должна формироваться таблица, отображающая оценки всех учеников класса.


###Основные файлы
####models.py
    from django.db import models
        from django.contrib.auth.models import AbstractUser
    
    
    class User(AbstractUser):
        is_student = models.BooleanField(default=False)
        is_teacher = models.BooleanField(default=False)
        with_additional_info = models.BooleanField(default=False)
    
    
    CHARACTERS = [
        ('K', 'K')
    ]
    
    NUMBERS = [
        (1, '3241'),
        (2, '3242')
    ]
    
    SUBJECTS = [
        ("Математика", "Математика"),
        ("История", "История"),
        ("КИГ", "КИГ"),
        ("Программирование", "Программирование"),
        ("Информатика", "Информатика")
    ]
    
    
    class StudentGroup(models.Model):
        character = models.CharField(max_length=1, choices=CHARACTERS, default="K", verbose_name="Литера")
        number = models.IntegerField(choices=NUMBERS, default=1, verbose_name="Номер")
    
        def __str__(self):
            return f"{self.character}{self.number}"
    
    
    class Student(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
        student_group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE, null=True)
    
        def __str__(self):
            return f"{self.user.first_name} {self.user.last_name}"
    
    
    class Teacher(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
        subject = models.CharField(max_length=30, choices=SUBJECTS, verbose_name="Предмет")
    
        def __str__(self):
            return f"{self.user.first_name} {self.user.last_name}"
    
    
    class Homework(models.Model):
        student_group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE, null=True)
        teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
        subject = models.CharField(max_length=30, choices=SUBJECTS, verbose_name="Предмет")
        start_date = models.DateTimeField(verbose_name="Дата выдачи")
        end_date = models.DateTimeField(verbose_name="Сдать до")
        task_description = models.TextField(verbose_name="Описание")
        fine_info = models.CharField(max_length=150, verbose_name="Информация о штрафах")
        max_points = models.IntegerField(verbose_name="Максимальное количество баллов")
    
    
    class HomeworkAnswer(models.Model):
        homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
        student = models.ForeignKey(Student, on_delete=models.CASCADE)
        date = models.DateTimeField(auto_now=True, blank=True)
        answer = models.TextField(null=True, blank=True, verbose_name="Ответ")
    
    
    class TeacherAnswerOnHomework(models.Model):
        homework_answer = models.OneToOneField(HomeworkAnswer, on_delete=models.CASCADE, primary_key=True)
        points = models.IntegerField(default=0, verbose_name="Баллы")
        message = models.TextField(null=True, blank=True, verbose_name="Сообщение")
        teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
        date = models.DateTimeField(auto_now=True, blank=True)


#### forms.py

    from django.contrib.auth.forms import UserCreationForm
    from django import forms
    
    from .models import Teacher, Student, User, Homework, StudentGroup, HomeworkAnswer, TeacherAnswerOnHomework
    
    ROLES = [
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    ]
    
    groups = [(group.pk, group) for group in StudentGroup.objects.all()]
    
    
    class RegisterForm(UserCreationForm):
        role = forms.ChoiceField(
            required=True,
            choices=ROLES
        )
    
        class Meta:
            model = User
            fields = ("username", "first_name", "last_name", "password1", "password2")
    
        def save(self, commit=True):
            user = super(RegisterForm, self).save(commit=False)
            print("ROLE", self.cleaned_data["role"])
            if self.cleaned_data["role"] == "teacher":
                user.is_teacher = True
            if self.cleaned_data["role"] == "student":
                user.is_student = True
            if commit:
                user.save()
            return user
    
    
    class TeacherForm(forms.ModelForm):
        def __init__(self, *args, **kwargs):
            self.user = kwargs.pop('user', None)
            super(TeacherForm, self).__init__(*args, **kwargs)
    
        class Meta:
            model = Teacher
            fields = ["subject"]
    
        def save(self, commit=True):
            teacher = super(TeacherForm, self).save(commit=False)
            teacher.user = self.user
            teacher.user.with_additional_info = True
            if commit:
                teacher.user.save()
                teacher.save()
            return teacher
    
    
    class StudentForm(forms.Form):
        def __init__(self, *args, **kwargs):
            self.user = kwargs.pop('user', None)
            super(StudentForm, self).__init__(*args, **kwargs)
    
        student_group = forms.ChoiceField(required=True, choices=groups)
    
        def save(self, commit=True):
            student = Student()
            student.user = self.user
            student.user.with_additional_info = True
            student.student_group = StudentGroup.objects.get(pk=self.cleaned_data["student_group"])
            if commit:
                student.user.save()
                student.save()
            return student
    
    
    class TeacherAnswerOnHomeworkForm(forms.ModelForm):
        class Meta:
            model = TeacherAnswerOnHomework
            fields = ["points", "message"]
    
        def __init__(self, *args, **kwargs):
            self.homework_answer = kwargs.pop('homework_answer', None)
            self.user = kwargs.pop('user', None)
            super(TeacherAnswerOnHomeworkForm, self).__init__(*args, **kwargs)
    
        def save(self, commit=True):
            teacher_homework_answer = super(TeacherAnswerOnHomeworkForm, self).save(commit=False)
            teacher_homework_answer.homework_answer = self.homework_answer
            teacher_homework_answer.teacher = self.user.teacher
            if commit:
                teacher_homework_answer.save()
            return teacher_homework_answer
    
    
    class HomeworkAnswerForm(forms.ModelForm):
        def __init__(self, *args, **kwargs):
            self.homework = kwargs.pop('homework', None)
            self.student = kwargs.pop('student', None)
            super(HomeworkAnswerForm, self).__init__(*args, **kwargs)
    
        class Meta:
            model = HomeworkAnswer
            fields = ["answer"]
    
        answer = forms.CharField(label='message', max_length=180)
    
        def save(self, commit=True):
            homework_answer = super(HomeworkAnswerForm, self).save(commit=False)
            homework_answer.homework = self.homework
            homework_answer.student = self.student
            if commit:
                homework_answer.save()
            return homework_answer
    
    
    class HomeworkForm(forms.ModelForm):
    
        def __init__(self, *args, **kwargs):
            self.user = kwargs.pop('user', None)
            super(HomeworkForm, self).__init__(*args, **kwargs)
    
        class Meta:
            model = Homework
            fields = ["task_description", "start_date", "end_date", "max_points", "fine_info"]
            widgets = {
                "start_date": forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
                "end_date": forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'})
            }
    
        student_group = forms.ChoiceField(required=True, choices=groups)
    
        def save(self, commit=True):
            homework = super(HomeworkForm, self).save(commit=False)
            homework.student_group = StudentGroup.objects.get(pk=self.cleaned_data["student_group"])
            homework.teacher = Teacher.objects.get(user=self.user)
            homework.subject = homework.teacher.subject
            if commit:
                homework.save()
            return homework

####views.py
    from django.shortcuts import render
    
    # Create your views here.
    import django.db
    import django.db
    from django.http import HttpResponse
    from django.shortcuts import render, redirect
    from django.contrib.auth.decorators import login_required
    from .decorators import student_required, teacher_required, additional_info_check
    from django.contrib.auth import authenticate, login, logout
    
    from .forms import RegisterForm, TeacherForm, StudentForm, HomeworkAnswerForm, HomeworkForm, \
        TeacherAnswerOnHomeworkForm
    from .models import Homework, Teacher, Student, HomeworkAnswer, TeacherAnswerOnHomework
    
    
    def registerPage(requset):
        form = RegisterForm
    
        if requset.method == "POST":
            form = RegisterForm(requset.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
    
        context = {'form': form}
        return render(requset, 'pages/register.html', context)
    
    
    def loginPage(request):
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
    
            user = authenticate(request, username=username, password=password)
    
            if user is not None:
                login(request, user)
                return redirect('home')
    
        context = {}
    
        return render(request, 'pages/login.html', context)
    
    
    @login_required(login_url='login')
    def add_info(request):
        if request.user.is_teacher:
            if request.method == "POST":
                form = TeacherForm(request.POST, user=request.user)
                if form.is_valid():
                    form.save()
                    return redirect('home')
            else:
                form = TeacherForm(user=request.user)
                context = {"form": form}
                return render(request, "pages/add_info.html", context)
    
        if request.user.is_student:
            if request.method == "POST":
                form = StudentForm(request.POST, user=request.user)
                if form.is_valid():
                    form.save()
                    return redirect('home')
            else:
                form = StudentForm(user=request.user)
                context = {"form": form}
                return render(request, "pages/add_info.html", context)
        return HttpResponse("You are not teacher or student")
    
    
    @login_required(login_url='login')
    @additional_info_check()
    def home(request):
        if request.user.is_teacher:
            return redirect("teacher_home")
        if request.user.is_student:
            return redirect("student_home")
        return HttpResponse("You are not teacher or student")
    
    
    def get_checked_and_unchecked_homeworks(homeworks):
        checked_homeworks = []
        unchecked_homeworks = []
        for homework in homeworks:
            try:
                t = homework.teacheransweronhomework
                if t:
                    checked_homeworks.append(homework)
            except TeacherAnswerOnHomework.DoesNotExist:
                unchecked_homeworks.append(homework)
        return {"checked_homeworks": checked_homeworks, "unchecked_homeworks": unchecked_homeworks}
    
    
    @login_required(login_url='login')
    @teacher_required()
    def teacher_marks_page(request):
        homeworks = Homework.objects.filter(teacher=request.user.teacher)
        homework_answers = []
        for homework in homeworks:
            try:
                homework_answers.append(HomeworkAnswer.objects.get(homework=homework))
            except HomeworkAnswer.DoesNotExist:
                continue
    
        filtered_homeworks = get_checked_and_unchecked_homeworks(homework_answers)
        context = {"homework_answers": homework_answers, "checked_homeworks": filtered_homeworks["checked_homeworks"],
                   "unchecked_homeworks": filtered_homeworks["unchecked_homeworks"]}
        return render(request, 'pages/marks.html', context)
    
    
    @login_required(login_url='login')
    @student_required()
    def student_marks_page(request):
        student = Student.objects.get(user=request.user)
        homeworks = Homework.objects.filter(student_group=student.student_group)
        homework_answers = []
        for homework in homeworks:
            try:
                homework_answers.append(HomeworkAnswer.objects.get(homework=homework))
            except HomeworkAnswer.DoesNotExist:
                continue
    
        filtered_homeworks = get_checked_and_unchecked_homeworks(homework_answers)
        context = {"homework_answers": homework_answers, "checked_homeworks": filtered_homeworks["checked_homeworks"],
                   "unchecked_homeworks": filtered_homeworks["unchecked_homeworks"]}
        return render(request, 'pages/marks.html', context)
    
    
    @login_required(login_url='login')
    @teacher_required()
    def delete_homework(request, work_id):
        homework = Homework.objects.get(pk=work_id)
        homework.delete()
        return redirect("home")
    
    
    @login_required(login_url='login')
    @teacher_required()
    def change_homework(request, work_id):
        homework = Homework.objects.get_or_create(pk=work_id)[0]
        if request.method == "POST":
            form = HomeworkForm(request.POST, instance=homework, user=request.user)
            if form.is_valid():
                form.save()
                return redirect("home")
        form = HomeworkForm(instance=homework, user=request.user)
        context = {"word_id": work_id, "form": form, "homework": homework}
        return render(request, 'pages/create_homework.html', context)
    
    
    @login_required(login_url='login')
    @teacher_required()
    def create_homework(request):
        if request.method == "POST":
            form = HomeworkForm(request.POST, user=request.user)
            if form.is_valid():
                form.save()
                return redirect("home")
        form = HomeworkForm(user=request.user)
        context = {"form": form}
        return render(request, 'pages/create_homework.html', context)
    
    
    @login_required(login_url='login')
    @teacher_required()
    def teacher_home_page(request):
        teacher = Teacher.objects.get(user=request.user)
        homeworks = Homework.objects.filter(teacher=teacher)
        context = {"homeworks": homeworks}
        return render(request, "pages/home.html", context)
    
    
    @login_required(login_url='login')
    @student_required()
    def student_home_page(request):
        student = Student.objects.get(user=request.user)
        completed_words = HomeworkAnswer.objects.all()
        completed_words = [work.homework for work in completed_words]
        homeworks = Homework.objects.filter(student_group=student.student_group)
        homeworks = [homework for homework in homeworks if homework not in completed_words]
        context = {"homeworks": homeworks}
        return render(request, "pages/home.html", context)
    
    
    @login_required(login_url='login')
    @login_required()
    def marks(request):
        if request.user.is_teacher:
            return redirect('teacher_marks')
        if request.user.is_student:
            return redirect('student_marks')
    
    
    @login_required(login_url='login')
    @teacher_required()
    def rate_homework(request, work_id):
        try:
            homework_answer = HomeworkAnswer.objects.get(pk=work_id)
        except HomeworkAnswer.DoesNotExist:
            return HttpResponse("Homework answer does not exist")
    
        try:
            if request.method == "POST":
                form = TeacherAnswerOnHomeworkForm(request.POST, instance=homework_answer.teacheransweronhomework,
                                                   homework_answer=homework_answer, user=request.user)
                if form.is_valid():
                    form.save()
                    return redirect("marks")
            form = TeacherAnswerOnHomeworkForm(instance=homework_answer.teacheransweronhomework,
                                               homework_answer=homework_answer, user=request.user)
            context = {"form": form, "homework_answer": homework_answer}
            return render(request, 'pages/rate_homework.html', context)
        except TeacherAnswerOnHomework.DoesNotExist:
            if request.method == "POST":
                form = TeacherAnswerOnHomeworkForm(request.POST, homework_answer=homework_answer, user=request.user)
                if form.is_valid():
                    form.save()
                    return redirect("marks")
            form = TeacherAnswerOnHomeworkForm(homework_answer=homework_answer, user=request.user)
            context = {"form": form, "homework_answer": homework_answer}
            return render(request, 'pages/rate_homework.html', context)
    
    
    @login_required(login_url='login')
    @student_required()
    def make_homework(request, work_id):
        student = Student.objects.get(user=request.user)
    
        try:
            homework = Homework.objects.get(pk=work_id)
        except Homework.DoesNotExist:
            return HttpResponse("Homework answer does not exist")
    
        if request.method == "POST":
            form = HomeworkAnswerForm(request.POST, homework=homework, student=student)
            if form.is_valid():
                form.save()
                return redirect("marks")
        form = HomeworkAnswerForm(homework=homework, student=student)
        context = {"form": form, "homework": homework}
        return render(request, 'pages/make_homework.html', context)
    
    
    @login_required(login_url='login')
    def logoutUser(request):
        logout(request)
        return redirect('login')
        
####urls.py
    from django.contrib import admin
    from django.urls import path
    import table.views
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('register/', table.views.registerPage, name="register"),
        path('login/', table.views.loginPage, name="login"),
        path("", table.views.home, name="home"),
        path("add_info/", table.views.add_info, name="add_info"),
        path("logout/", table.views.logoutUser, name="logout"),
        path("marks/", table.views.marks, name="marks"),
        path("teacher_marks/", table.views.teacher_marks_page, name="teacher_marks"),
        path("student_marks/", table.views.student_marks_page, name="student_marks"),
        path("make_homework/<int:work_id>/", table.views.make_homework, name="make_homework"),
        path("change_homework/<int:work_id>/", table.views.change_homework, name="change_homework"),
        path("create_homework/", table.views.create_homework, name="create_homework"),
        path("teacher_home/", table.views.teacher_home_page, name="teacher_home"),
        path("student_home/", table.views.student_home_page, name="student_home"),
        path("delete_homework/<int:work_id>/", table.views.delete_homework, name="delete_homework"),
        path("rate_homework/<int:work_id>/", table.views.rate_homework, name="rate_homework")
    ]

##Практическая работа 3.1

###Задание 3.1.1
Описание: напишите запрос на создание 6-7 новых автовладельцев и 5-6 автомобилей, каждому автовладельцу назначьте удостоверение и от 1 до 3 автомобилей. Задание можете выполнить либо в интерактивном режиме интерпретатора, либо в отдельном python-файле. Результатом должны стать запросы и отображение созданных объектов.
####models.py
    from django.db import models
    from django.contrib.auth.models import AbstractUser
    # Create your models here.
    
    
    class Car_owner(models.Model):
        id_owner = models.IntegerField(primary_key = True)
        last_name = models.CharField(max_length = 30, null = False)
        first_name = models.CharField(max_length = 30, null = False)
        birth_day = models.DateField(null = True)
        passport = models.IntegerField(null=True)
        address = models.CharField(max_length=50, null=True, blank=True)
        nationality = models.CharField(max_length=20, null=True, blank=True)
    
    class Car(models.Model):
        id_car = models.IntegerField(primary_key = True)
        state_number = models.CharField(max_length = 15, null = False)
        mark_car = models.CharField(max_length = 20, null = False)
        model_car = models.CharField(max_length = 20, null = False)
        color =  models.CharField(max_length = 30, null = True)
    
    class Ownerdhip(models.Model):
        id_owner_car = models.IntegerField(primary_key = True)
        id_owner = models.ForeignKey(Car_owner, on_delete = models.CASCADE)
        id_car = models.ForeignKey(Car, on_delete = models.CASCADE)
        start_date = models.DateField()
        end_date = models.DateField(null = True)
    
    class Driver_license(models.Model):
        id_license =  models.IntegerField(primary_key = True)
        id_owner = models.ForeignKey(Car_owner, on_delete = models.CASCADE)
        license_number = models.CharField(max_length = 10, null = False)
        type = models.CharField(max_length = 10, null = False)
        date_of_license= models.DateField()

####Создание автовладельцев:
    Car_owner(1, 'LN1', 'FN1', '1990-01-1').save()
    Car_owner(2, 'LN2', 'FN2', '1991-01-1').save()
    Car_owner(3, 'LN3', 'FN3', '1992-01-1').save()
    Car_owner(4, 'LN4', 'FN4', '1993-01-1').save()
    Car_owner(5, 'LN5', 'FN5', '1994-01-1').save()
    Car_owner(6, 'LN6', 'FN6', '1995-01-1').save()

    for i in Car_owner.objects.all():
        ...:     print(i)
        ...: 
    Car_owner object (1)
    Car_owner object (2)
    Car_owner object (3)
    Car_owner object (4)
    Car_owner object (5)
    Car_owner object (6)

    for i in Car_owner.objects.all():
    ...:     print(i.id_owner)
    ...: 
    1
    2
    3
    4
    5
    6

####Создание автомобилей
    Car(1, 'A1A1', 'BMW', 'Model1', 'white').save()
    Car(2, 'A2A2', 'BMW', 'Model2', 'black').save()
    Car(3, 'A3A3', 'Toyota', 'Model3', 'blue').save()
    Car(4, 'A4A4', 'Toyota', 'Model4', 'white').save()
    Car(5, 'A5A5', 'Audi', 'Model5', 'red').save()
    Car(6, 'A6A6', 'Audi', 'Model6', 'balck').save()

####Создание водительских прав
    Driver_license(1, 1, '1234567', 'B', '2010-01-01').save()
    Driver_license(2, 2, '4567890', 'B', '2011-01-01').save()
    Driver_license(3, 3, '6527810', 'B', '2012-01-01').save()
    Driver_license(4, 4, '65228340', 'B', '2013-01-01').save()
    Driver_license(5, 5, '15228143', 'B', '2014-01-01').save()
    Driver_license(6, 6, '13298123', 'B', '2015-01-01').save()

####Владение автомобилей
    Ownerdhip(1, 1, 1, '2011-01-01', '2012-01-01').save()
    Ownerdhip(2, 2, 2, '2012-01-01', '2013-01-01').save()
    Ownerdhip(3, 3, 3, '2013-01-01', '2014-01-01').save()
    Ownerdhip(4, 4, 4, '2014-01-01', '2015-01-01').save()
    Ownerdhip(5, 5, 5, '2015-01-01', '2016-01-01').save()
    Ownerdhip(6, 6, 6, '2016-01-01', '2017-01-01').save()



###Задание 3.1.2
Описание: по созданным в пр.1 данным написать следующие запросы на фильтрацию:

####Запрос 1
Выведете все машины марки “Toyota” (или любой другой марки, которая у вас есть):
   
    In [45]: Car.objects.filter(mark_car="Toyota")
    
    Out[45]: <QuerySet [<Car: Car object (3)>, <Car: Car object (4)>]>

####Запрос 2
Найти всех водителей с именем “Олег” (или любым другим именем на ваше усмотрение):

    In [46]: Car_owner.objects.filter(first_name="FN3")
    Out[46]: <QuerySet [<Car_owner: Car_owner object (3)>]>

####Запрос 3
Взяв любого случайного владельца получить его id, и по этому id получить экземпляр удостоверения в виде объекта модели (можно в 2 запроса):

    In [48]: take_id = Car_owner.objects.all()[1].id_owner
    In [49]: Driver_license.objects.get(id_owner=take_id)
    Out[49]: <Driver_license: Driver_license object (2)>

####Запрос 4
Вывести всех владельцев красных машин (или любого другого цвета, который у вас присутствует):
 
    In [2]: Car_owner.objects.filter(ownership__id_car__color = 'red')
    Out[2]: <QuerySet [<Car_owner: Car_owner object (5)>]>


####Запрос 5
Найти всех владельцев, чей год владения машиной начинается с 2010 (или любой другой год, который присутствует у вас в базе):

    In [3]: Car_owner.objects.filter(ownership__start_date__gte="2013-01-01")
    Out[3]: <QuerySet [<Car_owner: Car_owner object (3)>, <Car_owner: Car_owner object (4)>, <Car_owner: Car_owner object (5)>, <Car_owner: Car_owner object (6)>]>



###Задание 3.1.3
Описание: необходимо реализовать следующие запросы:

####Запрос 1
Вывод даты выдачи самого старшего водительского удостоверения:

    In [59]: from django.db.models import Min, Max
    
    In [60]: Driver_license.objects.aggregate(date_of_license=Min("date_of_license"))
    Out[60]: {'date_of_license': datetime.date(2010, 1, 1)}

####Запрос 2
Укажите самую позднюю дату владения машиной, имеющую какую-то из существующих моделей в вашей базе:
 
    In [62]: Ownerdhip.objects.aggregate(start_date=Max("start_date"))
    Out[62]: {'start_date': datetime.date(2016, 1, 1)}

####Запрос 3
Выведите количество машин для каждого водителя:

    In [64]: from django.db.models import Count
    
    In [65]: Ownerdhip.objects.values("id_owner").annotate(Count("id_car"))
    Out[65]: <QuerySet [{'id_owner': 1, 'id_car__count': 1}, {'id_owner': 2, 'id_car__count': 1}, {'id_owner': 3, 'id_car__count': 1}, {'id_owner': 4, 'id_car__count': 1}, {'id_owner': 5, 'id
    _car__count': 1}, {'id_owner': 6, 'id_car__count': 1}]>

####Запрос 4
Подсчитайте количество машин каждой марки:

    In [66]: Car.objects.values("mark_car").annotate(Count("id_car"))
    Out[66]: <QuerySet [{'mark_car': 'Audi', 'id_car__count': 2}, {'mark_car': 'BMW', 'id_car__count': 2}, {'mark_car': 'Toyota', 'id_car__count': 2}]>

####Запрос 5
Отсортируйте всех автовладельцев по дате выдачи удостоверения:

    In [79]: Car_owner.objects.order_by("driver_license__date_of_license")
    Out[79]: <QuerySet [<Car_owner: Car_owner object (1)>, <Car_owner: Car_owner object (2)>, <Car_owner: Car_owner object (3)>, <Car_owner: Car_owner object (4)>, <Car_owner: Car_owner objec
    t (5)>, <Car_owner: Car_owner object (6)>]>

##Лабораторная работа №3
###models.py
    from django.db import models
    from django.contrib.auth.models import AbstractUser
    
    class Organizer(AbstractUser):
        tel = models.CharField(verbose_name='Телефон', max_length=15, null=True, blank=True)
    
        REQUIRED_FIELDS = ['first_name', 'last_name', 'tel']
    
        def __str__(self):
            return self.username
    
    class Participant(models.Model):
        name = models.CharField(max_length=100)
        breed_types = (
            ('h', 'haski'),
            ('t', 'terrier'),
            ('b', 'bulldog'),
        )
        breed = models.CharField(max_length=1, choices=breed_types)
        age = models.IntegerField()
        family = models.CharField(max_length=1000)
        owner_data = models.CharField(max_length=1000)
        club = models.ForeignKey('Club', on_delete=models.CASCADE,
                                 null=True, blank=True
                                 )
    
        def __str__(self):
            return self.name
    
    
    class Show(models.Model):
        year = models.IntegerField(primary_key=True)
        show_types = (
            ('mono', 'mono-breed'),
            ('poly', 'poly-breed')
        )
        type = models.CharField(max_length=4, choices=show_types)
        participants = models.ManyToManyField('Participant',
                                              # through='Participation',
                                              related_name='show_participants'
                                             )
    
        def __str__(self):
            return str(self.year)
    
    
    class Participation(models.Model):
        participant = models.ForeignKey('Participant', on_delete=models.CASCADE)
        medal_types = (
            ('g', 'gold'),
            ('s', 'silver'),
            ('b', 'bronze'),
        )
        medal = models.CharField(max_length=1, choices=medal_types, null=True)
        rings = models.ManyToManyField('Ring', null=True, blank=True)
        vaccinated = models.DateField()
        dismissed = models.BooleanField()
        final_grade = models.IntegerField(blank=True, null=True)
    
        def __str__(self):
            return f'{self.participant}'
    
    
    class Expert(models.Model):
        name = models.CharField(max_length=50)
        last_name = models.CharField(max_length=50)
        club = models.CharField(max_length=100)
    
        def __str__(self):
            return f'{self.name} {self.last_name}'
    
    
    class Club(models.Model):
        name = models.CharField(max_length=100)
        members = models.ManyToManyField('Participant',
                                         related_name='club_members'
                                         )
    
        def __str__(self):
            return self.name
    
    
    class Ring(models.Model):
        show = models.ForeignKey('Show', on_delete=models.CASCADE)
        experts = models.ManyToManyField('Expert',
                                         # through='Grade'
                                         related_name='ring_experts',
                                         null=True,
                                         blank=True
                                         )
        breed_types = (
            ('h', 'haski'),
            ('t', 'terrier'),
            ('b', 'bulldog'),
        )
        breed = models.CharField(max_length=1, choices=breed_types)
    
        def __str__(self):
            return f'{self.show} {self.breed}'

###serializers.py
    from rest_framework import serializers
    from .models import *
    
    '''Организатору выставки могут потребоваться следующие сведения;
     На каком ринге выступает заданный хозяин со своей собакой? !
     Какими породами представлен заданный клуб? !
     Сколько собак были отстранены от участия в выставке? !
     Какие эксперты обслуживают породу? !
     Количество участников по каждой породе?'''
    
    
    
    class ExpertSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Expert
            fields = "__all__"
    
    class ParticipationSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Participation
            fields = "__all__"
    
    class ParticipantSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Participant
            fields = "__all__"
    
    
    class RingParticipationSerializer(serializers.ModelSerializer):
        '''На каком ринге выступает заданный хозяин со своей собакой?'''
    
        class Meta:
            model = Participation
            fields = ["rings"]
    
    
    class ParticipantBreedsSerializer(serializers.ModelSerializer):
        '''Количество участников по каждой породе?'''
        class Meta:
            model = Participant
            fields = ["breed"]
    
    
    class ClubBreedsSerializer(serializers.ModelSerializer):
        '''Какими породами представлен заданный клуб?'''
        members = ParticipantBreedsSerializer(many=True)
    
        class Meta:
            model = Club
            fields = ["name", "members"]
    
    
    class RingSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Ring
            fields = "__all__"
    
    
    class DismissedCountSerializer(serializers.ModelSerializer):
        '''Сколько собак были отстранены от участия в выставке?'''
        dismissed_count = serializers.SerializerMethodField()
    
        class Meta:
            model = Participation
            fields = ['dismissed_count']
    
        def get_dismissed_count(self, obj):
            return Participation.objects.filter(dismissed=True).count()
    
    
    class BreedExpertsSerializer(serializers.ModelSerializer):
        '''Какие эксперты обслуживают породу?'''
        experts = ExpertSerializer(many=True)
    
        class Meta:
            model = Ring
            fields = ["breed", "experts"]

###view.py
    from rest_framework import generics
    from rest_framework.views import APIView, Response
    from .serializers import *
    from .models import *
    from django.db.models.aggregates import Count, Sum
    
    
    class ExpertAPIView(generics.RetrieveUpdateDestroyAPIView):
        serializer_class = ExpertSerializer
        queryset = Expert.objects.all()
    
    class ParticipationAPIList(generics.ListCreateAPIView):
        serializer_class = ParticipationSerializer
        queryset = Participation.objects.all()
    
    class ParticipantAPIList(generics.ListCreateAPIView):
        serializer_class = ParticipantSerializer
        queryset = Participant.objects.all()
    
    
    class RingParticipationAPIView(generics.RetrieveAPIView):
        serializer_class = RingParticipationSerializer
        queryset = Participation.objects.all()
    
    
    class ClubBreedsRetrieveAPIView(generics.RetrieveAPIView):
        serializer_class = ClubBreedsSerializer
        queryset = Club.objects.all()
    
    
    class DismissedCountAPIView(generics.RetrieveAPIView):
        serializer_class = DismissedCountSerializer
        queryset = Participation.objects.all()
    
    # leave name
    class BreedExpertsAPIView(generics.ListAPIView):
        serializer_class = BreedExpertsSerializer
        queryset = Ring.objects.all()
    
    
    class BreedCountAPIView(APIView):
    
        def get(self, request):
            # breed_count = Participant.objects.filter(breed=breed).count()
            breed_count = Participant.objects \
                .values('breed').annotate(count=Count('breed'))
            content = {'breed_count': breed_count}
            return Response(content)
    
    
    class BreedCountAPIView(APIView):
    
        def get(self, request):
            breed_count = Ring.objects \
                .values('breed').annotate(count=Count('breed'))
            content = {'breed_count': breed_count}
            return Response(content)
    
    
    class ReportAPIView(APIView):
    
        def get(self, request, year):
            participants = Show.objects.get(year=year).participants
            participant_count = participants.count()
            breed_count = participants.values('breed').annotate(count=Count('breed'))
            best_grades = Participation.objects.filter(rings__show__year=year)\
                .values('participant')\
                .annotate(ex_sum=Sum('final_grade'))\
                .order_by()
            medals = Participation.objects.values('rings__breed')\
                .annotate(medals_count=Count('medal'))
            content = {'participant_count': participant_count,
                       'breeds': breed_count,
                       'best_grades': best_grades,
                       'medals': medals}
            return Response(content)
    
    

###urls.py
    from django.urls import path
    from .views import *
    
    
    app_name = "dogsapp"
    
    
    urlpatterns = [
        path('experts/<int:pk>', ExpertAPIView.as_view()),
        path('participation/', ParticipationAPIList.as_view()),
        path('participants/', ParticipantAPIList.as_view()),
    
        path('participant_ring/<int:pk>', RingParticipationAPIView.as_view()),
        path('club_breeds/<int:pk>', ClubBreedsRetrieveAPIView.as_view()),
        path('dismissed_count/<int:pk>', DismissedCountAPIView.as_view()),
        path('breed_experts/', BreedExpertsAPIView.as_view()),
        path('breeds_count/', BreedCountAPIView.as_view()),
        path('report/<int:year>', ReportAPIView.as_view()),
    ]

###Основной endpoint
