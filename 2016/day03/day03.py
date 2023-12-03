import re


def part1(file_path):
    with open(file_path, 'r') as file:
        numberList = [[int(n) for n in re.split(r"\s+", line.strip())] for line in list(file.read().splitlines())]

        return sum(1 for n in numberList if n[0] + n[1] > n[2] and n[1] + n[2] > n[0] and n[0] + n[2] > n[1])

def part2(file_path):
    with open(file_path, 'r') as file:
        input_data = list(file.read().splitlines())

        return 0


print("Part 1: ", part1('input.txt'))
print("Part 2: ", part2('input_test.txt'))
