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
        self._alias = f"Anonymous_{uuid.uuid1().hex[:5]}"
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.connect((ip, port))

    def _receive(self):
        while True:
            try:
                message = self._sock.recv(1024).decode()
                logger.info(message)
            except Exception as e:
                logger.info("Disconnected from server")
                break
        self._sock.close()

    def _send(self):
        while True:
            message = input()
            if message == '/quit':
                break
            self._sock.send(message.encode())
        self._sock.close()

    def start(self):
        try:
            self._sock.send(self._alias.encode())

            receive_thread = threading.Thread(target=self._receive)
            receive_thread.start()

            send_thread = threading.Thread(target=self._send)
            send_thread.start()
        except Exception:
            logger.warning("Something went wrong")


if __name__ == "__main__":
    ChatClient("127.0.0.1", 9095).start()
