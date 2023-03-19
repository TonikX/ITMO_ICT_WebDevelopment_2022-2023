from Entities import Status, Parameters
from NetworkEntity import NetworkEntity


class Response(NetworkEntity):
    status: Status
    parameters: Parameters

    def __init__(self, id: int, status: Status, parameters: Parameters):
        self.id = id
        self.status = status
        self.parameters = parameters

    def encode(self) -> str:
        return f"{self.id}{self.Constants.separator}{self.status}{self.Constants.separator}{self.parameters}"

    @classmethod
    def decode(cls, string: str):
        id, status, parameters = string.split(NetworkEntity.Constants.separator)

        return cls(id=int(id), status=status, parameters=parameters)
