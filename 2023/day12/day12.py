def part1(file_path):
    with open(file_path, 'r') as file:
        input_data = [line for line in file.read().splitlines()]
        answer = 0

        for line in input_data:
            springs,r  = line.split(' ')
            rec = [int(i) for i in r.split(',')]
            # springs = l.split(',')

            print(springs, rec)

        return answer


def part2(file_path):
    with open(file_path, 'r') as file:
        input_data = [line for line in file.read().splitlines()]
        answer = 0

        for line in input_data:
            print(line)

        return answer


print("Part 1: ", part1('input_test.txt'))
# print("Part 2: ", part2('input_test.txt'))
