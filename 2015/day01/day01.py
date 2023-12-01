def get_data(file):
    with open(file, 'r') as f:
        data = f.readline()
    return data

data = get_data("input.txt")

part1 = data.count("(") - data.count(")")

level = 0
part2 = 0

dirs = {"(": 1, ")": -1}
for l in range(len(data)):
    part2 = l
    x = data[l]
    if level == -1:
        break
    level += dirs[x]
      
print("Part 1:", part1)
print("Part 2:", part2)