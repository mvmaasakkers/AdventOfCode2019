def get_data(file):
    with open(file, 'r') as f:
        data = f.readline()
    return data

data = get_data("2015/day03/input.txt")
# data = "^>v<"
grid = [[0] * (len(data)*2) for _ in range(len(data)*2)]
# print(data)

pointer = {'x': len(data), 'y': len(data)}
grid[pointer['y']][pointer['x']] = 1
for direction in data:
    if direction == "^":
        pointer['y'] -= 1
    if direction == "v":
        pointer['y'] += 1
    if direction == "<":
        pointer['x'] -= 1
    if direction == ">":
        pointer['x'] += 1
    grid[pointer['y']][pointer['x']] += 1
    
houses = [y for x in grid for y in x if y > 0]
print("Part1:", len(houses))
