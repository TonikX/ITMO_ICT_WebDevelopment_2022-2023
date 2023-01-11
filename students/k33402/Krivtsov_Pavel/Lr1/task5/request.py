import typing as tp
from urllib.parse import parse_qs, urlparse


class Request:
    def __init__(
            self,
            method: str,
            target: str,
            version: str,
            headers: tp.Dict[str, tp.Any]
    ):
        self.method = method
        self.target = target
        self.version = version
        self.headers = headers

    @property
    def path(self):
        return self._url.path

    @property
    def query(self):
        return parse_qs(self._url.query)

    @property
    def _url(self):
        return urlparse(self.target)
