# Uses python3
# 4 Problem: Collecting Signatures
import sys
from collections import namedtuple, OrderedDict

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    full_list = sorted(segments, key=lambda t: t[1])

    num_points = 0
    right_bounds = []
    while len(full_list) > 0:
            indexes = []
            num_points += 1
            min_right_bound_segment = min(full_list, key=lambda t: t[1])
            right_bounds.append(min_right_bound_segment.end)

            for key, item in enumerate(full_list):
                # If start is smaller or equal to minimum right bound remove from original list
                if (item.start <= min_right_bound_segment.end):
                    indexes.append(key)
                else:
                    break

            for index_to_remove in reversed(indexes):
                points.append(full_list.pop(index_to_remove))

    return num_points, right_bounds

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    n, points = optimal_points(segments)
    print(n)
    for p in points:
        print(p, end=' ')
