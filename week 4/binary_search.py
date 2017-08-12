# Uses python3
# 1 Binary Search
import sys

def do_binary_search(a, low, high, v):
    if high < low:
        # not found
        return - 1

    mid = low + ((high - low ) // 2)

    if v == a[mid]:
        return mid
    elif v < a[mid]:
        return do_binary_search(a, low, mid - 1, v)
    else:
        return do_binary_search(a, mid + 1, high, v)


def binary_search(a, x):
    left, right = 0, len(a) - 1
    return do_binary_search(a, left, right, x)


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
