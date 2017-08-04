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
        if a == 0 and b == 1:
            return i + 1


def get_fibonacci_last_digit(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, ((previous + current) % 10)

    return current

""" The sum of the first n Fibonnaci numbers is
actuall the F(n+2) - 1 value
Calculates the Pisano period of 10
Calculates the (n+2) % 10 Fibonnaci element 
"""
def fibonacci_last_digit_of_sum(n, p):
    sum_last_digit = 0

    k = get_pisano_period(10)
    element_to_find = (n+2) % k

    fib_value = get_fibonacci_last_digit(element_to_find)
    sum_last_digit = fib_value - 1
        
    return sum_last_digit % 10

def fibonnaci_partial_sum_last_digit(from_, to):
    retValue = 0
    fromValue = fibonacci_last_digit_of_sum(from_ - 1, 10)
    toValue = 10 + fibonacci_last_digit_of_sum(to, 10)
    retValue = (toValue - fromValue) % 10

    return retValue


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonnaci_partial_sum_last_digit(from_, to))