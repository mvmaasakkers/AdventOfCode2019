import sys
import os

sys.path.append(os.path.abspath("2019"))
import intcode


def get_data(file):
    with open(file, 'r') as f:
        data = list(map(int, f.read().split(",")))
    return data


data = get_data("2019/day05/input.txt")

print("Part 1:", intcode.RUN(list.copy(data), [1]))
print("Part 2:", intcode.RUN(list.copy(data), [5]))
