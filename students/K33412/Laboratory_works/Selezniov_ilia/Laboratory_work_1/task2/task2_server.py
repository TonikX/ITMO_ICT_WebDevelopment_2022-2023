import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):

    def calculate_area(self, base: float, altitude: float) -> float:
        """Метод для расчёта площадь параллелограмма
        по заданной стороне и высоте, проведённой к ней"""
        area: float = base * altitude
        return area

    def handle(self):
        self.data = self.request.recv(1024).strip()
        print(f"Received data: {self.data.decode()}")
        try:
            base, altitude = self.data.decode().split()
            base = float(base)
            altitude = float(altitude)
            resp = bytes(str(self.calculate_area(
                base, altitude)) + "\n", "utf-8")
        except ValueError:
            resp = bytes(
                "Необходимо ввести сторону и высоту параллелограмма через пробел",
                "utf-8")
        self.request.sendall(resp)


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
