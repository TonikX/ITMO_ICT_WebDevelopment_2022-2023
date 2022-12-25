import json
import socket
import threading

from _config import *


class ChatServer:
    class Room:
        def __init__(self, name):
            self.name = name
            self.members = {}

        def send_message(self, user_from, message):
            disconnected_members = []
            for username in self.members:
                try:
                    self.members[username].send(json.dumps({
                        'message': message,
                        'from':    user_from
                    }).encode('utf-8'))
                except BrokenPipeError:
                    disconnected_members.append(username)
            for username in disconnected_members:
                self.remove_member(username)

        def add_member(self, user, client_socket):
            self.members[user] = client_socket
            self.send_message(
                'system',
                f'User "{user}" has joined the room'
            )
            return len(self.members)

        def remove_member(self, user):
            del self.members[user]
            self.send_message(
                'system',
                f'User "{user}" has left the room'
            )
            return len(self.members)

    def __init__(self):
        self.rooms = {}
        logging.debug("Starting server")
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((SOCKET_ADDR, SOCKET_PORT))
        self.socket.listen(100)
        logging.info("TCP server up and listening")

    def process_received_message(self, data_raw, client_socket):
        data = json.loads(data_raw)

        room_name = data.get('room')
        user_from = data.get('from')
        message = data.get('message')
        system_code = data.get('system')

        if room_name not in self.rooms:
            self.rooms[room_name] = self.Room(
                room_name
            )
        room = self.rooms[room_name]

        if message is None:
            if system_code == SYSTEM_CODES.ADD_USER_TO_ROOM:
                room.add_member(
                    user_from,
                    client_socket
                )
            elif system_code == SYSTEM_CODES.REMOVE_USER_FROM_ROOM:
                members_left = room.remove_member(
                    user_from
                )
                if members_left == 0:
                    del self.rooms[room_name]
        else:
            room.send_message(user_from, message)
            logging.debug(self.rooms)

    def client_thread(self, client_socket):
        while True:
            try:
                data_raw = client_socket.recv(SOCKET_BUFF_SIZE)
                if data_raw != b'':
                    logging.debug(data_raw)
                    self.process_received_message(data_raw, client_socket)
            except Exception as e:
                logging.error(e)
                break

    def listen(self):
        while True:
            try:
                client_socket, addr = self.socket.accept()
                logging.debug(addr)

                client_thread = threading.Thread(
                    target=self.client_thread,
                    args=(client_socket,)
                )
                client_thread.start()

            except Exception as e:
                logging.error(e)
                self.socket.close()
                break


if __name__ == '__main__':
    logformat = "%(asctime)s – %(message)s"
    logging.basicConfig(
        format=logformat,
        level=LOGGING_LEVEL,
        datefmt="%H:%M:%S"
    )
    server = ChatServer()
    server.listen()
