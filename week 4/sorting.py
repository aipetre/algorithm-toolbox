# Uses python3
<<<<<<< HEAD
# 3 Problem: Improving Quick Sort
=======
>>>>>>> 78dc913718eab8ea8409e1c79db1959582bca1b4
import sys
import random

def partition3(a, l, r):
<<<<<<< HEAD
    x = a[l]
    j = l
    k = r

    for i in range(l + 1, r + 1):
        if a[i] < x:
            j += 1
            a[i], a[j] = a[j], a[i]

        if a[i] > x:           
            a[i], a[k] = a[k], a[i]
            k -= 1

    a[l], a[j] = a[j], a[l]
    a[j], a[k] = a[k], a[j]

    return j, k

def partition2(a, l, r):
    x = a[l]
    j = l
=======
    #write your code here
    pass

def partition2(a, l, r):
    x = a[l]
    j = l;
>>>>>>> 78dc913718eab8ea8409e1c79db1959582bca1b4
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
<<<<<<< HEAD
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2 + 1, r)

    # partition 2
    # m = partition2(a, l, r)
    # randomized_quick_sort(a, l, m - 1)
    # randomized_quick_sort(a, m + 1, r)
=======
    m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m + 1, r);
>>>>>>> 78dc913718eab8ea8409e1c79db1959582bca1b4


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')