import re


def part1(file_path):
    with open(file_path, 'r') as file:
        input_data = [line for line in file.read().splitlines()]

        answer = 0

        # answer = sum([int(match[0]) * int(match[1]) for match in re.findall(r"mul\((\d+),(\d+)\)", input_data)])
        for line in input_data:
            answer += sum([int(match[0]) * int(match[1]) for match in re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", line)])
        # print(matches)
        # for line in input_data:
        #     print(line)
        #
        return answer


def part2(file_path):
    with open(file_path, 'r') as file:
        input_data = ''.join([line for line in file.read().splitlines()])

        line = input_data

        while line.find("don't()") > -1:
            start = line.find("don't()")
            end = line.find("do()", start)
            line = line[0:start] + line[end+4:]

        answer = sum(
            [int(match[0]) * int(match[1]) for match in re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", line)])

        return answer


print("Part 1: ", part1('input.txt'))
print("Part 2: ", part2('input.txt'))
