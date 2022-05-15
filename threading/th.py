import time
import logging
import threading

log = logging.getLogger(f"app.{__name__}")
stream_handler = logging.StreamHandler()
format = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] - %(message)s"
stream_handler.setFormatter(logging.Formatter(format))
log.addHandler(stream_handler)
log.setLevel(logging.INFO)


def thread_func(name):
    """메인 thread 가 끝나더라도 sub thread 가 작업을 완료함"""
    log.info("Sub-Thread %s : strting", name)
    time.sleep(3)
    log.info("Sub-Thread %s : finished", name)


if __name__ == "__main__":
    log.info("Main-Thread: before createing thread")

    x = threading.Thread(target=thread_func, args=("first",))

    log.info("Main-Trhead : before running thread")

    x.start()
    x.join()  # 대기

    log.info("Main-Thread: wait for the thread to finish.")

    log.info("Main-Thread: all done.")
