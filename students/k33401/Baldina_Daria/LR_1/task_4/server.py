import threading, socket


def send_to_chat(sender, msg):
    for client in clients:
        if sender != client:
            client.sendall(msg)

def handle_client(cl_sock, cl_addr): #обработка клиента
    print(f'Client {cl_addr[0]}:{cl_addr[1]} join the chat')

    while True:
        try:
            message = cl_sock.recv(1024) #принимаем сообщение от клиента
            if message.decode('utf-8').find('bye') != -1: #клиент покидает 
                send_to_chat(cl_sock, message) 
                break
            elif message.decode('utf-8').find('Error') != -1:
                break
            send_to_chat(cl_sock, message)  #отправляем сообщение участникам чата
        except socket.error:
            print(f'Client {cl_addr[0]}:{cl_addr[1]} suddenly left')
            break

    print (f'Client {cl_addr[0]}:{cl_addr[1]} left the chat')
    clients.remove(cl_sock)
    cl_sock.close()

#запускаем сервер
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 9090
s.bind((host,port))
s.listen(100)
clients = []

print('Starting chat server')


while True:
        try:
            client_socket, client_address = s.accept()
            if client_address not in clients:
                clients.append(client_socket)
            t1 = threading.Thread(target = handle_client, args =(client_socket, client_address))
            t1.start()
        except KeyboardInterrupt:
            print('Server stopped')
            break
s.close()