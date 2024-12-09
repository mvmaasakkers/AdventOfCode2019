def valid(rules: dict[int, set[int]], update: list[int]):
    ns = set()
    for n in update:
        if ns & rules.get(n, set()):
            return False
        ns.add(n)
    return True

def part1(file_path):
    with open(file_path, 'r') as file:
        page_ordering_rules, update_spec = file.read().split("\n\n")

        rules: dict[int, set[int]] = {}
        for line in page_ordering_rules.split("\n"):
            x, y = line.split("|")
            if int(x) in rules:
                rules[int(x)].add(int(y))
            else:
                rules[int(x)] = {int(y)}

        updates = [[int(n) for n in line.split(",")] for line in update_spec.split("\n") if line]

        a1 = 0
        for update in updates:
            k = len(update) // 2
            if valid(rules, update):
                a1 += update[k]
        return a1


def median(rules: dict[int, set[int]], update: set[int], k: int) -> int:
    candidate = update.pop()
    if not update:
        return candidate
    gt_candidate = update - rules.get(candidate, set())
    lt_candidate = update - gt_candidate

    N = len(lt_candidate)
    if N == k:
        return candidate
    if k < N:
        return median(rules, lt_candidate, k)
    return median(rules, gt_candidate, k - N - 1)


def part2(file_path):
    with open(file_path, 'r') as file:
        page_ordering_rules, update_spec = file.read().split("\n\n")

        rules: dict[int, set[int]] = {}
        for line in page_ordering_rules.split("\n"):
            x, y = line.split("|")
            if int(x) in rules:
                rules[int(x)].add(int(y))
            else:
                rules[int(x)] = {int(y)}

        updates = [[int(n) for n in line.split(",")] for line in update_spec.split("\n") if line]

        a1, a2 = 0, 0
        for update in updates:
            k = len(update) // 2
            if valid(rules, update):
                a1 += update[k]
            else:
                a2 += median(rules, set(update), k)
        return a2


print("Part 1: ", part1('input.txt'))
print("Part 2: ", part2('input.txt'))
