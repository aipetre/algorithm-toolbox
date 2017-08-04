# Uses python3
# 1 Problem: Small Fibonacci Number

"""
Calculates n Fibonnaci number
Note: We don't need a list, we could have just used 2 variable
"""
def fib_table(n):
    if (n <= 1):
        return n

    table = [0 for i in range(0, n+1)]
    table[0] = 0
    table[1] = 1
    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]

    return table[n]

n = int(input())
print(fib_table(n))
