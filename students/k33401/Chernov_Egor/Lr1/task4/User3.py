import socket
import threading
import time


def out_data():
    time.sleep(2)
    m = 'Hi, i\'m 3\n'
    s.send(m.encode('utf-8'))
    print(f'You ({s.getsockname()[1]}): {m}')
    time.sleep(5)
    m = 'Lol\n'
    s.send(m.encode('utf-8'))
    print(f'You ({s.getsockname()[1]}): {m}')
    time.sleep(4)
    m = 'I\'m cool!!!\n'
    s.send(m.encode('utf-8'))
    print(f'You ({s.getsockname()[1]}): {m}')
    time.sleep(5)
    s.send(b'/exit')


if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        host = '127.0.0.1'
        port = 8080
        s.connect((host, port))
        t = threading.Thread(target=out_data, name='out', daemon=True)
        i = 1
        while 1:
            try:
                in_data = s.recv(1024)
                decodeData = in_data.decode("utf-8")
                if not in_data:
                    print('You left the chat')
                    break
                print(decodeData)
                if i:
                    print('You have joined the chat')
                    t.start()
                    i -= 1
            except socket.error:
                print('Server was terminated')
                break
