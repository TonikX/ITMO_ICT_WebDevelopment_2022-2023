import socket

lessons = [
  {'name': 'Python', 'desc': 'Client/Server', 'marks' : [4,5]}
]

def post_func(post_msg):
  info = post_msg.split('&')
  return [info[0][7:], info[1][5:], [int(i) for i in info[2][6:].split('%2C')]]

def get():
  html = '<ol>'
  for lesson in lessons:
    html += '<li>'
    html += f'<h1>Lesson: {lesson["name"]}</h1>'
    for mark in lesson['marks']:
      html += f'<p>grade: {mark}</p>'
    html += '</li>'
  html += '</ol>'
  return html

def add():
  form = """
  <form action="/" method="post">
    <P>Lesson: </p>
    <input type="text" name="lesson" value="math"/>
    <P>Description: </p>
    <input type="text" name="desc" value="numbers"/>
    <P>Grades: </p>
    <input type="text" name="marks" value="5,5,5"/>
    <br/>
    <input type="submit" value="Add lesson"/>
  </form>"""
  return form

def start_server():
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind(('127.0.0.1', 4245))
  server.listen()
  
  while True:
    client, addr = server.accept()

    with client:
      request = client.recv(1024).decode()
      method = request.split(' ')[0]
      message = request.split(' ')[1][1:-1]
      setting = 'HTTP/1.1 200 OK\r\nContent-Type: text.html; charset=UTF-8\r\n\r\n'
      html = '<html><head><title>Website</title></head><body>'
      html += """
      <form method="get">
        <input type="submit" formaction="add" value="Add" />
        <input type="submit" formaction="get" value="Show" />
      </form>
      """
      if method == 'GET':
        if message == 'get':
          html += get()
        elif message == 'add':
          html += add()
      else:
        post = post_func(request.split(' ')[-1].split('\r\n\r\n')[1])
        lessons.append({'name': post[0], 'desc': post[1], 'marks' : post[2]})
      
      html += "</body></html>"
      client.send(setting.encode('utf-8') + html.encode('utf-8'))  
      
start_server();