import re


def abba(x):
    return any(a == d and b == c and a != b for a, b, c, d in zip(x, x[1:], x[2:], x[3:]))


def part1(file_path):
    with open(file_path, 'r') as file:
        input_data = [line for line in file.read().splitlines()]

        lines = [re.split(r'\[([^\]]+)\]', line) for line in input_data]
        parts = [(' '.join(p[::2]), ' '.join(p[1::2])) for p in lines]

        answer = sum(abba(sn) and not (abba(hn)) for sn, hn in parts)

        return answer


def part2(file_path):
    with open(file_path, 'r') as file:
        input_data = [line for line in file.read().splitlines()]

        lines = [re.split(r'\[([^\]]+)\]', line) for line in input_data]
        parts = [(' '.join(p[::2]), ' '.join(p[1::2])) for p in lines]

        answer = sum(
            any(a == c and a != b and b + a + b in hn for a, b, c in zip(sn, sn[1:], sn[2:])) for sn, hn in parts)

        return answer


print("Part 1: ", part1('input.txt'))
print("Part 2: ", part2('input.txt'))
