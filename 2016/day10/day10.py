import re


def part1(file_path):
    with open(file_path, 'r') as file:
        input_data = [line for line in file.read().splitlines()]
        answer = 0

        bots = {}
        outputs = {}

        bot_lines = [line[len('value '):] for line in input_data if line.startswith('value ')]
        op_lines = [line for line in input_data if line.startswith('bot ')]

        for line in bot_lines:
            value, bot = [int(n) for n in line.split(' goes to bot ')]
            if bot not in bots:
                bots[bot] = []
            bots[bot].append(value)

        # for bot in range(max(bots.keys())+10):
        #     if bot not in bots:
        #         bots[bot] = []

        # print(max(bots.keys())+1)
        for line in op_lines:
            parts = line.split(' ')
            # print(parts[5], parts[10])
            from_bot, low_to, high_to = [int(n) for n in re.findall(r'\d+', line)]
            low_designator = parts[5]
            high_designator = parts[10]

            if from_bot not in bots:
                bots[from_bot] = []

            if len(bots[from_bot]) == 2:
                print(bots[from_bot])

            if low_designator == 'output' and low_to not in outputs:
                outputs[low_to] = []
            if high_designator == 'output' and high_to not in outputs:
                outputs[high_to] = []
            if low_designator == 'bot' and low_to not in bots:
                bots[low_to] = []
            if high_designator == 'bot' and high_to not in bots:
                bots[high_to] = []


            if low_designator == 'output' and len(bots[from_bot]) >= 1:
                lowest = min(bots[from_bot])
                outputs[low_to].append(lowest)
                bots[from_bot].remove(lowest)

            if low_designator == 'bot' and len(bots[from_bot]) >= 1:
                lowest = min(bots[from_bot])
                bots[low_to].append(lowest)
                bots[from_bot].remove(lowest)

            if high_designator == 'output' and len(bots[from_bot]) >= 1:
                highest = max(bots[from_bot])
                outputs[high_to].append(highest)
                bots[from_bot].remove(highest)

            if high_designator == 'bot' and len(bots[from_bot]) >= 1:
                highest = max(bots[from_bot])
                bots[high_to].append(highest)
                bots[from_bot].remove(highest)

            if len(bots[from_bot]) == 2:
                print(bots[from_bot])

            # print(bots)
            # print(outputs)
            # if len(bots[from_bot]) >= 1:
            #     highest = max(bots[from_bot])
            #     bots[high_to_bot].append(highest)
            #     bots[from_bot].remove(highest)

        # print(bots)
        print(outputs)

        found = 0
        for i, bot in bots.items():
            # if 44 in bots[i]:
            #     print(i, bot)
            if 61 in bots[i]:
                print(i, bot)
            if 17 in bots[i]:
                print(i, bot)
            # if 61 in bots[i] and 17 in bots[i]:
            #     found = i


        return found


def part2(file_path):
    with open(file_path, 'r') as file:
        input_data = [line for line in file.read().splitlines()]
        # answer = 0
        #
        # for line in input_data:
        #     print(line)
        #
        # return answer


# print("Part 1: ", part1('input_test.txt'))
print("Part 1: ", part1('input.txt'))
print("Part 2: ", part2('input_test.txt'))
