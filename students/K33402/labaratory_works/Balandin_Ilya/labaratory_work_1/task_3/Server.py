import socket
 
sock = socket.socket()
sock.bind(('127.0.0.1', 1337))
sock.listen(1)
 
while True:
	conn, addr = sock.accept()
 
	html_page = open('index.html')
	html_content = html_page.read()
	html_page.close()
 
	html_response = 'HTTP/1.0 200 OK\n' + html_content 
 
	conn.sendall(html_response.encode('utf-8'))
 
conn.close()