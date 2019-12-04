start = 264360
end = 746325

def validatePartOne(n):
    chr = str(n)

    hasDeclines = False
    for c in range(len(chr)):
        if c > 0 and (int(chr[c]) < int(chr[c-1])):
            hasDeclines = True
            break

    if hasDeclines == True:
        return False

    hasDouble = False
    for c in range(len(chr)):
        if c > 0 and (chr[c] ==chr[c-1]):
            hasDouble = True
            break

    if hasDouble == False:
        return False

    return True

def validatePartTwo(n):
    chr = str(n)
    for c in chr:
        if chr.count(c) == 2:
            return True

    return False

print("Part 1:", len([x for x in range(start, end) if validatePartOne(x)]))
print("Part 2:", len([x for x in range(start, end) if validatePartOne(x) and validatePartTwo(x)]))