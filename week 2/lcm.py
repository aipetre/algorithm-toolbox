# Uses python3
# 4 Problem: Least Common Multiple
import sys

"""
Copied from gcm.py
"""
def euclid_gcd(a, b):
    if (b == 0):
        return a

    aprime = a % b
    return euclid_gcd(b, aprime)

"""
The lcm of 2 numbers is their product divided by their gcd
"""
def lcm_fast (a, b):
    lcm = ((a*b) // euclid_gcd(a, b))
    return lcm


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_fast(a, b))

