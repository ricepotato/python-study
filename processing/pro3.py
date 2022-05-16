from asyncio import futures
from multiprocessing import Process
from multiprocessing.dummy import current_process
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


def load_url(url, timeout):
    log.info("load url %s", url)
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()


def main():
    urls = [
        "https://www.daum.net",
        "https://www.cnn.com",
        "https://www.naver.com",
        "https://ruliweb.com",
    ]

    with ProcessPoolExecutor(max_workers=5) as executor:
        future_to_url = {executor.submit(load_url, url, 60): url for url in urls}

        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                _ = future.result()
            except Exception as e:
                log.error("error %s url %s", e, url)
            else:
                log.info("%s page load.", url)


if __name__ == "__main__":
    main()
