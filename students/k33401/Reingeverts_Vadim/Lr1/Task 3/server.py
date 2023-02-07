import socket
from os import path
from pathlib import Path
import webbrowser

# Makes consistent path to work directory in case of
# 1. Running .py file directly `python server.py`
# 2. Running .py file from another directory `python ./someComplicatedPath/server.py`
# 3. Running cell from .ipynb notebook
ipynb_path = "./Task 3"
if "__file__" in globals():
    dirname = path.dirname(__file__)
else:
    dirname = Path(path.abspath("") + ipynb_path)

index_file = Path(dirname) / 'index.html'

# TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Ensures that port is always ready to be used again
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('localhost', 0))

# Makes keyboard interrupt possible at all times
sock.settimeout(1.0)
sock.listen(10)

url = f'http://{sock.getsockname()[0]}:{sock.getsockname()[1]}'
print(
    f"Started server at {url}")
webbrowser.open(url)

while True:
    try:
        try:
            connection, client_address = sock.accept()
        # Handle timeout
        except IOError:
            continue

        print("Incoming connection from:", client_address)

        response_type = "HTTP/1.1 200 OK\n"
        headers = "Content-Type: text/html; charset=utf-8\n\n"

        with open(index_file, 'r', encoding="utf-8") as file:
            body = file.read()

        response = response_type + headers + body
        connection.sendall(response.encode('utf-8'))

    except KeyboardInterrupt:
        print("Stopping server...")
        if connection:
            connection.close()
        break
sock.close()
