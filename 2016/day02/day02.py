def part1(file_path, grid):
    return part2(file_path, grid)


def part2(file_path, grid):
    with open(file_path, 'r') as file:
        input_data = list(file.read().splitlines())

        x, y = 1, 1
        passcode = ""
        for number in input_data:
            for direction in number:
                if direction == "U":
                    y -= 1
                    if y < 0 or grid[y][x] == " ":
                        y += 1
                elif direction == "R":
                    x += 1
                    if x > len(grid[0]) - 1 or grid[y][x] == " ":
                        x -= 1
                elif direction == "D":
                    y += 1
                    if y > len(grid) - 1 or grid[y][x] == " ":
                        y -= 1
                elif direction == "L":
                    x -= 1
                    if x < 0 or grid[y][x] == " ":
                        x += 1

            passcode += grid[y][x]

        return passcode


print("Part 1: ", part1('input.txt', [["1", "2", "3"],
                                      ["4", "5", "6"],
                                      ["7", "8", "9"]]))
print("Part 2: ", part2('input.txt', [[" ", " ", "1", " ", " "],
                                      [" ", "2", "3", "4", " "],
                                      ["5", "6", "7", "8", "9"],
                                      [" ", "A", "B", "C", " "],
                                      [" ", " ", "D", " ", " "]]))
