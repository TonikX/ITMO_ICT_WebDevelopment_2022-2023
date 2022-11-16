import socket
import pickle

client = socket.socket()
client.connect(("127.0.0.1", 3300)) 

numb = {
	"a": input("Введите значение а: "),
	"b": input("Введите значение b: "),
	"c": input("Введите значение c: ")
}
numb=pickle.dumps(numb)
client.send(numb) 

data = client.recv(1024)
print(data.decode("utf-8"))

client.close()