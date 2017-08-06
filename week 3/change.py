# Uses python3
# 1 Problem: Changing Money
import sys

denominators = [10, 5, 1]

def get_change(m):
    num_coins = 0

    for i in range(0, len(denominators)):
        cur_denom = denominators[i]
        num_coins += m // cur_denom
        m = m % cur_denom

    return num_coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
