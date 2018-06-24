import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1, 1):
        if n % i == 0:
            return False
    if n == 0 or n == 1:
        return False
    else:
        return True


if __name__ == '__main__':
    for i in range(0, 100):
        if is_prime(i):
            print(i)
