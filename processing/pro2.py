from multiprocessing import Process
from multiprocessing.dummy import current_process
import os
import random
import time
import logging

from py import process

log = logging.getLogger(f"app.{__name__}")
stream_handler = logging.StreamHandler()
format = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] - %(message)s"
stream_handler.setFormatter(logging.Formatter(format))
log.addHandler(stream_handler)
log.setLevel(logging.INFO)


def square(n):
    time.sleep(random.randint(1, 3))
    process_id = os.getpid()
    process_name = current_process().name

    result = n * n

    log.info("process id : %s, process name %s", process_id, process_name)
    log.info("result %s", result)


def main():
    parent_process_id = os.getpid()

    log.info("process id %s", parent_process_id)

    processes = []

    for i in range(1, 10):
        t = Process(name=str(i), target=square, args=(i,))
        processes.append(t)
        t.start()

    for p in processes:
        p.join()


if __name__ == "__main__":
    main()
