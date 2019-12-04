def get_data(file):
    with open(file, 'r') as f:
        data = list(map(int, f.read().split(',')))
    return data

origLocations = get_data('day02/input.txt')

def part_one(locs, noun, verb):
    loc = list.copy(locs)
    loc[1] = noun
    loc[2] = verb
    pos = 0
    while True:
        opcode = loc[pos]
        if opcode == 1:
            loc[loc[pos+3]] = loc[loc[pos+1]] + loc[loc[pos+2]]

        if opcode == 2:
            loc[loc[pos+3]] = loc[loc[pos+1]] * loc[loc[pos+2]]
        if opcode == 99:
            # End
            return loc[0]
            break

        pos = pos + 4

def part_two(origLocations, output):
  for i in range(1,99):
    for j in range(1, 99):
        if part_one(origLocations, i, j) == output:
            return (100 * i) + j

print("Part 1:", part_one(origLocations, 12, 2));
print("Part 2:", part_two(origLocations, 19690720));