import socket
import logging
import enum
import math

host = "127.0.0.1"
port = 14900
addr = (host, port)
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
logging.basicConfig(filename = './log.log', filemode= 'w', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)

class operation(enum.Enum):
    hypotenuse = "hypotenuse"
    quadratic = "quadratic"
    trapezoid_area = "trapezoid_area"
    parallelogram_area = "parallelogram_area"

class calculation_service:
    
    def calculate(self, op, params):
        result = ""
        if op==operation.hypotenuse.value: result = self.hypotenuse(params[0],params[1])
        elif op==operation.quadratic.value: result = self.quadratic(params[0],params[1],params[2])
        elif op==operation.trapezoid_area.value: result = self.trapezoid_area(params[0], params[1], params[2])
        elif op==operation.parallelogram_area.value: result = self.parallelogram_area(params[0], params[1])
        return result

    def hypotenuse(self, a, b):
        c = (float(a)**2 + float(b)**2)**(0.5)
        return "Гипотенуза равна {}".format(c)

    def quadratic(self, a, b, c):
        a = float(a)
        b = float(b)
        c = float(c)
        discr = b ** 2 - 4 * a * c
        if discr > 0:
            x1 = (-b + math.sqrt(discr)) / (2 * a)
            x2 = (-b - math.sqrt(discr)) / (2 * a)
            return "x1 = {} \nx2 = {}".format(x1, x2)
        elif discr == 0:
            x = -b / (2 * a)
            return "x = {}".format(x)
        else:
            return "Корней нет"

    def trapezoid_area(self, a, b, h):
        area = ((float(a)+float(b))/2)*float(h)
        return "Площадь трапеции равна {}".format(area)

    def parallelogram_area(self, a, h):
        area = float(a) * float(h)
        return "Площадь параллелограмма равна {}".format(area)
            

class request_handler:
    def __init__(self, calculation_service):
        self.calculation_service = calculation_service

    def handle_request(self, msg_dec):
        msg_dec = msg_dec.split("\n")
        op = msg_dec[0]
        print(op)
        params = msg_dec[1].split("&")
        if self.validate(op, params):
            result = self.calculation_service.calculate(op,params)
            return result
        else:
            return "Params error"

    def validate(self, op, params):
        is_correct = False
        for oper in operation:
            if(op==oper.value): is_correct = True
        for param in params:
            try:
                int(param)
            except ValueError as ve:
                return False  
        return is_correct  

class server:
    def __init__(self, connection, req_handler, addr):
        self.connection = connection
        self.request_handler = req_handler
        self.addr = addr
        self.start_server()

    def start_server(self):
        self.connection.bind(addr)
        self.connection.listen(10)
        logging.info("Server started")
        client_socket, client_addr = self.connection.accept()
        self.get_request(client_socket, client_addr)

    def send_response(self, resp_msg, client_socket):
        client_socket.send(resp_msg)
        logging.info("Send response to %s" % (addr[0]))

    def get_request(self, client_sock, addr):
        while True:
            try:
                msg = client_sock.recv(16384)
                logging.info("Data received from %s port %d" % (addr[0], addr[1]))
                msg_dec = msg.decode("utf-8")
                response = self.request_handler.handle_request(msg_dec)
                response_encoded = response.encode("utf-8")
                self.send_response(response_encoded, client_sock)
            except:
                client_sock.close()
                break

if __name__ == "__main__":
    request_handler = request_handler(calculation_service())
    server = server(connection, request_handler, addr)
