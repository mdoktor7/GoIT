from time import time
from multiprocessing import Pool, cpu_count
import concurrent.futures


def factorize(number):
    result = []
    for num in number:
        num_list = []
        for i in range(1, num + 1):
            if num % i == 0:
                num_list.append(i)
        result.append(num_list)
    return result


def factorize_process(number):
    num_list = []
    for i in range(1, number + 1):
        if number % i == 0:
            num_list.append(i)
    return num_list


if __name__ == '__main__':
    numbers = [128000, 25500, 99999000, 106510600]

    start_sing = time()
    stop_sing = time()
    print(f"Run time for single thread is {stop_sing - start_sing} sec")

    print(f"cpu_count = {cpu_count()}")

    with Pool(processes=cpu_count()) as pool:
        pool.map(factorize_process, numbers)
        pool.close()
    start_pool = time()
    stop_pool = time()
    print(f"Proces pool timer {stop_pool - start_pool} sec")

    with concurrent.futures.ProcessPoolExecutor(cpu_count()) as executor:
        executor.map(factorize_process, numbers)
    start_exec = time()
    stop_exec = time()
    print(f"Executor pool timer {stop_exec - start_exec} sec")
