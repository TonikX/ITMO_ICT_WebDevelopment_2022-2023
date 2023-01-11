import socket


host = "127.0.0.1"
port = 14900
serv_addr = (host, port)
msg = bytes("Hello, server!\n", "utf-8")

def start_client():
    connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    connection.connect(serv_addr)
    connection.send(msg)
    recv_msg = connection.recv(16384)
    recv_msg_dec = recv_msg.decode("utf-8")
    print(recv_msg_dec)
    connection.close()

if __name__ == "__main__":
    start_client()
