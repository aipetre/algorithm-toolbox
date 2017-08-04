#Uses python3
# 3 Problem: Greatest Common Divisor

import sys

"""
Calculates the gcd using Euclid's algorithm
@see https://en.wikipedia.org/wiki/Euclidean_algorithm
"""
def euclidGcd(a, b):
    if (b == 0):
        return a

    aprime = a % b
    return euclidGcd(b, aprime)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print (euclidGcd(a, b))