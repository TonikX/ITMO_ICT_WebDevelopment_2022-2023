import socket
from loguru import logger

host: tuple[str, int] = ("localhost", 8765)

sock: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.bind(host)
    sock.listen(10)
    client_socket, address = sock.accept()
    logger.debug(f"Accepted connection:\n{address}")
    data: bytes = client_socket.recv(24000)
    logger.info(f"User data: {data.decode('utf-8')}")
    client_socket.send(b"Hello client\n")
except Exception as e:
    logger.warning(e)
finally:
    logger.debug("Server stopped")
    sock.close()
