import re

def part1(file_path):
    with open(file_path, 'r') as file:
        input_data = list(file.read().splitlines())
        total = 0
        for line in input_data:
            parts = line.split(": ")
            numbers_parts = parts[1].split(" | ")

            winning_numbers = [int(n) for n in numbers_parts[0].split()]
            own_numbers = [int(n) for n in numbers_parts[1].split()]

            intersected = [value for value in own_numbers if value in winning_numbers]

            points = 0
            if len(intersected) > 0:
                points = 1 << len(intersected) - 1

            total += points

        return total


def part2(file_path):
    with open(file_path, 'r') as file:
        input_data = list(file.read().splitlines())

        cards = {}
        for line in input_data:
            parts = line.split(": ")
            card_number = int(re.split(r"\s+", parts[0])[1])
            numbers_parts = parts[1].split(" | ")

            cards[card_number] = cards.get(card_number, 0) + 1

            winning_numbers = [int(n) for n in numbers_parts[0].split()]
            own_numbers = [int(n) for n in numbers_parts[1].split()]

            intersected = [value for value in own_numbers if value in winning_numbers]

            for n in range(card_number + 1, card_number + len(intersected) + 1):
                cards[n] = cards.get(n, 0) + cards[card_number]

        return sum(cards.values())


print("Part 1: ", part1('input.txt'))
print("Part 2: ", part2('input.txt'))
