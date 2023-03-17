import socket
import codecs

host = "127.0.0.1"
port = 14900
addr = (host, port)
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class reader:
    def __init__(self, path):
        self.path = path
    def read_html(self):
        file = codecs.open(self.path, "r", "utf_8_sig" )
        text = file.read()
        file.close()
        return text

class server:
    def __init__(self, connection, serv_addr, reader):
        self.connection = connection
        self.reader = reader
        self.serv_addr = serv_addr
        self.start_server()
  
    def start_server(self):
        self.connection.bind(self.serv_addr)
        self.connection.listen(10)
        clientsocket, client_addr = self.connection.accept()
        self.send_resp(clientsocket)
    
    def send_resp(self, client_socket):
        response = self.build_resp()
        client_socket.send(response)
        print('{} senderd' %(response))
        client_socket.close()

    def build_resp(self):
        type = 'HTTP/1.0 200 OK\r\n'
        headers = 'Content-Type: text/html\r\n\r\n'
        body = self.reader.read_html()
        response = type + headers + body
        response_enc = response.encode("utf-8")
        return response_enc




if __name__=="__main__":
    reader = reader('index.html')
    server = server(connection, addr, reader)        