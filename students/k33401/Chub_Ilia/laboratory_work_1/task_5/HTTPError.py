from typing import Optional


class HTTPError(Exception):
    status: int
    reason: str
    body: Optional[str]

    def __init__(self, status: int, reason: str, body: Optional[str] = None):
        super()

        self.status = status
        self.reason = reason
        self.body = body
