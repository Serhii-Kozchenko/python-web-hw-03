import time
import multiprocessing
import concurrent.futures


def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def factorize_multiprocess(numbers):
    with concurrent.futures.ProcessPoolExecutor() as pool:
        return pool.map(factorize, numbers)

if __name__ == "__main__":
    numbers = [128, 255, 99999, 10651060, 60, 6000, 10000, 120000,130000,100000, 1_000_000, 2_000_000]

    start_time = time.time()
    core1, core2, core3, core4, core5, core6, core7, core8, core9, core10, core11, core12 = factorize_multiprocess(numbers)
    end_time = time.time()
    time_work = end_time-start_time
  
    print("core1:", core1)
    print("core2:", core2)
    print("core3:", core3)
    print("core4:", core4)
    print("core5:", core5)
    print("core6:", core6)
    print("core7:", core7)
    print("core8:", core8)
    print("core9:", core9)
    print("core10:", core10)
    print("core11:", core11)
    print("core12:", core12)

    print(f"Work time: {time_work} seconds")