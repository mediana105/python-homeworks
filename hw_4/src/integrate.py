import math
import multiprocessing
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def integrate(f, step, start, end, a) -> float:
    acc = 0.0
    for i in range(start, end):
        acc += f(a + i * step) * step
    return acc


def parallel_integrate(f, a, b, *, n_jobs=4, n_iter=10000000, executor_type='thread') -> float:
    job_size = n_iter // n_jobs
    step = (b - a) / n_iter
    pool_executor = ThreadPoolExecutor if executor_type == 'thread' else ProcessPoolExecutor
    with pool_executor(max_workers=n_jobs) as executor:
        futures = []
        for i in range(n_jobs):
            start = i * job_size
            if i == n_jobs - 1:
                end = n_iter
            else:
                end = (i + 1) * job_size
            future = executor.submit(integrate, f, step, start, end, a)
            futures.append(future)
    return sum(f.result() for f in futures)


def calc_time():
    max_n_jobs = multiprocessing.cpu_count() * 2
    with open("artifacts/integrate.txt", "w") as file:
        for n_jobs in range(1, max_n_jobs + 1):
            start = time.perf_counter()
            parallel_integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs, executor_type='thread')
            thread_time = time.perf_counter() - start

            start = time.perf_counter()
            parallel_integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs, executor_type='process')
            process_time = time.perf_counter() - start
            file.write(
                f"{n_jobs}. thread pool time:  {thread_time:.4f}; process pool time: {process_time:.4f}\n")


if __name__ == "__main__":
    calc_time()
