def part1(file_path):
    with open(file_path, 'r') as file:
        input_data = [line for line in file.read().splitlines()]
        answer = 0

        conv = {
            'A': 14,
            'K': 13,
            'Q': 12,
            'J': 11,
            'T': 10,
            '9': 9,
            '8': 8,
            '7': 7,
            '6': 6,
            '5': 5,
            '4': 4,
            '3': 3,
            '2': 2,
            '1': 1,
        }

        conv_swap = {v: k for k, v in conv.items()}

        

        for line in input_data:
            hand = [conv[c] for c in line.split(' ')[0]]
            bid = int(line.split(' ')[1])

            hand_sorted = sorted(hand, reverse=True)

            count_cards = {i: hand_sorted.count(i) for i in conv_swap}

            t5oak = len([1 for n in count_cards if count_cards[n] == 5]) > 0
            t4oak = len([1 for n in count_cards if count_cards[n] == 4]) > 0
            tfullhouse = len([1 for n in count_cards if count_cards[n] == 3]) > 0 and len([1 for n in count_cards if count_cards[n] == 2]) > 0
            t3oak = len([1 for n in count_cards if count_cards[n] == 3]) > 0
            tp = len([1 for n in count_cards if count_cards[n] == 2]) == 2
            op = len([1 for n in count_cards if count_cards[n] == 2]) == 1


            print(line, hand, hand_sorted, bid, t5oak, t4oak, tfullhouse, t3oak, tp, op)



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
