from Lr1.server import Server


class FirstTaskServer(Server):
    def start(self):
        # create connection
        client_socket, address = self.accept_connection()
        self.send_data_to_client(client_socket, "Hello, client")

        client_data = self.get_data_from_client(client_socket)
        print(client_data)

        client_socket.close()
        self.socket.close()


if __name__ == '__main__':
    server = FirstTaskServer("UDP")
    server.start()
