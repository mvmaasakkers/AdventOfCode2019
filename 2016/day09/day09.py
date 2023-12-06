import re


def part1(file_path):
    with open(file_path, 'r') as file:
        line = file.read()

        marker_regex = re.compile(r'\(\d+x\d+\)')
        found = len(marker_regex.findall(line))
        start_pos = 0
        end_pos = 0
        pos = 0
        count = 0
        running = True
        while running:
            ch = line[pos]
            if ch == '(':
                start_pos = pos
                pos += 1
            elif ch == ')':
                end_pos = pos
                x, y = [int(n) for n in line[start_pos + 1:end_pos].split("x")]
                repeater = line[end_pos + 1:end_pos + x + 1]
                replace_with = ''.join(list([repeater for _ in range(y)]))
                line = line[:start_pos] + ''.join(list([repeater for _ in range(y)])) + line[end_pos + x + 1:]
                pos = start_pos + len(replace_with)
            else:
                pos += 1

            count += 1

            if pos >= len(line):
                running = False

        return len(line)


def getLength(data):
    length = pos = 0
    while pos < len(data):
        if data[pos] == '(':
            end_pos = data.find(')', pos)
            (repeater, repeat) = [int(n) for n in data[pos + 1:end_pos].split('x')]
            length += getLength(data[end_pos + 1:end_pos + repeater + 1]) * repeat
            pos = end_pos + repeater
        else:
            length += 1
        pos += 1
    return length


def part2(file_path):
    with open(file_path, 'r') as file:
        line = file.read().strip()

        return getLength(line)
        # I HATE RECURSION!
        #
        #
        # marker_regex = re.compile(r'\(\d+x\d+\)')
        # found = len(marker_regex.findall(line))
        # start_pos = 0
        # end_pos = 0
        # pos = 0
        # count = 0
        # running = True
        # while running:
        #     ch = line[pos]
        #     if ch == '(':
        #         start_pos = pos
        #         pos += 1
        #     elif ch == ')':
        #         end_pos = pos
        #         x, y = [int(n) for n in line[start_pos + 1:end_pos].split("x")]
        #         repeater = line[end_pos + 1:end_pos + x + 1]
        #         replace_with = ''.join(list([repeater for _ in range(y)]))
        #         line = line[:start_pos] + ''.join(list([repeater for _ in range(y)])) + line[end_pos + x + 1:]
        #         pos = start_pos
        #     else:
        #         pos += 1
        #
        #     count += 1
        #
        #     if pos >= len(line):
        #         running = False
        #
        # print(line)
        # return len(line)


print("Part 1: ", part1('input.txt'))
print("Part 2: ", part2('input.txt'))
