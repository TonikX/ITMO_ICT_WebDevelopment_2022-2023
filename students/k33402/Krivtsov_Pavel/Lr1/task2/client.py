from Lr1.client import Client


class SecondTaskClient(Client):
    def start(self):
        first_vector = input("Enter first vector's coordinates x, y, z: ")
        second_vector = input("Enter second vector's coordinates x, y, z: ")

        while True:
            data = self.get_data_from_server()
            if data == "First vector":
                self.send_data_to_server(first_vector)
            elif data == "Second vector":
                self.send_data_to_server(second_vector)
            else:
                print(data)
                break

        self.socket.close()


if __name__ == '__main__':
    client = SecondTaskClient("TCP")
    client.start()
