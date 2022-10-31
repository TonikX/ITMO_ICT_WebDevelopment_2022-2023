import codecs
f = codecs.open("index.html", 'r', 'utf-8')
print(f.read())


"""page = urllib.request.urlopen("index.html").read() 
print(page)"""


"""f = open (index.html, 'rb')
for line in f:
     print(line.decode('utf8'))"""