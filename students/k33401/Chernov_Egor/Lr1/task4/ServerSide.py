import concurrent.futures
import queue
import socket
import threading


def connect_user(sock):
    conn = sock.accept()[0]
    with conn:
        conn.recv(16384)


def producer(queue, event):
    """We're saving a message in a queue."""
    while not event.is_set():
        message = ""
        queue.put(message)


def consumer(queue, event):
    """We're getting a message from the queue and send to a chat."""
    while not event.is_set() or not pipeline.empty():
        message = queue.get()


with socket.socket() as s:
    s.bind(('', 8080))
    s.listen(4)

    pipeline = queue.Queue(10)
    event = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(4) as executor:
        executor.submit(connect_user, s)
        # executor.submit(producer, pipeline, event)
        # executor.submit(consumer, pipeline, event)

        # time.sleep(0.1)

        # event.set()
