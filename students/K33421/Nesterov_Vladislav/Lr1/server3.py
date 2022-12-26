#!/usr/bin/python
# -*- coding: utf-8 -*-

# import socket
#
# s = socket.socket()  # Create a socket object
# host = 'localhost'  # Get local machine name
# port = 1337
# s.bind((host, port))  # Bind to the port
#
# print('Starting server on', host, port)
# print('The Web server URL for this would be http://%s:%d/' % (host, port))
# s.listen(5)  # Now wait for client connection.
#
# print('Entering infinite loop; hit CTRL-C to exit')
# while True:
#     conn, addr = s.accept()
#     s.send('Server Online\n'.encode())
#     s.send('HTTP/1.0 200 OK\n'.encode())
#     s.send('Content-Type: text/html\n'.encode())
#     s.send("""
#         <html>
#         <body>
#         <p>
#         Hello, world!
#         </p>
#         </body>
#         </html>
#     """.encode())  # Use triple-quote string.

import socket

HOST, PORT = '127.0.0.1', 1337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(1)

print('Serving on port ', PORT)
print('Entering infinite loop; hit CTRL+C to exit')

while True:
    connection, address = s.accept()
    request = connection.recv(1024).decode('utf-8')
    string_list = request.split(' ')

    method = string_list[0]
    requesting_file = string_list[1]

    print('Client request ', requesting_file)

    myfile = requesting_file.split('?')[0]  # After the "?" symbol not relevent here
    myfile = myfile.lstrip('/')
    if myfile == '':
        myfile = 'index.html'  # Load index file as default

    try:
        file = open(myfile, 'rb')  # open file , r => read , b => byte format
        response = file.read()
        file.close()

        header = 'HTTP/1.1 200 OK\n'

        if myfile.endswith(".jpg"):
            mimetype = 'image/jpg'
        elif myfile.endswith(".css"):
            mimetype = 'text/css'
        else:
            mimetype = 'text/html'

        header += 'Content-Type: ' + str(mimetype) + '\n\n'

    except Exception as e:
        header = 'HTTP/1.1 404 Not Found\n\n'
        response = '<html><body><center><h3>Error 404: File not found</h3><p>Python HTTP Server</p></center></body></html>'.encode(
            'utf-8')

    final_response = header.encode('utf-8')
    final_response += response
    connection.send(final_response)
    connection.close()
