import time

def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors



if __name__ == "__main__":
    numbers = [128, 255, 99999, 10651060, 60, 6000, 10000, 120000,130000,100000,  1_000_000, 2_000_000 ]    

    start_time = time.time()
    a, b, c, d, e, f, g ,h, k, l, m, n = [factorize(number) for number in numbers]
    end_time = time.time()
    time_work = end_time-start_time
    
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)
    print("e:", e)
    print("f:", f)
    print("g:", g)
    print("k:", k)
    print("h:", h)
    print("l:", l)
    print("l:", m)
    print("l:", n)

    print(f"Work time: {time_work} seconds")

  