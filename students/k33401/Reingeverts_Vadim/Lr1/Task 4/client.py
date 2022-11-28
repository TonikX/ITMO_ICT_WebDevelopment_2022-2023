import os
import socket
from threading import Thread
import json


def destructure(dict):
    return (t[1] for t in dict.items())


class ChatClient(socket.socket):
    name = ""
    id = ""
    is_connected = False

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
            self.id = f"{self.getsockname()[0]}:{self.getsockname()[1]}"
            self.is_connected = True

        except IOError:
            print("Could not connect to the server.")
            self.client_disconnect()

        self.talk_with_server()

    def talk_with_server(self):

        thread1 = Thread(target=self.client_send)
        thread2 = Thread(target=self.client_receive)

        thread1.start()
        thread2.start()

    def client_send(self):
        while True:
            try:
                text = input("")
                print()

                msg_dict = {"name": self.name, "text": text}

                # Serialize dict
                serialized = json.dumps(msg_dict).encode("utf-8")
                self.send(serialized)

            except TimeoutError:
                continue
            except (EOFError, IOError, OSError):
                break
            except KeyboardInterrupt:
                break
        self.client_disconnect()

    def client_receive(self):
        while True:
            try:
                data = self.recv(2048)
                # Deserialize dict
                msg_dict = json.loads(data)
                name, text, id = destructure(msg_dict)
                local_name = "You" if id == self.id else name

                print(f"{local_name}: {text}")

            except TimeoutError:
                continue
            except (ConnectionResetError, ConnectionAbortedError):
                print("\nServer closed connection.")
                break
            except OSError:
                break
            except KeyboardInterrupt:
                break
        self.client_disconnect()

    def client_disconnect(self):
        if (self.is_connected):
            self.close()
        self.is_connected = False
        os._exit(0)


if __name__ == "__main__":
    client = ChatClient()
    client.client_connect()
