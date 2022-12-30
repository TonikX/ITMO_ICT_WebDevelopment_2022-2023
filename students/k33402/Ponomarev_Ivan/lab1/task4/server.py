import socket
import logging
import threading

host = "127.0.0.1"
port = 14901
addr = (host, port)
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class server:
    def __init__(self, connection, serv_addr):
        self.connection = connection
        self.serv_addr = serv_addr
        self.clients = dict()
        self.start_server()
    
    def start_server(self):
        self.connection.bind(self.serv_addr)
        self.connection.listen(10)
        while True:
            client, client_addr = self.connection.accept()
            name=client.recv(16384)
            self.clients[client]=name.decode("utf-8")
            thread = threading.Thread(target=self.handle_message, args = (client,))
            thread.start()
            
    def handle_message(self,client):
        while True:
            message = client.recv(16384)
            message_e = message.decode('utf-8')
            if message_e == 'bye':
                self.clients.pop(client)
                client.close()
                break
            self.send_message(message_e, self.clients[client])

    def send_message(self,message,user_message):
        for client in self.clients.keys():
                client.send(("%s: %s"%(user_message,message)).encode("utf-8"))




if __name__ == "__main__":
    server = server(connection, addr)