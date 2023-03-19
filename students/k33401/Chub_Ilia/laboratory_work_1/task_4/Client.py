from Request import Request
from Response import Response
from Subscription import Subscription
from RequestCompletionable import RequestCompletionable

import threading
import Configs
import sys

from Entities import *

sys.path.append('..')
from Base.TCPClient import *


class Client(TCPClient):
    requests_count: int = 0
    requests: [RequestCompletionable] = []
    subscriptions: [Subscription] = []
    is_waiting_message = True

    def handle_message(self, message: str):
        if len(message) == 0:
            self.close_socket()

        response = Response.decode(string=message)

        subscription: Subscription = next((x for x in self.subscriptions if x.id == response.id), None)
        request: RequestCompletionable = next((x for x in self.requests if x.id == response.id), None)

        if subscription is not None:
            if response.status == Statuses.success:
                subscription.completion(response.parameters)
            else:
                self.subscriptions = list(filter(lambda x: response.id != x.id, self.subscriptions))
        elif request is not None:
            if response.status == Statuses.success:
                request.success_closure()
            else:
                request.failure_closure()

            self.requests = list(filter(lambda x: response.id != x.id, self.requests))
        else:
            print(f'\x1b[2A\n\n{response.parameters}')

    def start_get_messages_thread(self):
        threading.Thread(target=self.wait_to_get_message).start()

    def wait_to_get_message(self):
        def failure_closure():
            self.is_waiting_message = False

        while self.is_waiting_message:
            self.receive_message(failure_closure=failure_closure)

    def start_send_messages_thread(self):
        threading.Thread(target=self.wait_to_send_user_message).start()

    def login(self, username: str):
        def success_closure():
            print("SUCCESS LOGIN")
            self.is_possible_to_send_message = True
            self.start_send_messages_thread()
            self.subscribe_all_messages()

        def failure_closure():
            print(f"FAILED! THE USERNAME {username} IS NOT UNIQUE!")

        self.start_get_messages_thread()

        self.send_request(
            method=Methods.login,
            parameters=username,
            success_closure=success_closure,
            failure_closure=failure_closure
        )

    def subscribe_all_messages(self):
        def subscription_completion(message):
            print(f'\x1b[2A\n\n{message}')

        self.subscribe(method=Methods.subscribe_all_messages, subscription_completion=subscription_completion)

    def subscribe(self, method: Method, subscription_completion: Callable):
        subscription = Subscription(id=self.requests_count+1, completion=subscription_completion)

        def success_closure():
            print(f"SUCCESS SUBSCRIPTION {method}")
            self.subscriptions.append(subscription)

        def failure_closure():
            print(f"Impossible to subscribe with method {method}")

        self.send_request(
            method=method,
            parameters='nil',
            success_closure=success_closure,
            failure_closure=failure_closure
        )

    def send_request(
        self,
        method: Method,
        parameters: Parameters,
        success_closure: Callable,
        failure_closure: Callable
    ):
        self.requests_count += 1
        request = Request(id=self.requests_count, method=method, parameters=parameters)
        requestCompletionable = RequestCompletionable(
            id=self.requests_count,
            success_closure=success_closure,
            failure_closure=failure_closure
        )

        print(f"THE REQUEST HAS BEEN SENT: {method}")
        self.requests.append(requestCompletionable)
        self.send_message(message=request.encode())

    def wait_to_send_user_message(self):
        try:
            message = input()

            self.send_user_message(message=message)
        except BaseException as error:
            self.handle_error(error=error)

    def send_user_message(self, message: str):
        def success_closure():
            self.start_send_messages_thread()

        def failure_closure():
            print(f"SENDING ERROR")

        self.send_request(
            method=Methods.send_message,
            parameters=message,
            success_closure=success_closure,
            failure_closure=failure_closure
        )


if __name__ == "__main__":
    client = Client(server_socket_address=Configs.server_socket_address, timeout=240)
    client.connect()

    try:
        username = input("Enter your username: ")

        client.login(username=username)
    except BaseException as error:
        client.handle_error(error=error)
