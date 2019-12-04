start = 264360
end = 746325

options = (x for x in range(start, end))


def hasDeclines(n):
    return any(c1 > c2 for c1, c2 in zip(str(n), str(n)[1:]))


def hasDouble(n):
    return any(c1 == c2 for c1, c2 in zip(str(n), str(n)[1:]))


def hasMoreThanDouble(n):
    return any(c for c in n if n.count(c) == 2)


possibilities = []
part2Possibilities = []
for o in options:
    chr = str(o)
    if not hasDeclines(chr) and hasDouble(chr):
        possibilities.append(chr)
        if hasMoreThanDouble(chr):
            part2Possibilities.append(chr)

part1 = len(possibilities)
print("Part 1:", part1)

part2 = len(part2Possibilities)
print("Part 2:", part2)
