import socket
import sys
import threading
import uuid

from loguru import logger

logger_format = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
    "<level>{level}</level> | "
    "<level>{message}</level>"
)
logger.remove()
logger.add(sys.stdout, format=logger_format)


class ChatClient:
    def __init__(self, ip: str, port: int):
        self.alias = f"Anonymous_{uuid.uuid1().hex[:5]}"
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ip, port))

    def receive(self):
        while True:
            try:
                message = self.sock.recv(1024).decode()
                logger.info(message)
            except Exception as e:
                logger.info("Disconnected from server")
                break
        self.sock.close()

    def send(self):
        while True:
            message = input()
            if message == '/quit':
                break
            self.sock.send(message.encode())
        self.sock.close()

    def start(self):
        try:
            self.sock.send(self.alias.encode())

            receive_thread = threading.Thread(target=self.receive)
            receive_thread.start()

            send_thread = threading.Thread(target=self.send)
            send_thread.start()
        except Exception:
            logger.warning("Something went wrong")


if __name__ == "__main__":
    ChatClient("127.0.0.1", 9095).start()
