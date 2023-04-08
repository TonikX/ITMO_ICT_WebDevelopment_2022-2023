import socket
import numpy as np
import pickle

sock = socket.socket()
sock.bind(('localhost', 9090))
sock.listen(1)
conn, addr = sock.accept()

while True:
    data = conn.recv(1024)
    #udata = data.decode("utf-8")
    data_variable = pickle.loads(data)
    if not data:
        break

    t_answer = str(float(data_variable['a'])*float(data_variable['b'])*np.sin(float(data_variable['gr'])))
    

    conn.send(t_answer.encode())
    
conn.close()