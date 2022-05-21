from multiprocessing import Process, Value, Array, Queue, current_process
import os
import time
import logging
from tkinter import font
import requests
from concurrent.futures import (
    Executor,
    ProcessPoolExecutor,
    as_completed,
    ThreadPoolExecutor,
)
import threading

log = logging.getLogger(f"app.{__name__}")
stream_handler = logging.StreamHandler()
format = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] - %(message)s"
stream_handler.setFormatter(logging.Formatter(format))
log.addHandler(stream_handler)
log.setLevel(logging.INFO)

thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def request_site(url):
    session = get_session()

    with session.get(url) as response:
        log.info("read conetnt %s status code %s", url, response.status_code)


def request_all_sites(urls):
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(request_site, urls)


def main():
    pass


if __name__ == "__main__":
    main()
