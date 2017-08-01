#Uses python3
import sys

def euclidGcd(a, b):
    if (b == 0):
        return a

    aprime = a % b
    return euclidGcd(b, aprime)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print (euclidGcd(a, b))