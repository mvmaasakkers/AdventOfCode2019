import math
import re
from typing import List, Dict


def part1(file_path):
    with open(file_path, 'r') as file:
        input_data = [line for line in file.read().splitlines()]

        instructions = [n for n in input_data[0]]
        nodes = {}

        for line in input_data[2:]:
            node, rawdirections = [n for n in line.split(' = ')]
            left, right = rawdirections[1:-1].split(", ")

            nodes[node] = {'left': left, 'right': right}

        node = 'AAA'
        i = 0
        steps = 0
        while node != 'ZZZ':
            instruction = instructions[i]
            if instruction == 'R':
                node = nodes[node]['right']
            elif instruction == 'L':
                node = nodes[node]['left']

            i += 1
            if i == len(instructions):
                i = 0

            steps += 1

        return steps

START = "AAA"
END = "ZZZ"
LEFT = "L"
RIGHT = "R"

def part2(file_path):
    with open(file_path, 'r') as file:
        lines = [line for line in file.read().splitlines()]
        directions = lines[0]
        n = len(directions)

        nodes = {}
        for line in lines[2:]:
            start, left, right = re.findall("([1-9A-Z]+)", line)
            nodes[start] = (left, right)

        positions = []
        for node in nodes:
            if node[-1] == "A":
                positions.append(node)

        cl = [cycle_length(p, directions, nodes) for p in positions]
        for c in cl:
            assert c % n == 0

        lcm = math.lcm(*cl)
        return lcm

def cycle_length(start: str, directions: str, nodes: Dict) -> int:
    position = start

    steps = 0
    while position[-1] != "Z":
        direction = directions[steps % len(directions)]
        if direction == LEFT:
            position = nodes[position][0]
        else:
            position = nodes[position][1]
        steps += 1

    return steps


print("Part 1: ", part1('input.txt'))
print("Part 2: ", part2('input.txt'))
