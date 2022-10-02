import socket


SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', SERVER_PORT))
sock.listen(1)
print('Listening on port %s ...' % SERVER_PORT)

while True:    
    # Wait for client connections
    client_connection, client_address = sock.accept()

    # When enter localhost in browser, we as a client send a GET request.
    request = client_connection.recv(1024).decode()

    with open('index.html') as f:
        content = f.read()

    # Send HTTP response
    response = 'HTTP/1.0 200 OK\n\n'+ content
    client_connection.sendall(response.encode())
    client_connection.close()

#sock.close()