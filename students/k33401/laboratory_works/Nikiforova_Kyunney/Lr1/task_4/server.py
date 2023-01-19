import socket
import threading

sock = socket.socket()
sock.bind(('localhost', 9090))
sock.listen(10)

print('[ Server Started ]')

clients = []


def send_messages(msg, author):
    for client in clients:
        if author != client:
            client.send(msg)


def accept_messages(client):
    while True:
        msg = client.recv(1024)
        send_messages(msg, client)


while True:
    try:
        client_socket, address = sock.accept()
        clients.append(client_socket)
        thread = threading.Thread(target=accept_messages, args=(client_socket,))
        thread.start()
    except KeyboardInterrupt:
        print('[ Server stopped ]')
        break
sock.close()