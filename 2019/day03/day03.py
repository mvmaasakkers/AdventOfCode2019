def get_data(file):
    with open(file, 'r') as f:
        data = list(map(str, f.read().split("\n")))
    return data


data = get_data("2019/day03/input.txt")

changeX = {'R': '1', 'L': '-1', 'U': '0', 'D': '0'}
changeY = {'R': '0', 'L': '0', 'U': '-1', 'D': '1'}

def part_one(first, second):
    pairs1 = set(())
    pairs2 = set(())

    def traverse(p):
        x = 0
        y = 0
        for f in p:
            d = f[0]
            n = int(f[1:])
            for i in range(n):
                x += int(changeX[d])
                y += int(changeY[d])
                if p == first:
                    pairs1.add((x, y))
                else:
                    pairs2.add((x, y))

    traverse(first)
    traverse(second)
    return min(abs(x)+abs(y) for (x, y) in pairs1 & pairs2)


def part_two(first, second):
    pair1 = set(())
    pair2 = set(())

    dist1 = {}
    dist2 = {}

    def traverse(p):
        x = 0
        y = 0
        z = 0
        for f in p:
            d = f[0]
            n = int(f[1:])
            for i in range(n):
                x += int(changeX[d])
                y += int(changeY[d])
                z += 1
                if p == first:
                    pair1.add((x, y))
                    if (x, y) not in dist1:
                        dist1.update({(x, y): z})
                else:
                    pair2.add((x, y))
                    if (x, y) not in dist2:
                        dist2.update({(x, y): z})

    traverse(first)
    traverse(second)

    return min(dist1[(x, y)] + dist2[(x, y)] for (x, y) in pair1 & pair2)


print("Part 1:", part_one(data[0].split(","), data[1].split(",")))
print("Part 2:", part_two(data[0].split(","), data[1].split(",")))
