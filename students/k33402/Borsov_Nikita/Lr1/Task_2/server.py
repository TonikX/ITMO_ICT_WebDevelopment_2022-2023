from socket import *
import pickle

host = 'localhost'
port = 777
addr = (host, port)

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.bind(addr)
tcp_socket.listen()

print('Server was started!')

while True:
    conn, addr = tcp_socket.accept()
    data = conn.recv(1024)
    data = pickle.loads(data)
    problem_answer = (data[0] + data[1]) * data[2] / 2

    print(f'client {addr} succesfully connected to our socket and send data \n```\n{data}\n```')
    conn.sendall(pickle.dumps(problem_answer))

# udp_socket.close() As part of my expirience if you use Ctrl+C for exit, socket connection will be automatically
# destroyed, I check with `sudo lsof -i:777`
