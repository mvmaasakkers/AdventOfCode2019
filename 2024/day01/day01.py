def part1(file_path):
    with open(file_path, 'r') as file:
        input_data = [[int(i) for i in line.split('   ')] for line in file.read().splitlines()]
        answer = 0

        l1 = sorted([i[0] for i in input_data])
        l2 = sorted([i[1] for i in input_data])

        for i, line in enumerate(input_data):
            # print(abs(l1[i] - l2[i]))
            answer += abs(l1[i] - l2[i])
            # print(i, line)

        # print(l1, l2)
        return answer


def part2(file_path):
    with open(file_path, 'r') as file:
        input_data = [[int(i) for i in line.split('   ')] for line in file.read().splitlines()]
        answer = 0

        l1 = [i[0] for i in input_data]
        l2 = [i[1] for i in input_data]

        for i, num in enumerate(l1):
            occ = [x for x in l2 if x == num]
            answer += num * len(occ)

        return answer


print("Part 1: ", part1('input.txt'))
print("Part 2: ", part2('input.txt'))
