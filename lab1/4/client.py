import json
import signal
import socket
import threading

from _config import *


class ChatClient:
    def __init__(self, username):
        self.shutdown_from_thread = False
        self.shutdown = threading.Event()
        self.thread_sending = None
        self.thread_receiving = None
        self.room = None
        self.username = username
        logging.debug('Connecting to server')
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((SOCKET_ADDR, SOCKET_PORT))
        logging.debug('Connected successfully')

    def select_room(self):
        self.leave_room()
        self.room = input('Enter chat room name (leave blank to exit): ')
        if self.room == '':
            self.graceful_shutdown()
        print(f'Chat room "{self.room}" selected\n'
              f'To change room enter "exit-room" in message box\n'
              f'To send message enter text and hit "Enter"')
        self.socket.send(
            json.dumps({
                'message': None,
                'system':  SYSTEM_CODES.ADD_USER_TO_ROOM,
                'from':    self.username,
                'room':    self.room
            }).encode('utf-8')
        )

    def leave_room(self):
        if self.room is not None:
            self.socket.send(
                json.dumps({
                    'message': None,
                    'system':  SYSTEM_CODES.REMOVE_USER_FROM_ROOM,
                    'from':    self.username,
                    'room':    self.room
                }).encode('utf-8')
            )

    def graceful_shutdown(self, *args):
        self.leave_room()
        self.socket.close()
        self.shutdown.set()
        if not self.shutdown_from_thread:
            logging.info('Press enter to shutdown')
            self.thread_sending.join()
            self.thread_receiving.join()

    def listen(self):
        if self.room is None:
            self.select_room()
        self.thread_sending = threading.Thread(
            target=self.serve_sending
        )
        self.thread_receiving = threading.Thread(
            target=self.serve_receiving
        )
        self.thread_receiving.start()
        self.thread_sending.start()

    def serve_receiving(self):
        while not self.shutdown.is_set():
            try:
                data_raw = self.socket.recv(SOCKET_BUFF_SIZE)
                if data_raw != b'':
                    data = json.loads(data_raw)
                    print(f"{data.get('from')}: {data.get('message')}")
                    logging.debug(data_raw.decode('utf-8'))
            except Exception as e:
                logging.error(e)
                break

    def serve_sending(self):
        while not self.shutdown.is_set():
            try:
                message = input()
                if message == 'exit-room':
                    self.select_room()
                elif message == 'exit':
                    self.shutdown_from_thread = True
                    self.graceful_shutdown()
                else:
                    self.socket.send(
                        json.dumps({
                            'message': message,
                            'from':    self.username,
                            'room':    self.room
                        }).encode('utf-8')
                    )
                    logging.debug('sent message')
            except Exception as e:
                logging.error(e)
                break


if __name__ == '__main__':
    logformat = "%(asctime)s – %(message)s"
    logging.basicConfig(
        format=logformat,
        level=LOGGING_LEVEL,
        datefmt="%H:%M:%S"
    )

    username = input('Enter username: ')
    client = ChatClient(username)

    signal.signal(signal.SIGINT, client.graceful_shutdown)
    signal.signal(signal.SIGTERM, client.graceful_shutdown)

    client.listen()
