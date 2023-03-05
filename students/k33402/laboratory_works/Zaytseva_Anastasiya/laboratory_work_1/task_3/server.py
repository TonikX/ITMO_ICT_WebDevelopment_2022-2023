import socket
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime

LOCAL_PORT = 25030
MAX_CLIENTS = 10
BUFFER_SIZE = 1024

SERVER_NAME = 'chiclasserver/1.0.0'

sock = socket.socket()
sock.bind(('', LOCAL_PORT))
sock.listen(MAX_CLIENTS)

with open('index.html', 'r') as file:  # чтение файла
    file_data = file.read()

now = datetime.now()  # вычисляем время в нужном формате для подстановки в поле даты
stamp = mktime(now.timetuple())
date = format_date_time(stamp)

dt = datetime.strptime('24/09/22 15:08', '%d/%m/%y %H:%M')  # вычисляем время в нужном формате для подстановки в поле
# последней модификации файла
stamp = mktime(dt.timetuple())
last_modified = format_date_time(stamp)

content_length = len(file_data.encode('utf-8'))  # вычисляем размер файла

data = f'''HTTP/1.1 200 OK
Server: {SERVER_NAME}
Date: {date}
Content-Type: text/html
Content-Length: {content_length}
Last-Modified: {last_modified}
Connection: keep-alive
Access-Control-Allow-Origin: *
Accept-Ranges: bytes

'''

data += file_data

while True:
    conn, addr = sock.accept()
    conn.send(data.encode('utf-8'))
    print('index.html был отправлен')
    conn.close()
