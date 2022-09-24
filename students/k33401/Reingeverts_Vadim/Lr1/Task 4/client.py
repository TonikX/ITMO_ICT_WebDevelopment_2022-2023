import socket
from threading import Thread


class SocketClient(socket.socket):
    name = ""

    def __init__(self):
        # TCP
        socket.socket.__init__(self, socket.AF_INET, socket.SOCK_STREAM)
        # Ensures that port is always ready to be used again
        self.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Makes keyboard interrupt possible at all times
        self.settimeout(0.1)

        self.name = input("Create a nickname: ") or "Anonymous"

    def client_connect(self, host='localhost', port=12344):
        try:
            self.connect((host, port))
        except IOError:
            print("Could not connect to the server.")
            self.stop()
            return
        self.talk_with_server()

    def talk_with_server(self):
        while True:
            try:
                text = input("Your message: ")
                message = f"{self.name}: {text}".encode("utf-8")
                self.send(message)

                try:
                    connection = self.recv(2048)
                    message = connection.decode('utf-8')
                    print(message)
                # Handle timeout
                except IOError:
                    continue
            except ConnectionResetError or ConnectionAbortedError:
                print("Server closed connection.")
            except ConnectionRefusedError:
                print("Could not connect to the server.")
            except KeyboardInterrupt:
                break
        self.stop()

    def stop(self):
        print("\nDisconnecting...")
        self.close()


if __name__ == "__main__":
    client = SocketClient()
    client.client_connect()
