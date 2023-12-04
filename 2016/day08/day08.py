import helpers


def part1(file_path):
    with open(file_path, 'r') as file:
        input_data = [line for line in file.read().splitlines()]
        rows, columns = 3, 7
        grid = [[c for c in range(columns)] for r in range(rows)]


        helpers.print_grid(grid)

        answer = 0

        for line in input_data:
            newgrid = grid
            if line.startswith("rect"):
                c, r = [int(n) for n in line[len("rect"):].split("x")]
                for R in range(r):
                    for C in range(c):
                        newgrid[R][C] = "#"

            if line.startswith("rotate row y="):
                r, n = [int(n) for n in line[len("rotate row y="):].split("by")]
                # for c in grid[r]:
                #     print(c)
                print(r, n)

            if line.startswith("rotate column x="):
                c, n = [int(n) for n in line[len("rotate column x="):].split(" by ")]
                for row in grid:
                    for column, value in enumerate(row):
                        print(column)
                        if column == c:
                            print(c)
                print(r, n)

                print(c, n)

            print(line)

            grid = newgrid
            helpers.print_grid(grid)

        return answer


def part2(file_path):
    with open(file_path, 'r') as file:
        input_data = [line for line in file.read().splitlines()]
        answer = 0

        for line in input_data:
            print(line)

        return answer


print("Part 1: ", part1('input_test.txt'))
print("Part 2: ", part2('input_test.txt'))
