import socket

from loguru import logger

host: tuple[str, int] = ("localhost", 8765)


def pythagoras_theorem(a: int, b: int) -> float:
    return round((a**2 + b**2) ** (1 / 2))


sock: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.bind(host)
    sock.listen(10)
    client_socket, address = sock.accept()
    logger.debug(f"Connection from {address}")

    client_socket.send(b"Calculate C side of triangle using Pythagoras theorem. Enter a side:")
    data = client_socket.recv(24000)
    a_side = int(data.decode())

    client_socket.send(b"Enter b side:")
    data = client_socket.recv(24000)
    b_side = int(data.decode())
    client_socket.send(f"C side is: ~{pythagoras_theorem(a=a_side, b=b_side)}".encode())
except Exception as e:
    logger.warning(e)
finally:
    logger.debug("Server stopped")
    sock.close()
