def get_data(file):
    with open(file, 'r') as f:
        data = list(map(int, f.read().split(',')))
    return data

origLocations = get_data('2019/day02/input.txt')

def part_one(locs, noun, verb):
    loc = list.copy(locs)
    loc[1] = noun
    loc[2] = verb
    pos = 0
    while True:
        opcode = loc[pos]
        if opcode not in [99]:
            input1Pos = loc[pos+1]
            if opcode in [1, 2, 3]:
                input2Pos = loc[pos+2]
            if opcode in [1, 2]:
                outputPos = loc[pos+3]

        if opcode == 1:
            loc[outputPos] = loc[input1Pos] + loc[input2Pos]

        if opcode == 2:
            loc[outputPos] = loc[input1Pos] * loc[input2Pos]
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