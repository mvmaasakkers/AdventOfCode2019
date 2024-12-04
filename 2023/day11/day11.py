from helpers import transpose


def part1(file_path):
    with open(file_path, 'r') as file:
        input_data = [line for line in file.read().splitlines()]

        return expand(input_data, 2)


def expand(input_data, multiplier):
    answer = 0

    empty_rows = [y for y in range(len(input_data)) if not '#' in input_data[y]]
    transposed = transpose(input_data)
    empty_columns = [x for x in range(len(transposed)) if not '#' in transposed[x]]

    locations = [(y, x) for y in range(len(input_data)) for x in range(len(input_data[y])) if input_data[y][x] == '#']

    for start in range(len(locations)):
        for end in range(len(locations)):
            if locations[start] == locations[end]:
                continue

            col_adds = sum([multiplier - 1 for col in empty_columns if
                            min(locations[start][1], locations[end][1]) <= col <= max(locations[start][1],
                                                                                      locations[end][1])])
            row_adds = sum([multiplier - 1 for row in empty_rows if
                            min(locations[start][0], locations[end][0]) <= row <= max(locations[start][0],
                                                                                      locations[end][0])])

            answer += abs(locations[end][0] - locations[start][0]) + abs(
                locations[end][1] - locations[start][1]) + row_adds + col_adds
    return int(answer / 2)


def part2(file_path):
    with open(file_path, 'r') as file:
        input_data = [line for line in file.read().splitlines()]

        return expand(input_data, 1000000)


print("Part 1: ", part1('input.txt'))
print("Part 2: ", part2('input.txt'))
