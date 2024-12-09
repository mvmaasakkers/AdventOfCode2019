def eval_right_to_left(l: list[int], target: int) -> bool:
    if len(l) == 1:
        return l[0] == target

    n = l.pop(0)

    l1 = l.copy()

    l[0] += n
    l1[0] *= n

    return eval_right_to_left(l, target) or eval_right_to_left(l1, target)


def part1(file_path):
    with open(file_path, 'r') as file:
        input_data = [line for line in file.read().splitlines()]
        # answer = 0
        inp = {}

        cals = []

        for l in input_data:
            ps = l.strip().split(":")
            inp[int(ps[0])] = list(map(int, ps[1].split()))
            cals.append((int(ps[0]), list(map(int, ps[1].split()))))

        return sum(v for v, nums in cals if eval_right_to_left(nums, v))


def eval_right_to_left_2(numbers: list[int], target: int) -> bool:
    if len(numbers) == 1:
        return numbers[0] == target

    n = numbers.pop(0)

    numbers1 = list(numbers)
    numbers2 = list(numbers)
    numbers3 = list(numbers)

    numbers1[0] += n
    numbers2[0] *= n
    numbers3[0] = int(str(n) + str(numbers3[0]))

    return (
            eval_right_to_left_2(numbers1, target)
            or eval_right_to_left_2(numbers2, target)
            or eval_right_to_left_2(numbers3, target)
    )


def part2(file_path):
    with open(file_path, 'r') as file:
        input_data = [line for line in file.read().splitlines()]
        answer = 0
        inp = {}

        cals = []

        for l in input_data:
            ps = l.strip().split(":")
            inp[int(ps[0])] = list(map(int, ps[1].split()))
            cals.append((int(ps[0]), list(map(int, ps[1].split()))))

        return sum(v for v, nums in cals if eval_right_to_left_2(nums, v))


print("Part 1: ", part1('input.txt'))
print("Part 2: ", part2('input.txt'))
