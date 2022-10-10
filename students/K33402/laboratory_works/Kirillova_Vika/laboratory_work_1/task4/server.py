import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('127.0.0.1', 3300))
server.listen(100)

clients = list()
end = list()

def accept():
 
    while True:
        client, addr = server.accept()
        clients.append(client)
        print (f'Текущее количество подключений: {client}')
 
 
def recv_data(client):
    while True:
        try:
            indata = client.recv(1024)
        except Exception as e:
            clients.remove(client)
            end.remove(client)
            break
        print(indata.decode('utf-8'))
        for clien in clients:
            if clien != client:
                clien.send(indata)
 
 
def outdatas():
    while True:
        print('')
        outdata = input('')
        print()
        if outdata=='enter':
            break
        for client in clients:
            client.send (f"Сервер: {outdata}". encode ('utf-8)'))
 
 
def indatas():
    while True:
            for clien in clients:
                if clien in end:
                    continue
                index = threading.Thread(target = recv_data,args = (clien,))
                index.start()
                end.append(clien)
 

t1 = threading.Thread(target = indatas,name = 'input')
t1.start()
 
t2 = threading.Thread(target = outdatas, name= 'out')
t2.start()
 
t3 = threading.Thread(target = accept(),name = 'accept')
t3.start()

t2.join()

for client in clients:
    client.close()