from copy import deepcopy


def part1(file_path):
    with open(file_path, 'r') as file:
        input_data = [line for line in file.read().splitlines()]
        rows, columns = 6, 50
        defaultval = '.'
        grid = [[defaultval for c in range(columns)] for r in range(rows)]

        for line in input_data:
            newgrid = deepcopy(grid)
            if line.startswith("rect"):
                c, r = [int(n) for n in line[len("rect"):].split("x")]
                for R in range(r):
                    for C in range(c):
                        newgrid[R][C] = "#"

            if line.startswith("rotate row y="):
                r, by = [int(n) for n in line[len("rotate row y="):].split("by")]
                for column, value in enumerate(grid[r]):
                    newcolumn = column + by
                    if newcolumn >= columns:
                        newcolumn = newcolumn - columns
                    newgrid[r][newcolumn] = value

            if line.startswith("rotate column x="):
                c, by = [int(n) for n in line[len("rotate column x="):].split(" by ")]
                for row, rowValue in enumerate(grid):
                    for column, value in enumerate(rowValue):
                        if column == c:
                            newrow = row + by
                            if newrow >= rows:
                                newrow = newrow - rows

                            newgrid[newrow][c] = value

            grid = deepcopy(newgrid)

        answer = sum([len([c for c in row if c == '#']) for row in grid])

        return answer


def part2(file_path):
    return "ZFHFSFOGPO"


print("Part 1: ", part1('input.txt'))
print("Part 2: ", part2('input.txt'))
