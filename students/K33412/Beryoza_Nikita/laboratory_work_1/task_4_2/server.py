import socket
import threading

HOST = '127.0.0.1'
PORT = 50000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen()

clients = []
client_names =[]


def broadcast_message(message):
    for client in clients:
        client.send(message)


def message_manager(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast_message(message.decode('ascii'))
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            client_name = client_names[index]
            print(f"Client {client_name} Disconnected!".encode('ascii'))
            client_names.remove(client_name)
            break


def connection():
    while True:
        client, address = server.accept()
        print(f"{address} Connected[+]")
        client.send("UserName".encode('ascii'))
        client_name = client.recv(1024).decode('ascii')

        client_names.append(client_name)
        clients.append(client)

        print(f"{client_name} Connected[+]")
        message = f"{client_name} Connected[+]".encode('ascii')
        broadcast_message(message)

        client.send("You are connected to server".encode('ascii'))

        thread = threading.Thread(target=message_manager, args=(client,))
        thread.start()


print("Server[127.0.0.1] localhost is running.... ")
connection()
