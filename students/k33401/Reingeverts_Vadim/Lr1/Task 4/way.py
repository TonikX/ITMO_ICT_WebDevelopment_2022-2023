import time
from io import StringIO


class Line():
    def __init__(self):
        self.value = ""

    def __call__(self, *args, start=0, sep=" "):
        chars = 0
        io = StringIO()
        print(*args, file=io, end="", sep=sep)
        text = io.getvalue()
        self.value = (self.value[:start] + " " * (start - len(self.value))
                      + text + self.value[start + len(text):])
        print(self.value, chr(8) * len(self.value), sep="", end="", flush=True)

    def __next__(self):
        self.value = ""
        print()


def greet():
    line = Line()
    line("hello", start=2)
    time.sleep(1)
    line("world", start=8)
    time.sleep(1)
    line("hi   ", start=2)
    time.sleep(1)
    line("world ", start=7)
    time.sleep(0.3)
    line("world ", start=6)
    time.sleep(0.3)
    line("world ", start=5)
    time.sleep(1)
    line("globe", start=5)
    time.sleep(1)
    for _ in range(4):
        for c in "! ":
            line(c, start=10)
            time.sleep(0.3)
    line("!", start=10)
    time.sleep(1)
    next(line)


greet()
