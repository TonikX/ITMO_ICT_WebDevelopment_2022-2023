import socket

def pifagor(a: int, b: int) -> float:
    return round((a**2 + b**2) ** (1 / 2))

def square_equation(a: int, b: int, c: int) -> list[float]:
    d = b**2 - 4*a*c
    if (d < 0):
        return []
    if (d == 0):
        x = -b / (2*a)
        return [x]
    x1 = (-b - d**(1/2)) / (2*a)
    x2 = (-b + d**(1/2)) / (2*a)
    return [x1, x2]

def s_trapezoid(a: int, b: int, h: int) -> float:
    return 1/2*a*b*h

def s_parallelogram(a: int, h: int) -> int:
    return a*h

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 4462))
sock.listen(1)
conn, addr = sock.accept()

conn.send("Выбери один из вариантов:'\n'1 - теорема Пифагора '\n'2 - решить квадратное уравнение '\n'3 - вычислить площадь трапеции '\n'4 - вычислить площади параллелограмма".encode())

while True:
    data = conn.recv(24000)
    if not data:
        break
    v = int(data.decode())
    match v:
        case 1:
            conn.send("Введите a и b".encode())
            data = conn.recv(24000)
            a, b = map(int, data.decode().split())
            ans = pifagor(a, b)
            conn.send(f'Ответ: {ans}'.encode())
        case 2:
            conn.send("Введите параметры уравнения".encode())
            data = conn.recv(24000)
            a, b, c = map(int, data.decode().split())
            roots = square_equation(a, b, c)
            if roots:
                conn.send(f'Количество корней: {len(roots)}; Ответ: {roots}'.encode())
            else:
                conn.send('Рациональных корней нет'.encode())
        case 3:
            conn.send("Введите основания и высоту".encode())
            data = conn.recv(24000)
            a, b, h = map(int, data.decode().split())
            ans = s_trapezoid(a, b, h)
            conn.send(f'Ответ: {ans}'.encode())
        case 4:
            conn.send("Введите основание и высоту".encode())
            data = conn.recv(24000)
            a, h = map(int, data.decode().split())
            ans = s_parallelogram(a, h)
            conn.send(f'Ответ: {ans}'.encode())
        case _:
            conn.send("Таких вычислений нет'\n'".encode())

conn.close()