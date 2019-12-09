def getOpcode(mem, instructionPointer):
    return mem[instructionPointer] % 100

def getMode(mem, instructionPointer, param):
    return (mem[instructionPointer] // (10**(param+1))) %10

def getParam(mem, instructionPointer, param, rel):
    if getMode(mem, instructionPointer, param) == 2:
        return mem[mem[instructionPointer + param] + rel]
    elif getMode(mem, instructionPointer, param) == 1:
        return mem[instructionPointer + param]
    else:
        return mem[mem[instructionPointer + param]]

def setParam(mem, instructionPointer, param, rel, val):
    if getMode(mem, instructionPointer, param) == 2:
        mem[mem[instructionPointer + param] + rel] = val
    elif getMode(mem, instructionPointer, param) == 1:
        mem[instructionPointer + param] = val
    else:
        mem[mem[instructionPointer + param]] = val

def RUN(program, userInput, isFeedback=False, pos=0, memorySize=10000, returnLoc0=False):
    memory = list.copy(program) + [0 for x in range(memorySize)]
    diagnostic = 0
    relativeBase = 0
    while pos < len(program):
        opcode = getOpcode(memory, pos)

        if opcode == 1:  # ADD
            # setParam(mem, 3, )
            setParam(memory, pos, 3, relativeBase, getParam(memory, pos, 1, relativeBase) + getParam(memory, pos, 2, relativeBase))
            pos += 4
        elif opcode == 2:  # MULTIPLY
            # multiply
            setParam(memory, pos, 3, relativeBase, getParam(memory, pos, 1, relativeBase) * getParam(memory, pos, 2, relativeBase))
            pos += 4
        elif opcode == 3:  # USER INPUT
            if len(userInput) == 0:
                raise Exception('no input!')

            setParam(memory, pos, 1, relativeBase, userInput.pop(0))
            pos += 2
        elif opcode == 4:  # OUTPUT
            diagnostic = getParam(memory, pos, 1, relativeBase)
            pos += 2

            if isFeedback:  # and loc[input1Pos] != 0
                return diagnostic, pos
        elif opcode == 5:  # JUMP IF TRUE
            if getParam(memory, pos, 1, relativeBase) != 0:
                pos = getParam(memory, pos, 2, relativeBase)
            else:
                pos += 3
        elif opcode == 6:  # JUMP IF FALSE
            if getParam(memory, pos, 1, relativeBase) == 0:
                pos = getParam(memory, pos, 2, relativeBase)
            else:
                pos += 3
        elif opcode == 7:  # LESS THAN
            # less-than
            if getParam(memory, pos, 1, relativeBase) < getParam(memory, pos, 2, relativeBase):
                setParam(memory, pos, 3, relativeBase, 1)
            else:
                setParam(memory, pos, 3, relativeBase, 0)
            pos += 4
        elif opcode == 8:  # EQUALS
            if getParam(memory, pos, 1, relativeBase) == getParam(memory, pos, 2, relativeBase):
                setParam(memory, pos, 3, relativeBase, 1)
            else:
                setParam(memory, pos, 3, relativeBase, 0)
            pos += 4
        elif opcode == 9:  # ADJUST RELATIVE BASE
            relativeBase += getParam(memory, pos, 1, relativeBase)
            pos += 2
        elif opcode == 99:  # HALT
            # end
            if isFeedback:
                if returnLoc0:
                    return memory[0]
                return diagnostic, None
            break
        else:
            print("Unknown opcode")
            break

    return diagnostic
