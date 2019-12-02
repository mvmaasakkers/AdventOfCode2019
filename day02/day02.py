
origLocations = []
with open('day02/input.txt', 'r') as f:
    for line in f:
        if line != '':
            origLocations = list(map(int, line.split(",")))

part1 = 0
part2 = 0

answerP2 = 19690720

pos = 0
locations = list.copy(origLocations)
locations[1] = 12
locations[2] = 2
while True:
    opcode = locations[pos]
    if opcode == 1:
        # Add
        param1 = locations[locations[pos+1]]
        param2 = locations[locations[pos+2]]
        locations[locations[pos+3]] = param1 + param2

    if opcode == 2:
        # Multiply
        param1 = locations[locations[pos+1]]
        param2 = locations[locations[pos+2]]
        locations[locations[pos+3]] = param1 * param2

    if opcode == 99:
        # End
        part1 = locations[0]
        break

    pos = pos + 4


for i in range(1,99):
    for j in range(1, 99):
        locations = list.copy(origLocations)
        # print(locations)
        # exit
        locations[1] = i
        locations[2] = j
        res = 0
        pos = 0
        while True:
            opcode = locations[pos]
            if opcode == 1:
                # Add
                param1 = locations[locations[pos+1]]
                param2 = locations[locations[pos+2]]
                locations[locations[pos+3]] = param1 + param2

            if opcode == 2:
                # Multiply
                param1 = locations[locations[pos+1]]
                param2 = locations[locations[pos+2]]
                locations[locations[pos+3]] = param1 * param2

            if opcode == 99:
                # End
                res = locations[0]
                if res == answerP2:
                    part2 = (100 * i + j)
                break

            pos = pos + 4


print("Part 1:", part1);
print("Part 2:", part2);