from typing import Callable


class Subscription:
    id: int
    completion: Callable

    def __init__(self, id: int, completion: Callable):
        self.id = id
        self.completion = completion
