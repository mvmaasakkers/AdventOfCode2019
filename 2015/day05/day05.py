def get_data(file):
    with open(file, 'r') as f:
        data = list(map(str, f.read().split("\n")))
    return data


lines = get_data("2015/day05/input.txt")

vowels = ['a', 'e', 'i', 'o', 'u']
notAllowed = ['ab', 'cd', 'pq', 'xy']

print("Part 1:", len([line for line in lines if any(c1 == c2 for c1, c2 in zip(str(line), str(line)[1:])) and len(
    [e for e in notAllowed if e in line]) == 0 and sum([line.count(i) for i in vowels if i in line]) >= 3]))

