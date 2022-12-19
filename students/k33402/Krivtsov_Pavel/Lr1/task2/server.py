from Lr1.server import Server
import typing as tp


class SecondTaskServer(Server):
    def start(self):
        client_socket, address = self.accept_connection()

        while not self.area:
            while len(self.vectors) < 2:
                if len(self.vectors) == 0:
                    self.send_data_to_client(client_socket, "First vector")
                else:
                    self.send_data_to_client(client_socket, "Second vector")

                data = self.get_data_from_client(client_socket)
                self._set_vector_from_data(data)

            self._set_area()
            client_socket.send(str(self.area).encode())

        client_socket.close()
        self.socket.close()

    def _set_vector_from_data(self, data: str):
        coords = tuple(map(float, data.split()))
        self.vectors.append(coords)

    def _set_area(self):
        x = self.vectors[0][1] * self.vectors[1][2] - self.vectors[0][2] * self.vectors[1][1]
        y = self.vectors[0][0] * self.vectors[1][2] - self.vectors[0][2] * self.vectors[1][0]
        z = self.vectors[0][0] * self.vectors[1][1] - self.vectors[0][1] * self.vectors[1][0]

        self.area = (x**2 + y**2 + z**2)**0.5
        print(self.area)

    def __init__(self, protocol_type: str):
        super().__init__(protocol_type)
        self.vectors: tp.List[tp.Tuple[float, ...]] = []
        self.area = 0.0


if __name__ == '__main__':
    server = SecondTaskServer("TCP")
    server.start()
