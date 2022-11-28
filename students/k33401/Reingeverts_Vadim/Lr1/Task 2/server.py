import socket
from math import sqrt


def calc_pythagorean_equation(solveFor, x, y):
    solution = None
    x = float(x)
    y = float(y)
    if solveFor == "a":
        solution = sqrt(y**2 - x**2)
    elif solveFor == "b":
        solution = sqrt(y**2 - x**2)
    else:
        solution = sqrt(x**2 + y**2)
    return solution


# TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Ensures that port is always ready to be used again
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('localhost', 12346))


# Makes keyboard interrupt possible at all times
sock.settimeout(1.0)
sock.listen(10)

print(
    f"Started server at tcp://{sock.getsockname()[0]}:{sock.getsockname()[1]}")

while True:
    try:
        connection, client_address = None, None
        try:
            connection, client_address = sock.accept()
        # Handle timeout
        except IOError:
            continue

        data = connection.recv(2048)
        data = data.decode('utf-8')
        print('Recived:\n' + data)

        solveFor, x, y, _ = data.split("\n")
        solution = calc_pythagorean_equation(solveFor, x, y)

        print("Sending response:", solution)
        connection.send(str(solution).encode('utf-8'))

    except KeyboardInterrupt:
        print("Stopping server...")
        if connection:
            connection.close()
        break
sock.close()
