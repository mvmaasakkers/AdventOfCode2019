def part1(file_path):
    with open(file_path, 'r') as file:
        input_data = [line for line in file.read().splitlines()]
        answer = 0

        for row in range(len(input_data)):
            for col in range(len(input_data[row])):

                if input_data[row][col] == 'X':
                    l = [
                        [(row, col), (row, col + 1), (row, col + 2), (row, col + 3)],
                        [(row, col), (row + 1, col + 1), (row + 2, col + 2), (row + 3, col + 3)],
                        [(row, col), (row + 1, col), (row + 2, col), (row + 3, col)],
                        [(row, col), (row + 1, col - 1), (row + 2, col - 2), (row + 3, col - 3)],
                        [(row, col), (row, col - 1), (row, col - 2), (row, col - 3)],
                        [(row, col), (row - 1, col - 1), (row - 2, col - 2), (row - 3, col - 3)],
                        [(row, col), (row - 1, col), (row - 2, col), (row - 3, col)],
                        [(row, col), (row - 1, col + 1), (row - 2, col + 2), (row - 3, col + 3)],
                    ]

                    for i in l:
                        skip = False
                        for n in i:
                            if n[0] < 0 or n[1] < 0 or n[0] > len(input_data)-1 or n[1] > len(input_data[0])-1:
                                skip = True


                        if not skip:
                            if ''.join([input_data[row][col] for row, col in i]) == 'XMAS':
                                answer += 1

        return answer


def part2(file_path):
    with open(file_path, 'r') as file:
        input_data = [line for line in file.read().splitlines()]
        answer = 0

        for row in range(len(input_data)):
            for col in range(len(input_data[row])):

                if input_data[row][col] == 'A':
                    found = 0
                    l = [
                        [(row-1, col-1), (row, col), (row + 1, col + 1)],
                        [(row-1, col+1), (row, col), (row + 1, col - 1)],
                        [(row + 1, col - 1), (row, col), (row - 1, col + 1)],
                        [(row + 1, col + 1), (row, col), (row - 1, col - 1)],
                    ]

                    for i in l:
                        skip = False
                        for n in i:
                            if n[0] < 0 or n[1] < 0 or n[0] > len(input_data) - 1 or n[1] > len(input_data[0]) - 1:
                                skip = True

                        if not skip:
                            if ''.join([input_data[row][col] for row, col in i]) == 'MAS':
                                found += 1
                    if found >= 2:
                        answer += 1

        return answer


print("Part 1: ", part1('input.txt'))
print("Part 2: ", part2('input.txt'))
