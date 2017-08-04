# Uses python3
# 5 Advanced Problem: Huge Fibonacci Number modulo m
import sys

"""
Calculates the Pisano period for a number
@see https://en.wikipedia.org/wiki/Pisano_period
"""
def get_pisano_period(modulo):
    a = 0
    b = 1
    c = a + b
    for i in range(0, modulo * modulo):
        c = (a + b) % modulo
        a = b
        b = c
        if (a == 0 and b == 1):
            return i + 1


def get_fibonacci(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current

"""
Calculates Fibonnaci(n) % m
"""
def get_fibonacii_modulo(n, m):
    if n <= 1:
        return n

    k = get_pisano_period(m)
    fib_value = get_fibonacci(n % k)

    return fib_value % m



if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacii_modulo(n, m))