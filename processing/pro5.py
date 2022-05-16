from multiprocessing import Process, Value, Array, Queue, current_process
import os
import time
import logging
from concurrent.futures import Executor, ProcessPoolExecutor, as_completed


log = logging.getLogger(f"app.{__name__}")
stream_handler = logging.StreamHandler()
format = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] - %(message)s"
stream_handler.setFormatter(logging.Formatter(format))
log.addHandler(stream_handler)
log.setLevel(logging.INFO)


def foreach(func, iter):
    for item in iter:
        func(item)


def worker(id, baseNum, q):
    process_id = os.getpid()
    process_name = current_process().name

    sub_total = 0
    for i in range(baseNum):
        sub_total += 1

    q.put(sub_total)

    log.info("process %s %s ", process_id, process_name)
    log.info("result %s", sub_total)


def main():
    total = 0
    parent_process_id = os.getpid()
    log.info("parent_process_id %s", parent_process_id)
    start_time = time.time()

    q = Queue()
    processes = [
        Process(name=str(i), target=worker, args=(1, 10000, q)) for i in range(5)
    ]
    list(map(lambda p: p.start(), processes))
    list(map(lambda p: p.join(), processes))

    q.put("exit")

    while True:
        tmp = q.get()
        if tmp == "exit":
            break
        else:
            total += tmp

    log.info("total %s", total)


if __name__ == "__main__":
    main()
