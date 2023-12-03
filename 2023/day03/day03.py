from collections import defaultdict


def numbers(max_y, max_x, y, x1, x2):
    number_list = set()
    for x in range(x1, x2):
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if (di, dj) == (0, 0):
                    continue
                nbri, nbrj = y + di, x + dj
                if 0 <= nbri < max_y and 0 <= nbrj < max_x:
                    number_list.add((nbri, nbrj))
    return number_list


def is_symbol(char):
    return (not char.isdigit()) and char != '.'


def part1(file_path):
    with open(file_path, 'r') as file:
        input_data = list(file.read().splitlines())
        grid = [line for line in input_data]

        max_y = len(grid)
        max_x = len(grid[0])

        total = 0
        for y in range(max_y):
            x = 0
            while x < max_x:
                if not grid[y][x].isdigit():
                    x += 1
                    continue
                j2 = x + 1
                while j2 < max_x and grid[y][j2].isdigit():
                    j2 += 1
                if any(is_symbol(grid[nbri][nbrj]) for nbri, nbrj in numbers(max_y, max_x, y, x, j2)):
                    num = int(grid[y][x:j2])
                    total += num
                x = j2

        return total


def part2(file_path):
    with open(file_path, 'r') as file:
        input_data = list(file.read().splitlines())
        grid = [line for line in input_data]

        max_y = len(grid)
        max_x = len(grid[0])

        total = 0
        table = defaultdict(list)
        for y in range(max_y):
            x = 0
            while x < max_x:
                if not grid[y][x].isdigit():
                    x += 1
                    continue
                j2 = x + 1
                while j2 < max_x and grid[y][j2].isdigit():
                    j2 += 1
                if any(is_symbol(grid[nbri][nbrj]) for nbri, nbrj in numbers(max_y, max_x, y, x, j2)):
                    num = int(grid[y][x:j2])
                    total += num
                    for nbri, nbrj in numbers(max_y, max_x, y, x, j2):
                        if grid[nbri][nbrj] == '*':
                            table[(nbri, nbrj)].append(num)
                x = j2

        gear_ratio_sum = 0
        for v in table.values():
            if len(v) == 2:
                gear_ratio_sum += (v[0] * v[1])

        return gear_ratio_sum


print("Part 1: ", part1('input.txt'))
print("Part 2: ", part2('input.txt'))
