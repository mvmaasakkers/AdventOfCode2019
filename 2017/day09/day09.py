def part1(file_path):
    with open(file_path, 'r') as file:
        input_data = file.read().splitlines()[0]
        answer = 0

        depth = 0

        in_garbage = False
        ignore_next = False
        for ch, char in enumerate(input_data):
            if ignore_next:
                ignore_next = False
                continue

            if in_garbage and char == '!':
                ignore_next = True
                continue

            if in_garbage and char == '>':
                in_garbage = False
                continue

            if not in_garbage and char == '<':
                in_garbage = True
                continue

            if not in_garbage and char == '{':
                depth += 1
                answer += depth
                continue

            if not in_garbage and char == '}':
                depth -= 1
                continue

            # print(ch, char)

        return answer


def part2(file_path):
    with open(file_path, 'r') as file:
        input_data = file.read().splitlines()[0]
        answer = 0

        in_garbage = False
        ignore_next = False
        for ch, char in enumerate(input_data):
            if ignore_next:
                ignore_next = False
                continue

            if in_garbage and char == '!':
                ignore_next = True
                continue

            if in_garbage and char == '>':
                in_garbage = False
                continue

            if not in_garbage and char == '<':
                in_garbage = True
                continue

            if in_garbage:
                answer += 1

        return answer


print("Part 1: ", part1('input.txt'))
print("Part 2: ", part2('input.txt'))
