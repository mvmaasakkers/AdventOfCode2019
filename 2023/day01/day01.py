def part1(file_path):
    with open(file_path, 'r') as file:
        input_data = list(file.read().splitlines())

        return sum(int(f"{num[0]}{num[-1]}")
                   for num in (list(filter(str.isdigit, line))
                               for line in input_data
                               ))


def part2(file_path):
    with open(file_path, 'r') as file:
        input_data = list(file.read().splitlines())
        digits = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
            "0": "0",
            "1": "1",
            "2": "2",
            "3": "3",
            "4": "4",
            "5": "5",
            "6": "6",
            "7": "7",
            "8": "8",
            "9": "9",
        }
        return sum(int(f"{num[0]}{num[-1]}")
                   for line in input_data
                   for num in ([digit for i in range(len(line))
                                for string, digit in digits.items()
                                if line[i:].startswith(string)],))


print("Part 1: ", part1('input.txt'))
print("Part 2: ", part2('input.txt'))
