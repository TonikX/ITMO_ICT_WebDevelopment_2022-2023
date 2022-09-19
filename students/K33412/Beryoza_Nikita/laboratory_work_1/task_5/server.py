import socket

LOCALHOST = "127.0.0.1"
PORT = 3000
OK_STATUS = "HTTP/1.1 200 OK\n"
BAD_STATUS = "HTTP/1.1 500 BAD\n"
CLOSING_SOCKET = "Socket Closed\n"
database = []


def run_server():
    serv_sock = create_serv_sock()
    while True:
        client_sock = accept_client_conn(serv_sock)
        serve_client(client_sock)


def create_serv_sock():
    serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serv_sock.bind((LOCALHOST, PORT))
    serv_sock.listen(10)
    print(f"Сервер запущен на порту > {LOCALHOST}:{PORT}")
    return serv_sock


def accept_client_conn(serv_sock):
    client_sock, client_addr = serv_sock.accept()
    print(f'Клиент подключился с порта > {client_addr[0]}:{client_addr[1]}')
    return client_sock


def serve_client(client):
    data = client.recv(4096).decode()
    if data is None:
        print(f'Клиент неожиданно отключился')
        return
    response = handle_request(data)
    client.send(response.encode())


def parse_request(data):
    try:
        req = data[:data.index("\r\n")]
    except ValueError:
        req = data
        return req, "", ""
    if "\r\n\r\n" in data:
        headers, body = data[data.index("\r\n") + 1:].split("\r\n\r\n")
    else:
        headers, body = data[data.index("\r\n") + 1:], ""
    return req, headers, body


def parse_body(body):
    body_dict = {}
    for elem in body.split('&'):
        name = elem[:elem.index('=')]
        value = elem[elem.index('=') + 1:].replace('+', ' ')
        body_dict[name] = value
    return body_dict


def handle_request(data):
    req, headers, body = parse_request(data)
    headers += "\nAccess-Control-Allow-Origin: *"
    method, url, ver = req.split()
    response = f"{ver} 200 OK\r\n"
    error_response = f"{ver} 400\r\n\r\nBad request"
    if method == 'GET' and url == '/index':
        with open('index.html') as f:
            response += f.read()
    elif method == 'GET' and url == '/table':
        with open('table.html') as f:
            lines = f.readlines()
        table = [f"<tr><td>{s}</td><td>{g}</td></tr>" for s, g in database]
        # response += headers + '\r\n'.join(lines[:8]) + '\r\n'.join(table) + '\r\n'.join(lines[8:])
        response += headers + '\r\n\r\n' + '\r\n'.join(table)
        print("Response\n", response)
    elif method == 'POST' and url == '/send':
        parsed_body = parse_body(body)
        database.append((parsed_body['subject'], parsed_body['grade']))
        return response
    else:
        return error_response
    return response


if __name__ == '__main__':
    run_server()
