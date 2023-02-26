from email.message import Message
from urllib.parse import parse_qs, urlparse, ParseResult
from typing import Dict, List, Any


class Request:
    method: str
    target: str
    version: str
    headers: str
    path: str
    query: Dict[str, List[Any]]

    def __init__(self, method: str, target: str, version: str, headers: [Message]):
        self.method = method
        self.target = target
        self.version = version
        self.headers = headers
        url = self.get_url(target=target)
        self.path = self.get_path(url=url)
        self.query = self.get_query(url=url)

    @staticmethod
    def get_path(url: ParseResult) -> str:
        return url.path

    @staticmethod
    def get_query(url: ParseResult):
        return parse_qs(url.query)

    @staticmethod
    def get_url(target: str) -> ParseResult:
        return urlparse(target)
