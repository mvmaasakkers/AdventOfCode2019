import math
import re


def part1(file_path):
    with open(file_path, 'r') as file:
        input_data = [line for line in file.read().splitlines()]

        times = [int(n) for n in re.split(r'\s+', input_data[0][len("Time: "):].strip())]
        distances = [int(n) for n in re.split(r'\s+', input_data[1][len("Distance: "):].strip())]
        races = [{'time': times[i], 'distance': distances[i]} for i in range(len(times))]

        possibilities = [
            sum([1 for time in range(0, race['time'] + 1) if time * (race['time'] - time) > race['distance']]) for race
            in races]

        return math.prod(possibilities)


def part2(file_path):
    with open(file_path, 'r') as file:
        input_data = [line for line in file.read().splitlines()]

        total_time = int(''.join([n for n in re.split(r'\s+', input_data[0][len("Time: "):].strip())]))
        total_distance = int(''.join([n for n in re.split(r'\s+', input_data[1][len("Distance: "):].strip())]))

        return sum([1 for time in range(0, total_time + 1) if time * (total_time - time) > total_distance])


print("Part 1: ", part1('input.txt'))
print("Part 2: ", part2('input.txt'))
