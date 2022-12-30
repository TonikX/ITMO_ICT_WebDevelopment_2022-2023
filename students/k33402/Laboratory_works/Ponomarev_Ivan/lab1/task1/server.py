import socket
import logging


host = "127.0.0.1"
port = 14900
addr = (host, port)
resp_msg = "Hello, client\n"
logging.basicConfig(filename = './log.log', filemode= 'w', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)

def start_server():
    connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    connection.bind(addr)
    logging.info("Server started")
    msg, client_addr = connection.recvfrom(16384)
    logging.info("Data received from %s port %d" % (addr[0], addr[1]))
    msg_dec = msg.decode("utf-8")
    print(msg_dec)
    connection.sendto(resp_msg.encode("utf-8"), client_addr)
    logging.info("Send response to %s" % (addr[0]))
    connection.close()        

if __name__ == "__main__":
    start_server()