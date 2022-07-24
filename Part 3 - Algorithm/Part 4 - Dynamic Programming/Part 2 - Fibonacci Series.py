import time


def fibonacci(n):
    if n < 2:
        return n

    return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_dynamic():
    cache = {}

    def fibonacci_cache(n: int):
        if n in cache:
            return cache[n]
        else:
            if n < 2:
                return n
            else:
                cache[n] = fibonacci_cache(n-1) + fibonacci_cache(n-2)
                return cache[n]
    return fibonacci_cache


def fibonacci_dynamic2(n):
    answer = [0, 1]
    for i in range(2, n+1):
        answer.append(answer[i-2] + answer[i-1])
    return answer[-1]


if __name__ == "__main__":
    then = int(round(time.time() * 1000))
    print(fibonacci(30))
    print(f"Took {int(round(time.time() * 1000)) - then} milliseconds")

    then = int(round(time.time() * 1000))
    fibonacci_faster = fibonacci_dynamic()
    print(fibonacci_faster(30))
    print(f"Took {int(round(time.time() * 1000)) - then} milliseconds")

    then = int(round(time.time() * 1000))
    print(fibonacci_dynamic2(30))
    print(f"Took {int(round(time.time() * 1000)) - then} milliseconds")
