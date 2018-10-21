from clockdeco2 import clock

import functools


@functools.lru_cache()
@clock
def fibonacci(n):
    return n if n < 2 else fibonacci(n - 2) + fibonacci(n - 1)


@clock
def fibonacci_recursive(n):
    if n < 2:
        return n
    return fibonacci_recursive(n - 2) + fibonacci_recursive(n - 1)


if __name__ == '__main__':
    print(fibonacci_recursive(6))
    print('*' * 40)
    print(fibonacci(6))
