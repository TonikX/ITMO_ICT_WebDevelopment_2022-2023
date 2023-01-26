import typing as tp


class Response:
    def __init__(
            self,
            status: int,
            reason: str,
            headers: tp.Optional[tp.Dict[str, tp.Any]] = None,
            body: tp.Optional[bytes] = None
    ):
        self.status = status
        self.reason = reason
        self.headers = headers
        self.body = body
