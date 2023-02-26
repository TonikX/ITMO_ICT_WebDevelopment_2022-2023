from Entities import Method, Parameters
from NetworkEntity import NetworkEntity


class Request(NetworkEntity):
    method: Method
    parameters: Parameters

    def __init__(self, id: int, method: Method, parameters: Parameters):
        self.id = id
        self.method = method
        self.parameters = parameters

    def encode(self) -> str:
        return f"{self.id}{self.Constants.separator}{self.method}{self.Constants.separator}{self.parameters}"

    @classmethod
    def decode(cls, string: str):
        id, method, parameters = string.split(NetworkEntity.Constants.separator)

        return cls(id=int(id), method=method, parameters=parameters)
