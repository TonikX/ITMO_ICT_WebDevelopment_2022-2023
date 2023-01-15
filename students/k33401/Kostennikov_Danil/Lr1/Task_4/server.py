import socket
import threading
HOST = '127.0.0.1'
PORT = 14900

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

clients = []

def brodcast(message):
    print(message)
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            brodcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            break

def receive():
    while True:
        client, address = s.accept()
        print("Connected with {}".format(str(address)))
        clients.append(client)
        
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()


'''while True:
    cliensocket, address = s.accept()
    message = cliensocket.recv(1024)
    print(f"message: {message}, address: {address}")
    print(f" client_socket: {cliensocket}")
    if address not in users:
        users.append(address)
    for user in users:
        if user != address:
            address.send()
            s.sendto(message, user)

'''
