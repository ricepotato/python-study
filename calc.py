import time
import logging
import functools
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

log = logging.getLogger(f"app.{__name__}")
stream_handler = logging.StreamHandler()
format = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] - %(message)s"
stream_handler.setFormatter(logging.Formatter(format))
log.addHandler(stream_handler)
log.setLevel(logging.INFO)


def duration_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        st_time = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - st_time
        print(f"function {func.__name__} duration {duration} sec.")
        return result

    return wrapper


def calc(number):
    return sum(i * i for i in range(number))


def get_sums(numbers):
    result = []
    for number in numbers:
        result.append(calc(number))
    return result


@duration_time
def get_thread_sums(numbers):
    with ThreadPoolExecutor(max_workers=5) as executor:
        return executor.map(calc, numbers)


@duration_time
def get_process_sums(numbers):
    with ProcessPoolExecutor(max_workers=5) as executor:
        return executor.map(calc, numbers)


def main():
    numbers = [3_000_000 + x for x in range(30)]

    st_time = time.time()
    # total = get_sums(numbers)
    total = get_thread_sums(numbers)
    # total = get_process_sums(numbers)

    duration = time.time() - st_time

    print(sum(total))
    print(duration)


if __name__ == "__main__":
    main()
