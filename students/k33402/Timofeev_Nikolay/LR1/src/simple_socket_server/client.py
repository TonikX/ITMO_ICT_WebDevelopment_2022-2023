import socket
from loguru import logger


host: tuple[str, int] = ("localhost", 8765)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(host)
logger.debug(f"Connecting to socket-server at {host}")
sock.send(b"Hello server\n")

data = sock.recv(24000)
logger.info(f"Server response: {data.decode('utf-8')}")
sock.close()
