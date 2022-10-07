from Lr1.client import Client


class FirstTaskClient(Client):
    def start(self):
        self.send_data_to_server("Hello, server!")

        server_data = self.get_data_from_server()
        print(server_data)

        self.socket.close()


if __name__ == '__main__':
    client = FirstTaskClient("UDP")
    client.start()
