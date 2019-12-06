def get_data(file):
    with open(file, 'r') as f:
        data = list(map(str, f.read().split("\n")))
    return data

data = get_data("2019/day06/input.txt")
objects = {line.split(")")[1]: [] for line in data}
for line in data:
    parts = line.split(")")
    objects[parts[1]].append(parts[0])

def traverse(obj, i):
    i.append(obj)
    if obj in objects:
        for o in objects[obj]:
            if o in objects:
                return traverse(o, i)
    return i

def traverseTo(obj, to, i):
    i.append(obj)
    if obj in objects:
        if obj != to:
            for o in objects[obj]:
                if o in objects:
                    return traverseTo(o, to, i)
    return i

print("Part 1:", sum([len(traverse(o, [])) for o in objects]))

youToCOM = traverse('YOU', [])
sanToCOM = traverse('SAN', [])

base = [planet for planet in youToCOM if planet in sanToCOM][0]

# The 2 times - 2 are for removing the start and end object from the list
print("Part 2:", len(traverseTo('YOU', base, [])) - 2 + len(traverseTo('SAN', base, [])) - 2)
