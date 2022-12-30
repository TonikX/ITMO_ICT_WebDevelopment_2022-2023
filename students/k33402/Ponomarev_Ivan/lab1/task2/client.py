import socket
import enum

host = "127.0.0.1"
port = 14900
serv_addr = (host, port)
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class input_l(enum.Enum):

    hypotenuse = 1
    quadratic = 2
    trapezoid_area = 3
    parallelogram_area = 4
    exit = 5

class line_interface:
    def __init__(self, client):
        self.is_ex = True
        self.client = client
        self.msg = ""

    def start_li(self):
        while self.is_ex:
            self.msg=""
            print("Выберите операцию(введите цифру):\n" +
                "\n1)Теорема Пифагора" +
                "\n2)Решение квадратного уравнения" +
                "\n3)Поиск площади трапеции" + 
                "\n4)Поиск площади параллелограмма" + 
                "\n5)exit-завершение программы\n")
            act = int(input())
            if input_l.hypotenuse.value == act: self.hypotenuse()
            elif input_l.quadratic.value == act: self.quadratic()
            elif input_l.trapezoid_area.value == act: self.trapezoid_area()
            elif input_l.parallelogram_area.value == act: self.parallelogram_area()
            elif input_l.exit.value == act:
                 self.close_li
                 break
            else: 
                print("Вы ввели неправильное число(Пример: [1] - Теорема пифагорa")
                continue
            recv_msg = self.client.send_request(self.msg)
            self.print_response(recv_msg)

    
    def quadratic(self):
        self.msg+=input_l.quadratic.name + "\n"
        print("Введите a")
        x = input()
        print("Введите b")
        b = input()
        print("Введите c")
        c = input()
        self.msg+=x + "&" + b + "&" + c


    def hypotenuse(self):
        self.msg += input_l.hypotenuse.name + "\n"
        print("Введите a")
        a = input()
        print("Введите b")
        b = input()
        self.msg+=a +"&" + b

    def trapezoid_area(self):
        self.msg += input_l.trapezoid_area.name + "\n"
        print("Введите a")
        a = input()
        print("Введите b")
        b = input()
        print("Введите h")
        h = input()
        self.msg+=a+"&"+b+"&"+h

    def parallelogram_area(self):
        self.msg+= input_l.parallelogram_area.name + "\n" 
        print("Введите a")
        a = input()
        print("Введите h")
        h=input()
        self.msg+=a+"&"+h

    def print_response(self, msg_recv):
        print(msg_recv)

    def close_li(self):
        self.client.close_conneciton()
        self.is_ex = False
        print("Bye!")



class client:
    def __init__(self, serv_addr, connection):
        self.serv_addr = serv_addr
        self.connection = connection
        self.start_client()

    def start_client(self):
        self.connection.connect(self.serv_addr)

    def send_request(self, msg):
        msg_b = bytes(msg, "utf-8")
        connection.send(msg_b)
        return self.rec_response()

    def rec_response(self):
        recv_msg = self.connection.recv(16384)
        recv_msg_dec = recv_msg.decode("utf-8")
        return recv_msg_dec
    
    def close_connection(self):
        self.connection.close()

if __name__ == "__main__":
    client = client(serv_addr, connection)
    line_i = line_interface(client)
    line_i.start_li()

