import re

import numpy


def split_list(lst, size):
    return [lst[i:i + size] for i in range(0, len(lst), size)]


def part1(file_path):
    with open(file_path, 'r') as file:
        numberList = [[int(n) for n in re.split(r"\s+", line.strip())] for line in list(file.read().splitlines())]

        return sum(1 for n in numberList if n[0] + n[1] > n[2] and n[1] + n[2] > n[0] and n[0] + n[2] > n[1])


def part2(file_path):
    with open(file_path, 'r') as file:
        numbers = [[int(n) for n in re.split(r"\s+", line.strip())] for line in list(file.read().splitlines())]
        numbers = numpy.transpose(numbers)

        possible_triangles = split_list(numbers[0], 3) + split_list(numbers[1], 3) + split_list(numbers[2], 3)

        return sum(1 for n in possible_triangles if n[0] + n[1] > n[2] and n[1] + n[2] > n[0] and n[0] + n[2] > n[1])


print("Part 1: ", part1('input.txt'))
print("Part 2: ", part2('input.txt'))
