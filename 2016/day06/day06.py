import helpers


def part1(file_path):
    with open(file_path, 'r') as file:
        input_data = helpers.transpose([[c for c in line] for line in file.read().splitlines()])
        chars = 'abcdefghijklmnopqrstuvwxyz'

        pw = ""
        for column in input_data:
            found = {}
            for c in chars:
                found[c] = len([n for n in column if n == c])

            pw += [key for key, _ in sorted(found.items(), key=lambda x: x[1], reverse=True)][0]

        return pw


def part2(file_path):
    with open(file_path, 'r') as file:
        input_data = helpers.transpose([[c for c in line] for line in file.read().splitlines()])
        chars = 'abcdefghijklmnopqrstuvwxyz'

        pw = ""
        for column in input_data:
            found = {}
            for c in chars:
                found[c] = len([n for n in column if n == c])

            pw += [key for key, value in sorted(found.items(), key=lambda x: x[1]) if value > 0][0]

        return pw


print("Part 1: ", part1('input.txt'))
print("Part 2: ", part2('input.txt'))
