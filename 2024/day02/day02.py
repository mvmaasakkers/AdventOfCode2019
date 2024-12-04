def part1(file_path):
    with open(file_path, 'r') as file:
        reports = [[int(i) for i in line.split(' ')] for line in file.read().splitlines()]
        answer = 0

        for report in reports:
            direction = ''
            if report[0] > report[1]:
                direction = 'down'
            elif report[0] < report[1]:
                direction = 'up'
            else:
                direction = ''

            checks = []

            for i, level in enumerate(report):
                if i + 1 >= len(report):
                    continue

                if direction == 'up':
                    if report[i] > report[i + 1]:
                        break

                if direction == 'down':
                    if report[i] < report[i + 1]:
                        break

                if abs(report[i] - report[i + 1]) < 1 or abs(report[i] - report[i + 1]) > 3:
                    break

                checks.append(level)

            if len(checks) == len(report) - 1:
                answer += 1
        return answer


def is_safe(row):
    inc = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    if set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3}:
        return True
    return False


def part2(file_path):
    with open(file_path, 'r') as file:
        reports = [[int(i) for i in line.split(' ')] for line in file.read().splitlines()]

        answer = sum([any([is_safe(row[:i] + row[i + 1:]) for i in range(len(row))]) for row in reports])

        return answer


print("Part 1: ", part1('input.txt'))
print("Part 2: ", part2('input.txt'))
