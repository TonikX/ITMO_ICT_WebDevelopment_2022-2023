from dataclasses import dataclass
from http.client import responses


@dataclass
class Response:
	status: int
	headers: dict[str, str]
	body: str
	reason: str = None

	def __post_init__(self):
		self.reason = responses[self.status]

	def get_http_response(self):
		headers = "\r\n".join([f"{key}: {value}" for key, value in self.headers.items()])
		return f"HTTP/1.1 {self.status} {self.reason}\r\n{headers}\r\n\r\n{self.body}"
