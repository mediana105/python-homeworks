import multiprocessing
import threading
import time


def calc_time(func, *args, **kwargs) -> float:
    start_time = time.perf_counter()
    func(*args, **kwargs)
    return time.perf_counter() - start_time


def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def sync_launch(n: int, iterations: int = 10):
    for _ in range(iterations):
        fib(n)


def thread_launch(n: int, iterations: int = 10):
    threads = []
    for _ in range(iterations):
        t = threading.Thread(target=fib, args=(n,))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()


def process_launch(n: int, iterations: int = 10):
    processes = []
    for _ in range(iterations):
        p = multiprocessing.Process(target=fib, args=(n,))
        p.start()
        processes.append(p)
    for process in processes:
        process.join()


if __name__ == "__main__":
    N = 30
    sync_time = calc_time(sync_launch, N)
    thread_time = calc_time(thread_launch, N)
    process_time = calc_time(process_launch, N)
    with open("artifacts/fibonacci.txt", "w") as f:
        f.write(f"Synchronous launch: {sync_time:.4f}\n")
        f.write(f"Thread launch: {thread_time:.4f}\n")
        f.write(f"Process launch: {process_time:.4f}\n")
