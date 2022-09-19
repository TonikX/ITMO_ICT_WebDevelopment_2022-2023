import socket


def get_decimal_input(decimalName):
    decimalNum = None
    while True:
        try:
            decimalNum = float(input(f"Enter value for {decimalName}: "))
        except ValueError:
            print("Not a number.")
            continue
        if decimalNum < 0:
            print(f"{decimalName} must be a positive number.")
            continue
        else:
            break
    return decimalNum


# TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect(('localhost', 12346))

    print("\nPythagorean theorem solver.")
    print("""
        +
        |\\
        | \\ C
      A |  \\
        |   \\
        +----+
           B
    """)
    message = ""
    option1 = ""
    while True:
        option1 = input("Choose to solve for (A, B or C): ").lower()
        if option1 not in ('a', 'b', 'c'):
            print("Not an appropriate choice.")
        else:
            message += option1 + "\n"
            break
    if (option1 == "a"):
        b = get_decimal_input("B")
        c = get_decimal_input("C")

        message += str(b) + "\n"
        message += str(c) + "\n"

    elif (option1 == "b"):
        a = get_decimal_input("A")
        c = get_decimal_input("C")

        message += str(a) + "\n"
        message += str(c) + "\n"
    else:
        a = get_decimal_input("A")
        b = get_decimal_input("B")

        message += str(a) + "\n"
        message += str(b) + "\n"

    sock.send(message.encode("utf-8"))
    connection = sock.recv(2048)
    data = connection.decode('utf-8')

    print(f'\nSolution for {option1.upper()} is:', data)
except ConnectionRefusedError:
    print("Could not connect to the server")


sock.close()
