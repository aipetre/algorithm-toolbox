# Uses python3
# 5 Problem: Maximizing the Number of Prize Places in a Competition
import sys

def get_summand(k, l):
    if (k <= 2 * l):
        return k

    return l

def optimal_summands2(n):
    summands = []
    index = 1
    
    while n != 0:
        summand = get_summand(n, index)
        summands.append(summand)
        n = n - summand
        index = index + 1

    return summands
        

def optimal_summands(n):
    summands = []
    leftOver = 0

    while n > 0:
        for i in range(1, n+1):
            if n-i >= 0:
                summands.append(i)
                n -= i
            else:
                leftOver = n
                n = -1
                break

    if leftOver > 0:
        for i in reversed(range(0, len(summands))):
            summands[i] += 1
            leftOver -= 1
            if leftOver == 0: break

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands2(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
