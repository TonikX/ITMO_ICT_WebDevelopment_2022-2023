import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('127.0.0.1', 1337))
server.listen(100)

clients = list()
end = list()

def accept():
 
    while True:
        conn, addr = server.accept()
        clients.append(conn)
        print (f'Current connections: {len(clients)}')
 
 
def recv_data(conn):
    while True:
        try:
            indata = conn.recv(1024)
        except Exception as e:
            clients.remove(conn)
            end.remove(conn)
            break
        print(indata.decode('utf-8'))
        for cl in clients:
            if cl != conn:
                cl.send(indata)
 
 
def outdatas():
    while True:
        print('')
        outdata = input('')
        print()
        if outdata=='/LEAVE':
            break
        for conn in clients:
            conn.send (f"Server: {outdata}". encode ('utf-8)'))
 
 
def indatas():
    while True:
            for cl in clients:
                if cl in end:
                    continue
                index = threading.Thread(target = recv_data,args = (cl,))
                index.start()
                end.append(cl)
 

t1 = threading.Thread(target = indatas,name = 'input')
t1.start()
 
t2 = threading.Thread(target = outdatas, name= 'out')
t2.start()
 
t3 = threading.Thread(target = accept(),name = 'accept')
t3.start()

t2.join()

for conn in clients:
    conn.close()