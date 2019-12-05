from itertools import cycle
import math

modules = [];
with open('2019/day01/input.txt', 'r') as f:
    for line in f:
        if line != '':
            modules.append(int(line));

part1 = 0
part2 = 0

for module in modules:
    fuel = math.floor(module / 3) - 2
    part1 += fuel
    mass = fuel
    while True:
        extraFuel = math.floor(mass / 3) - 2
        if extraFuel > 0:
            fuel += extraFuel
        if extraFuel <= 0:
            break
        mass = extraFuel
    part2 += fuel

print("Part 1:", part1);
print("Part 2:", part2);