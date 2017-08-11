#Uses python3
# 6 Advanced Problem: Maximizing Your Salary

import sys

def is_greater_or_equal(checkDigit, maxDigit):
    xy = int(checkDigit + maxDigit)
    yz = int(maxDigit + checkDigit)

    return True if xy > yz else False    

def largest_number(numbers):
    #write your code here
    res = ""
    while len(numbers):
        maxD = '0'
        for x in numbers:
            if (is_greater_or_equal(x, maxD)):
                maxD = x

        res += str(maxD)
        numbers.remove( str(maxD))        
    return res

if __name__ == '__main__':
    #print(is_greater_or_equal(103, 12))
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
