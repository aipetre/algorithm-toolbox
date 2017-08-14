# Uses python3
# 2 Majority Element
import sys

def get_frequency(a, left, right, el1):
    count = 0
    for i in range(left, right + 1):
        if a[i] == el1:
            count +=1

    return count


def get_majority_element(a, left, right):
    if left > right:
        return -1

    if left == right:             
        return a[left]
    
    mid = ((right - left) // 2) + left
    lower = get_majority_element(a, left, mid)
    upper = get_majority_element(a, mid + 1, right)
    
    majority_count = (right - left + 1) // 2

    if lower == -1 and upper != -1:
        num = get_frequency(a, left, right, upper)
        if num > majority_count:
            return upper
        else:
            return -1
    elif upper == -1 and lower != -1:
        num = get_frequency(a, left, right, lower)
        if num > majority_count:
            return lower
        else:
            return -1
    elif lower != -1 and upper != -1:
        lower_num = get_frequency(a, left, right, lower)
        upper_num = get_frequency(a, left, right, upper)

        if lower_num > majority_count:
            return lower
        elif upper_num > majority_count:
            return upper
        else:
            return -1

    return -1


def get_majoirty_element_fast(a):
    pass

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, len(a) - 1) != -1:
        print(1)
    else:
        print(0)
