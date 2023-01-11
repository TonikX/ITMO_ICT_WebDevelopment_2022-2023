from functools import lru_cache
from urllib.parse import parse_qs, urlparse

class request:
    def __init__(self, method, target, version, headers, rfile):
        self.method = method
        self.target = target
        self.version = version
        self.headers = headers
        self.rfile = rfile

    @property
    def path(self):
        return self.url.path
    
    @property
    def query(self):
        return parse_qs(self.url.query)
    
    @property
    def url(self):
        return urlparse(self.target)
        