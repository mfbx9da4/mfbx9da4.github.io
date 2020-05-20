"""
"""


def int_as_array(num): return list(map(int, [y for y in str(num)]))


def array_as_int(arr): return int(''.join(map(str, arr)))


def read_int(): return int(input())


def read_array(): return list(map(int, input().split(' ')))


def array_to_string(arr, sep=' '): return sep.join(map(str, arr))


def matrix_to_string(arr, sep=' '): return '[\n' + '\n'.join(
    [sep.join(map(str, row)) for row in arr]) + '\n]'


def read(): input()


# 3 30
# 4 50
# 5 60

# 5 + 4 => 9 
# 8 is capacity
# create fictitious bags up to size C
# 1 2 3  4  5  6  7  8
# 0 0 30 50 60
# 4 => or 3 + 1
# 5 => (5, 4 + 1, 3 + 2, 2 + 3, 1 + 4)
#      (60, 4 + 1, 3 + 2)
# for each weight in weights:
#   3, 4, 5
#   capacities[w] = values[i]
#   for c in 0..w:
#       capacities[w] = max(capacities[w], capacities[w - c] + capacities[c])

def solve(capacity, weights, values):
    capacities = [0 for i in range(capacity)]
    for c in range(capacity):
        for i in range(len(weights)):
            w = weights[i]
            v = values[i]
            delta = c - w
            if delta < 0: break
            capacities[c] = max(capacities[c], capacities[delta] + v)
        print(capacities)
    return capacities[-1]



num_items, capacity = read_array()
weights = []
values = []
for x in range(num_items):
    w, v = read_array()
    weights.append(w)
    values.append(v)
print(solve(capacity, weights, values))
