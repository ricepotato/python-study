import logging
import time
from concurrent.futures import ThreadPoolExecutor
import threading
import multiprocessing


log = logging.getLogger(f"app.{__name__}")
stream_handler = logging.StreamHandler()
format = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] - %(message)s"
stream_handler.setFormatter(logging.Formatter(format))
log.addHandler(stream_handler)
log.setLevel(logging.INFO)


class FakeDataStore:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def update(self, n):
        log.info("threa %s : starting update", n)

        # self._lock.acquire()
        # log.info("thread %s has lock", n)
        # local_copy = self.value
        # local_copy += 1
        # time.sleep(0.1)
        # self.value = local_copy

        # log.info("thread %s release", n)
        # self._lock.release()

        with self._lock:
            log.info("thread %s has lock", n)
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy

        log.info("threa %s : finishing update", n)


if __name__ == "__main__":
    store = FakeDataStore()

    with ThreadPoolExecutor(max_workers=2) as executor:
        for n in ["first", "second", "thrid"]:
            executor.submit(store.update, n)

    log.info("result store value = %s", store.value)
