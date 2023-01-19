import socket

list_lessons = [
  {'lesson': 'Russian', 'description': 'About russian language', 'grade' : [5,5,4,5,4]}
]

def post(msg):
  list_msg = msg.split('&')
  return [list_msg[0][7:], list_msg[1][5:], [int(i) for i in list_msg[2][6:].split('%2C')]]

def start_server():
  serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  serv.bind(('127.0.0.1', 4800))
  serv.listen()
  
  while True:
    client_conn, client_addr = serv.accept()

    with client_conn:
      req = client_conn.recv(1024).decode()
      req_method = req.split(' ')[0]
      req_msg = req.split(' ')[1][1:-1]
      headers = 'HTTP/1.1 200 OK\r\nContent-Type: text.html; charset=UTF-8\r\n\r\n'
      page_content = '<html><head><title>Get</title></head><body>'
      page_content += """
      <form method="get">
        <input type="submit" formaction="add" value="Add" />
        <input type="submit" formaction="show" value="Show" />
      </form>
      """
      if req_method == 'GET':
        if req_msg == 'show':
          page_content += show()
        elif req_msg == 'add':
          page_content += add()
        
      else:
        post_convertation = post(req.split(' ')[-1].split('\r\n\r\n')[1])
        list_lessons.append({'lesson': post_convertation[0], 'description': post_convertation[1], 'grade' : post_convertation[2]})
      
      page_content += "</body></html>"
      client_conn.send(headers.encode('utf-8') + page_content.encode('utf-8'))  
      
def show():
  show = '<ol>'
  for lesson in list_lessons:
    show += '<li>'
    show += f'<p>Name: {lesson["lesson"]}</p>'
    for grade in lesson['grade']:
      show += f'<p>grade: {grade}</p>'
    show += '</li>'
  show += '</ol>'
  return show

def add():
  form = """
  <form action="/" method="post">
    <P>Name: </p>
    <input type="text" name="lesson" value="math"/>
    <P>Desc: </p>
    <input type="text" name="description" value="description" />
    <P>Grades: </p>
    <input type="text" name="grade" value="4,5,5,5,4"/>
    <input type="submit" value="Add"/>
  </form>"""
  return form


start_server();