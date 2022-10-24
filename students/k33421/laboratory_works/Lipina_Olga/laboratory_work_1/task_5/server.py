import socket
import sys
from typing import Dict, Tuple, List


class MyHTTPServer:
    def __init__(self, host, port):
        """ Initializing HTTP server. Creating
        database for saving records of grades.
        :param host: Host address.
        :param port: Free port for server.
        """
        self.host = host
        self.port = port
        self.database: List[Tuple[str, str]] = []
        # tcp connection
        self._conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def run_server(self):
        """Activates HTTP server."""
        self._conn.bind((self.host, self.port))
        # listen to 1 client.
        self._conn.listen(1)
        while True:
            client, address = self._conn.accept()
            print(f"Connected at {address}")
            self.client_dialogue(client)

    def client_dialogue(self, client: socket.socket):
        """Handling client request and sending response. """
        data = client.recv(4096).decode()
        if data is None:
            return None
        response = self.handle_request(data)
        client.send(response.encode())

    @staticmethod
    def parse_request(data: str) -> Tuple[str, str]:
        """Get request info."""
        data = data.replace("\r", "")
        try:
            # get request from first line
            req = data[:data.index("\n")]
        except ValueError:
            # when we don't send anything
            return data, ""

        if "\n\n" in data:
            body = data[data.index("\n") + 1:].split("\n\n")[1]
        else:
            body = ""
        return req, body

    @staticmethod
    def parse_body(body: str) -> Dict[str, str]:
        """
        Parse body args.
        :param body: body of request
        :return: Dict of args.
        """
        body_dict: Dict[str,str] = {}
        for elem in body.split('&'):
            head_name = elem[:elem.index('=')]
            value = elem[elem.index('=') + 1:].replace('+', ' ')
            body_dict[head_name] = value
        return body_dict

    def handle_request(self, data: str) -> str:
        """Handling user's request and send a page.
        """
        req, body = self.parse_request(data)
        method, url, smt = req.split()
        response = f"{smt} 200 OK\n\n"

        if method == 'GET' and url == '/index':
            with open('index.html') as f:
                response += f.read()

        elif method == 'GET' and url == '/table':
            with open('grading.html') as f:
                lines = f.readlines()
            table = [f"<tr><td>{s}</td><td>{g}</td></tr>" for s, g in self.database]
            response += '\n'.join(lines[:8]) + '\n'.join(table) + '\n'.join(lines[8:])

        elif method == 'POST' and url == '/send':
            parsed_body = self.parse_body(body)
            self.database.append((parsed_body['subject'], parsed_body['grade']))
            return response

        else:
            return f"{smt} 400\n\nBad request\n\n"

        return response



if __name__ == '__main__':
    host = "localhost"
    port = 8005
    serv = MyHTTPServer(host, port)
    serv.run_server()