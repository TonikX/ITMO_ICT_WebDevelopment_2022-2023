from typing import TypeAlias, Optional
from socket import socket as Socket

Status: TypeAlias = str
Method: TypeAlias = str
Parameters: TypeAlias = str


class Methods:
    login: Method = "login"
    send_message: Method = "send_message"
    subscribe_all_messages = "subscribe_all_messages"


class Statuses:
    success: Status = "Success"
    failure: Status = "Failure"


class Client:
    username: Optional[str] = None
    is_logged_in: bool = False
    subscriptions: [str] = []
