def determine_direction(dir, turn):
    if dir == 'N':
        if turn == 'R':
            return 'E'
        if turn == 'L':
            return 'W'
    elif dir == 'E':
        if turn == 'R':
            return 'S'
        if turn == 'L':
            return 'N'
    elif dir == 'S':
        if turn == 'R':
            return 'W'
        if turn == 'L':
            return 'E'
    elif dir == 'W':
        if turn == 'R':
            return 'N'
        if turn == 'L':
            return 'S'


def part1(file_path):
    with open(file_path, 'r') as file:
        input_data = list(file.read().split(", "))

        dir = 'N'
        pos = (0, 0)  # (x, y)

        for direction in input_data:
            dir = determine_direction(dir, direction[0])
            if dir == 'N':
                pos = (pos[0], pos[1] + int(direction[1:]))
            elif dir == 'E':
                pos = (pos[0] + int(direction[1:]), pos[1])
            elif dir == 'S':
                pos = (pos[0], pos[1] - int(direction[1:]))
            elif dir == 'W':
                pos = (pos[0] - int(direction[1:]), pos[1])

        return abs(pos[0]) + abs(pos[1])


def part2(file_path):
    with open(file_path, 'r') as file:
        input_data = list(file.read().split(", "))

        dir = 'N'
        x, y = 0, 0
        visited_positions = set()
        visited_positions.add((x, y))
        for direction in input_data:
            dir = determine_direction(dir, direction[0])
            amount = int(direction[1:])
            for _ in range(amount):
                if dir == 'N':
                    y += 1
                elif dir == 'E':
                    x += 1
                elif dir == 'S':
                    y -= 1
                elif dir == 'W':
                    x -= 1

                if (x, y) in visited_positions:
                    return abs(x) + abs(y)
                else:
                    visited_positions.add((x, y))

        return 0


print("Part 1: ", part1('input.txt'))
print("Part 2: ", part2('input.txt'))
