start = 264360
end = 746325

options = [x for x in range(start, end)]

def hasDeclines(n):
    for c in range(len(n)):
        if c > 0 and (int(n[c]) < int(n[c-1])):
            return True
    return False

def hasDouble(n):
    for c in range(len(n)):
        if c > 0 and (int(n[c]) == int(n[c-1])):
            return True
    return False

def hasMoreThanDouble(n):
    for c in n:
        if n.count(c) == 2:
            return False
        
    return True

possibilities = []
part2Possibilities = []
for o in options:
    chr = str(o)
    if hasDeclines(chr) == False and hasDouble(chr) == True:
        possibilities.append(chr)
        if hasMoreThanDouble(chr) == False:
            part2Possibilities.append(chr)

part1 = len(possibilities)
print("Part 1:", part1)

part2 = len(part2Possibilities)
print("Part 2:", part2)