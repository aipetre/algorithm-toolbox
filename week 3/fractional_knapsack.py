# Uses python3
# 2 Problem: Maximizing the Value of a Loot
import sys
from collections import OrderedDict

def sort_items (weights, values):
    units = {}
    for i in range(0, len(weights)):
        units[i] = values[i] / weights[i] 

    sorted_units = OrderedDict(sorted(units.items(), key=lambda t: t[1], reverse=True))

    sorted_weights = []
    sorted_values = []
    for key, _ in sorted_units.items():
        sorted_weights.append(weights[key])
        sorted_values.append(values[key])

    return sorted_weights, sorted_values

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here

    s_weights, s_values = sort_items(weights, values)

    for i in range(0, len(s_weights)):
        if capacity == 0:
            break
        
        # weight to take from item
        weight_to_add = min(s_weights[i], capacity)
        value_per_unit = s_values[i] / s_weights[i]
        value += value_per_unit * weight_to_add
        capacity -= weight_to_add

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
