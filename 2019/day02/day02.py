import sys
import os

sys.path.append(os.path.abspath("2019"))
import intcode

def get_data(file):
    with open(file, 'r') as f:
        data = list(map(int, f.read().split(',')))
    return data


origLocations = get_data('2019/day02/input.txt')


def part_one(locs, noun, verb):
    loc = list.copy(locs)
    loc[1] = noun
    loc[2] = verb

    return intcode.RUN(loc, [], isFeedback=True, returnLoc0=True)


def part_two(origLocations, output):
    for i in range(1, 99):
        for j in range(1, 99):
            if part_one(origLocations, i, j) == output:
                return (100 * i) + j


# Part 1: 5866714
# Part 2: 5208
print("Part 1:", part_one(origLocations, 12, 2))
print("Part 2:", part_two(origLocations, 19690720))
