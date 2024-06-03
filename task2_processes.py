import time
from collections import defaultdict
from multiprocessing import Pool, current_process, cpu_count

def factorize_sync(*number):
    divisors = defaultdict(list)
    for num in number:
        result = []
        for i in range(1, num + 1):
            if num % i == 0:
                result.append(i)
        divisors[num] = result
    return divisors.values()

def factorize_async(number):
    result = []
    for i in range(1, number + 1):
        if number % i == 0:
            result.append(i)
            continue
    print(f"{number}: {result}")
    return result

def callback(result):
    print(f"Result in callback: {result}")

if __name__ == "__main__":
    # Виклик функції з синхроним кодом
    start_time = time.perf_counter()
    a, b, c, d  = factorize_sync(128, 255, 99999, 10651060)
    end_time = time.perf_counter()
    print(f"Час виконання синхронного коду: {end_time - start_time} секунд")

    # Виклик функції з асинхроним кодом
    print(f"Count CPU: {cpu_count()}")
    start_time = time.perf_counter()
    with Pool(cpu_count()) as p:
        p.map_async(
            factorize_async,
            [128, 255, 99999, 10651060],
            callback=callback
        )
        end_time = time.perf_counter()
        p.close()
        p.join()
    print(f"Час виконання aсинхронного коду: {end_time - start_time} секунд")
    print(f'End {current_process().name}')



# assert a == [1, 2, 4, 8, 16, 32, 64, 128]
# assert b == [1, 3, 5, 15, 17, 51, 85, 255]
# assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
# assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]