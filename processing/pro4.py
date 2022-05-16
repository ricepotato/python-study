from asyncio import futures
from multiprocessing import Process, Value, Array
import os
import random
import time
import logging
from concurrent.futures import Executor, ProcessPoolExecutor, as_completed
import urllib.request


log = logging.getLogger(f"app.{__name__}")
stream_handler = logging.StreamHandler()
format = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] - %(message)s"
stream_handler.setFormatter(logging.Formatter(format))
log.addHandler(stream_handler)
log.setLevel(logging.INFO)


def generate_update_number(v):
    log.info("gen number")
    for _ in range(400):
        v.value += 1
    log.info("value %s", v.value)


def main():
    parent_process_id = os.getpid()

    processes = []
    share_value = Value("i", 0)

    for _ in range(1, 10):
        p = Process(target=generate_update_number, args=(share_value,))
        processes.append(p)
        log.info("start process %s", _)
        p.start()

    for p in processes:
        p.join()


if __name__ == "__main__":
    main()
