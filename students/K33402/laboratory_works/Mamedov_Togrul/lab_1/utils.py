import dataclasses
from urllib.parse import parse_qs, urlparse
from typing import Optional


@dataclasses.dataclass
class Request:
    def __init__(self, method, target, headers, version, data):
        self.method = method
        self.target = target
        self.version = version
        self.url = urlparse(self.target)
        self.query = parse_qs(self.url.query)
        self.path = self.url.path
        self.headers = headers
        self.data = data


@dataclasses.dataclass
class Response:
    status: int
    reason: str

    body: Optional[str] = None
    headers: str = "Content-Type: text/html; charset=utf-8"
