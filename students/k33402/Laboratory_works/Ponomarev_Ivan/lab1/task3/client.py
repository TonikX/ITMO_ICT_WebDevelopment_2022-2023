import socket


host = "127.0.0.1"
port = 14900
serv_addr = (host, port)
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class client:
    def __init__(self,connection, serv_addr):
        self.connection = connection
        self.start_client(serv_addr)

    def start_client(self, serv_addr):
        self.connection.connect(serv_addr)
        self.get_response()

    def get_response(self):
        while True:
            recv_data = self.connection.recv(1024)
            if not recv_data:
                break
            print(recv_data.decode("utf-8"))

if __name__=="__main__":
    client = client(connection, serv_addr)