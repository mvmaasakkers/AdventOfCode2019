from itertools import permutations

def get_data(file):
    with open(file, 'r') as f:
        data = list(map(int, f.read().split(",")))
    return data

data = get_data("2019/day07/input.txt")

scoopOver = {1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4, 99: 0}

def RUN(locs, userInput, userInput2):
    loc = list.copy(locs)
    pos = 0
    input1Given = False

    while True:
        pointerChanged = False
        rawOpcode = loc[pos]
        opcode = rawOpcode
        parameterMode = False # 0 = position mode
        if rawOpcode > 100:
            parameterMode = True
            opcode = int(str(rawOpcode)[-2:])
            c = int(str(rawOpcode)[-3:-2] if len(str(rawOpcode)) >= 3 else 0)
            b = int(str(rawOpcode)[-4:-3] if len(str(rawOpcode)) >= 4 else 0)
            a = int(str(rawOpcode)[-5:-4] if len(str(rawOpcode)) == 5 else 0)
            
        
        scoop = scoopOver[opcode]
        
        if opcode not in [99]:
            input1Pos = pos+1 if parameterMode and c == 1 else loc[pos+1]
            if opcode in [1, 2, 3, 5, 6, 7, 8]:
                input2Pos = pos+2 if parameterMode and b == 1 else loc[pos+2]
            if opcode in [1, 2, 7, 8]:
                # outputPos = pos+3 if parameterMode and a == 1 else loc[pos+3]
                # Parameters that an instruction writes to will never be in immediate mode.
                outputPos = loc[pos+3]
        
        if opcode == 1:
            # add
            loc[outputPos] = loc[input1Pos] + loc[input2Pos]
        if opcode == 2:
            # multiply
            loc[outputPos] = loc[input1Pos] * loc[input2Pos]
        if opcode == 3:
            # input
            loc[loc[pos+1]] = userInput if input1Given == False else userInput2
            input1Given = True
        if opcode == 4:
            # output
            if loc[input1Pos] != 0:
                return loc[input1Pos]
        if opcode == 5:
            # jump-if-true
            if loc[input1Pos] != 0:
                pointerChanged = True
                pos = loc[input2Pos]
        if opcode == 6:
            # jump-if-false
            if loc[input1Pos] == 0:
                pointerChanged = True
                pos = loc[input2Pos]
        if opcode == 7:
            # less-than
            loc[outputPos] = 1 if loc[input1Pos] < loc[input2Pos] else 0
        if opcode == 8:
            # equals
            loc[outputPos] = 1 if loc[input1Pos] == loc[input2Pos] else 0
        if opcode == 99:
            # end
            break

        if not pointerChanged:
            pos = pos + scoop
    return 0

# phase = [4, 3, 2, 1, 0]

options = list(permutations([0, 1, 2, 3, 4]))
options2 = list(permutations([5, 6, 7, 8, 9]))

# print(options2)
def Thrust(phase, userInput):
    return RUN(data, phase[4], RUN(data, phase[3], RUN(data, phase[2], RUN(data, phase[1], RUN(data, phase[0], 0)))))

print("Part 1:", max([Thrust(phase, 0) for phase in options]))
print("Part 2:", max([Thrust(phase, 0) for phase in options2]))
# print("Part 1:", RUN(data, phase[4], RUN(data, phase[3], RUN(data, phase[2], RUN(data, phase[1], RUN(data, phase[0], 0))))))
