import socket 

host = '127.0.0.1'
port = 14901
addr = (host,port)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(addr)
subject = input("Enter a subject: ")
mark = input("Enter a mark: ")
message = f'POST /marks?subject={subject}&mark={mark} HTTP/1.1\r\n'
message += 'Host: example.com\r\n'
message += 'Accept: text/html\r\n\r\n'
message_enc = message.encode("utf-8")
socket.send(message_enc)
recv = socket.recv(16384)
recv_decode = recv.decode("utf-8")
print(recv_decode)