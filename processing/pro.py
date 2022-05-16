from multiprocessing import Process
import time
import logging

log = logging.getLogger(f"app.{__name__}")
stream_handler = logging.StreamHandler()
format = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] - %(message)s"
stream_handler.setFormatter(logging.Formatter(format))
log.addHandler(stream_handler)
log.setLevel(logging.INFO)


def proc_func(name):
    log.info("Sub-process %s: start", name)
    time.sleep(3)
    log.info("sub process %s: finish", name)


def main():
    p = Process(target=proc_func, args=("first",))
    log.info("main process: before create process")
    p.start()
    log.info("main process: join process")

    p.join()

    log.info("process p is alive: %s", p.is_alive())


if __name__ == "__main__":
    main()
