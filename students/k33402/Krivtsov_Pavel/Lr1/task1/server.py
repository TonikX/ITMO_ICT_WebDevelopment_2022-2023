from ..server import Server


class FirstTaskServer(Server):
    def start(self):
        # create connection
        client_socket, address = self.accept_connection()
        client_socket.send(bytes("Hello, client", "utf-8"))

        client_data = self.get_str_data(client_socket)
        print(client_data)

        client_socket.close()
        self.socket.close()


if __name__ == '__main__':
    server = FirstTaskServer("UDP")
    server.start()
