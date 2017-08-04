# Uses python3
import sys

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


def fibonacci_sum_fast(n, p):
    sum = 0

    for i in range(n+1):
        fib_value = get_fibonacci(i % p)
        sum += fib_value

    return sum % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    pisanoPeriod = get_pisano_period(10)
    print(fibonacci_sum_fast(n, pisanoPeriod))
