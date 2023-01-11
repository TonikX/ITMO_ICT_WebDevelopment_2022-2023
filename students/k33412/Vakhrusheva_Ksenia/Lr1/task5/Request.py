from dataclasses import dataclass
from urllib.parse import parse_qs, urlparse, ParseResult


@dataclass
class Request:
	method: str
	target: str
	version: str
	headers: dict[str, str]
	data: str
	url: ParseResult = None
	query: dict[str, list[str]] = None
	path: str = None

	def __post_init__(self):
		self.url = urlparse(self.target)
		self.query = parse_qs(self.url.query)
		self.path = self.url.path
