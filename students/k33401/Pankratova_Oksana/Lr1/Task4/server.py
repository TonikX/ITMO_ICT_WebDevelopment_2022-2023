import socket
import threading


def connection(sockets):
    # заблокировать другие потоки
    while True:
        clsocket, addr = s.accept()
        sockets.append(clsocket)
        print('connected ', addr)


def get(sock, sockets):
    while True:
        try:
            msg = sock.recv(1024)
        except Exception as e:
            sockets.remove(sock)
            break
        for soc in sockets:
            if soc != sock:
                soc.send(msg)


def make_threads(sockets, threads):
    while True:
        for soc in sockets:
            if soc in threads:
                continue
            t = threading.Thread(target=get, args=(soc, sockets))
            t.start()
            threads.append(soc)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((socket.gethostname(), 2020))
s.listen(10)

sockets = []
threads = []

t1 = threading.Thread(target=connection, args=(sockets,))
t1.start()

t2 = threading.Thread(target=make_threads, args=(sockets, threads,))
t2.start()

t2.join()
