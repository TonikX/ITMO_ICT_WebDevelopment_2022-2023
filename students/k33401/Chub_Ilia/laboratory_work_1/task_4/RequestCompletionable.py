from NetworkEntity import NetworkEntity
from typing import Callable


class RequestCompletionable(NetworkEntity):
    success_closure: Callable
    failure_closure: Callable

    def __init__(
        self, id: int,
        success_closure: Callable,
        failure_closure: Callable
    ):
        self.id = id
        self.success_closure = success_closure
        self.failure_closure = failure_closure
