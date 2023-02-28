import asyncio
import socket

connections = []

async def handle_client(client, address):
    request = None
    while request != 'покинуть':
        request = (await loop.sock_recv(client, 255)).decode('utf8')
        response = f'User{address}: ' + str(request)
        if request == 'покинуть':
            response = f'User {address} left the chat'
        for client_ in connections:
            if client_ == client:
                continue
            await loop.sock_sendall(client_, response.encode('utf8'))
    connections.remove(client)
    print(f'Client: {address} disconnected')
    client.close()


async def run_server():
    while True:
        client, address = await loop.sock_accept(server)
        if client not in connections:
            connections.append(client)
        print(f'Client {address} connected to the chat!')
        loop.create_task(handle_client(client, address))


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 53330))
server.listen(8)
server.setblocking(False)

loop = asyncio.get_event_loop()
loop.run_until_complete(run_server())