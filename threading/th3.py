import logging
import time
from concurrent.futures import ThreadPoolExecutor

log = logging.getLogger(f"app.{__name__}")
stream_handler = logging.StreamHandler()
format = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] - %(message)s"
stream_handler.setFormatter(logging.Formatter(format))
log.addHandler(stream_handler)
log.setLevel(logging.INFO)


def task(name):
    log.info("Sub - Thread %s : starting", name)

    result = 0
    for i in range(10000):
        result += i

    log.info("Sub - Thread %s : finishing result %s", name, result)
    return result


def main():
    log.info("Main - Thread: before creating and running thread.")

    # excutor = ThreadPoolExecutor(max_workers=3)
    # task1 = excutor.submit(task, ("First",))
    # task2 = excutor.submit(task, ("Second",))

    # log.info("result 1 %s", task1.result())
    # log.info("result 2 %s", task2.result())

    with ThreadPoolExecutor(max_workers=5) as executor:
        tasks = executor.map(task, ["first", "second", "third"])
        log.info(list(tasks))


if __name__ == "__main__":
    main()
