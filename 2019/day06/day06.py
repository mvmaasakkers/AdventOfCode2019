data = [l.split(")") for l in open('2019/day06/input.txt').read().split('\n')]
objects = {l[1]: [] for l in data}
for line in data:
    objects[line[1]].append(line[0])

def traverse(obj, to):
    if obj in objects:
        if obj != to:
            for o in objects[obj]:
                if o in objects:
                    return [obj] + traverse(o, to)
    return [obj]

print("Part 1:", sum([len(traverse(o, 'COM')) for o in objects]))

youToCOM = traverse('YOU', 'COM')
sanToCOM = traverse('SAN', 'COM')

base = [planet for planet in youToCOM if planet in sanToCOM][0]

# The 2 times - 2 are for removing the start and end object from the list
print("Part 2:", len(traverse('YOU', base)) - 2 + len(traverse('SAN', base)) - 2)
