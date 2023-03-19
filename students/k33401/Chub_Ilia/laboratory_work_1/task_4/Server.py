import threading
import Configs

from Request import Request
from Response import Response
from Entities import *
from typing import Dict

import sys

sys.path.append('..')
from Base.AsyncTCPServer import *


class Server(AsyncTCPServer):
    clients: Dict[socket_module.socket, Client] = {}

    def save_client(self, client_socket: socket_module.socket):
        self.clients[client_socket] = Client()

    def get_client_sockets(self) -> [socket_module.socket]:
        return self.clients.keys()

    def handle_message(self, message: str, client_socket_address: SocketAddress):
        if len(message) == 0:
            return self.disconnect_client(client_socket_address=client_socket_address)

        request = Request.decode(string=message)

        if request.method == Methods.login:
            self.handle_login_request(
                id=request.id,
                username=request.parameters,
                client_socket_address=client_socket_address
            )
        elif request.method == Methods.subscribe_all_messages:
            self.handle_subscribe_all_messages_request(id=request.id, client_socket_address=client_socket_address)
        elif request.method == Methods.send_message:
            self.handle_send_message_request(
                id=request.id,
                user_message=request.parameters,
                client_socket_address=client_socket_address
            )

    def disconnect_client(self, client_socket_address: SocketAddress):
        client_socket, client = self.get_client_socket_and_client(client_socket_address=client_socket_address)

        if client_socket is None or client is None:
            return

        print(f"USER {client.username} DISCONNECTED")

        self.clients = {key: value for key, value in self.clients.items() if key.getpeername() != client_socket_address}

        client_socket.close()

    def handle_login_request(self, id: int, username: str, client_socket_address: SocketAddress):
        status: Status

        client_socket, client = self.get_client_socket_and_client(client_socket_address=client_socket_address)

        if len(list(filter(lambda x: x.username == username, self.clients.values()))) > 0:
            print(f"THE USER ({username}) IS ALREADY IN THE CHAT")

            status = Statuses.failure
        else:
            print(f"{username} LOGGED IN")

            status = Statuses.success
            client.username = username
            client.is_logged_in = True

        response = Response(id=id, status=status, parameters="nil")

        self.send_response(response=response, client_socket=client_socket)

    def handle_subscribe_all_messages_request(self, id: int, client_socket_address: SocketAddress):
        click_socket, client = self.get_client_socket_and_client(client_socket_address=client_socket_address)

        client.subscriptions.append(Methods.subscribe_all_messages)

        response = Response(id=id, status=Statuses.success, parameters="nil")

        self.send_response(response=response, client_socket=click_socket)

    def handle_send_message_request(self, id: int, user_message: str, client_socket_address: SocketAddress):
        sender_socket, sender = self.get_client_socket_and_client(client_socket_address=client_socket_address)
        message = f"{sender.username}: {user_message}"
        response = Response(id=-1, status=Statuses.success, parameters=message)

        for client_socket, client in self.clients.items():
            if client.is_logged_in and sender.username != client.username:
                self.send_response(response=response, client_socket=client_socket)

        sender_response = Response(id=id, status=Statuses.success, parameters="nil")

        self.send_response(response=sender_response, client_socket=sender_socket)

    def send_response(self, response: Response, client_socket: socket_module.socket):
        response_message = response.encode()

        self.send_message(message=response_message, client_socket=client_socket)

    def get_client_socket_and_client(
        self,
        client_socket_address: SocketAddress
    ) -> (Optional[socket_module.socket], Optional[Client]):
        try:
            return next(
                (key, value) for key, value in self.clients.items() if key.getpeername() == client_socket_address
            )
        except:
            return None, None


if __name__ == "__main__":
    server = Server(socket_address=Configs.server_socket_address, number_to_listening=Configs.server_listen_number)

    server.listen()
