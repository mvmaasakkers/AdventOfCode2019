def part1(file_path):
    with open(file_path, 'r') as file:
        input_data = list(file.read().splitlines())

        total = []

        maxRed, maxGreen, maxBlue = 12, 13, 14
        for line in input_data:
            game, turns = line.split(": ")
            game = int(game.split(" ")[1])

            possible = True
            for turn in turns.split("; "):
                for color in turn.split(", "):
                    amount, color = color.split(" ")
                    amount = int(amount)
                    if color == "red" and amount > maxRed:
                        possible = False
                    if color == "green" and amount > maxGreen:
                        possible = False
                    if color == "blue" and amount > maxBlue:
                        possible = False

            if possible:
                total.append(game)

        return sum(total)


def part2(file_path):
    with open(file_path, 'r') as file:
        input_data = list(file.read().splitlines())

        total = []

        for line in input_data:
            game, turns = line.split(": ")

            minRed, minGreen, minBlue = 0, 0, 0
            for turn in turns.split("; "):
                for color in turn.split(", "):
                    amount, color = color.split(" ")
                    amount = int(amount)
                    if color == "red" and amount > minRed:
                        minRed = amount
                    if color == "green" and amount > minGreen:
                        minGreen = amount
                    if color == "blue" and amount > minBlue:
                        minBlue = amount
            total.append(minRed * minGreen * minBlue)
        return sum(total)


print("Part 1: ", part1('input.txt'))
print("Part 2: ", part2('input.txt'))
