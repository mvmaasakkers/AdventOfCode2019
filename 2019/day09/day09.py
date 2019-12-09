import sys
import os
sys.path.append(os.path.abspath("2019"))
import intcode

def parse_data(f):
    return list(map(int, f.split(",")))

def get_data(file):
    with open(file, 'r') as f:
        data = parse_data(f.read())
    return data

program = get_data('2019/day09/input.txt')

print('Part 1:', intcode.RUN(program, [1]))
print('Part 1:', intcode.RUN(program, [2]))