import socket
import webbrowser


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 8888
server.bind((host, port))
server.listen(1)

while True:
    conn, addr = server.accept()

    webbrowser.open("index.html")

    conn.close()
