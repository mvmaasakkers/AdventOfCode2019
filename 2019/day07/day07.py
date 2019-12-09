from itertools import permutations
from copy import copy
import sys
import os
sys.path.append(os.path.abspath("2019"))
import intcode

def get_data(file):
    with open(file, 'r') as f:
        data = list(map(int, f.read().split(",")))
    return data

# data = get_data("2019/day07/input.txt")

options = list(permutations([0, 1, 2, 3, 4]))

def getPhasePerms(phases):
    phase_perms = [[]]
    for n in phases:
        new_perm = []
        for perm in phase_perms:
            for i in range(len(perm) + 1):
                new_perm.append(perm[:i] + [n] + perm[i:])
                phase_perms = new_perm
    return phase_perms

def part_one():
    max_thruster_signal = 0
    phasePerms = getPhasePerms(range(0, 5))

    program = get_data("2019/day07/input.txt")
    for phasePerm in phasePerms:
        out = 0 
        while len(phasePerm) > 0:
            out = intcode.RUN(program.copy(), [phasePerm.pop(0), out], False, 0)
        max_thruster_signal = max(max_thruster_signal, out)
    return max_thruster_signal

def runWithPase(program, phase_setting):
    programs, pcs, inputs = [], [], []
    num_amps = len(phase_setting)
    amp_output = 0
    for i in range(0, num_amps):
        programs.append(program.copy())
        pcs.append(0)
        inputs.append([phase_setting[i]])
    while pcs[0] is not None:
        for i in range(0, num_amps):
            inputs[i].append(amp_output)
            amp_output, pc = intcode.RUN(programs[i], inputs[i], True, pcs[i])
            pcs[i] = pc
    return inputs[0][0]


def part_two():
    max_thruster_signal = 0
    for phase_perm in getPhasePerms(range(5, 10)):
        max_thruster_signal = max(max_thruster_signal, runWithPase(get_data("2019/day07/input.txt"), phase_perm))
    return max_thruster_signal

print("Part 1:", part_one())
print("Part 2:", part_two())
