start = 264360
end = 746325


def validatePartOne(n):
    # Password option cannot have declining numbers
    if any(c1 > c2 for c1, c2 in zip(str(n), str(n)[1:])):
        return False

    # Password option should at least have one character that appears more than once
    if not any(c1 == c2 for c1, c2 in zip(str(n), str(n)[1:])):
        return False

    return True


def validatePartTwo(n):
    # Password option should have at least one character that appears exactly twice next to each other
    # This checks just if a char appears twice, but because of the cannot decline check of validate one this will work.
    return any(c for c in str(n) if str(n).count(c) == 2)


print("Part 1:", len([x for x in range(start, end) if validatePartOne(x)]))
print("Part 2:", len([x for x in range(start, end)
                      if validatePartOne(x) and validatePartTwo(x)]))
