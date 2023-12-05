import re


def part1(file_path):
    with open(file_path, 'r') as file:
        line = file.read()

        markerRegex = re.compile(r'\(\d+x\d+\)')
        found = len(markerRegex.findall(line))
        print(found)
        pos = 0
        for _ in range(found):
            marker = markerRegex.search(line)
            x, y = [int(n) for n in line[marker.start() + 1:marker.end() - 1].split("x")]
            print(line)
            repeater = line[marker.end():marker.end() + x]

            line = line[:marker.start()] + ''.join(list([repeater for _ in range(y)])) + line[marker.end()+x:]

        print(line)

        return len(line)


def part2(file_path):
    with open(file_path, 'r') as file:
        input_data = [line for line in file.read().splitlines()]
        answer = 0

        for line in input_data:
            print(line)

        return answer


print("Part 1: ", part1('input_test.txt'))
print("Part 2: ", part2('input_test.txt'))
