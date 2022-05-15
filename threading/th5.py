import logging
import queue
import time
import random
from concurrent.futures import ThreadPoolExecutor
import threading
import multiprocessing


log = logging.getLogger(f"app.{__name__}")
stream_handler = logging.StreamHandler()
format = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] - %(message)s"
stream_handler.setFormatter(logging.Formatter(format))
log.addHandler(stream_handler)
log.setLevel(logging.INFO)


def producer(queue, event):
    while not event.is_set():
        message = random.randint(1, 11)

        # log.info("producer make message %s", message)
        time.sleep(0.5)
        queue.put(message)

    logging.info("producer exiting")


def consumer(queue, event):
    while not event.is_set() or not queue.empty():
        message = queue.get()
        log.info("consumer got message %s size=%s", message, queue.qsize())

    logging.info("consumer exiting")


def main():
    event = threading.Event()
    pipeline = queue.Queue()

    with ThreadPoolExecutor(max_workers=2) as executor:
        pass
        # future1 = executor.submit(producer, pipeline, event)
        # future2 = executor.submit(consumer, pipeline, event)

    time.sleep(3)

    log.info("set event!")
    event.set()


if __name__ == "__main__":
    main()
