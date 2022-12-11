import socket
from loguru import logger

host: tuple[str, int] = ("localhost", 8765)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(host)

for _ in range(2):
    data = sock.recv(24000)
    text = data.decode()
    logger.info("Server response: %s", text)
    side = input()
    sock.send(side.encode())

data = sock.recv(24000)
c_side = data.decode()
logger.info('side is %s', c_side)
sock.close()
