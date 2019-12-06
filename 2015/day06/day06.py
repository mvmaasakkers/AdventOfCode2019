def showGrid(g):
    looper = [[x for x in range(gridWidth)] for y in range(gridHeight)]
    for y in range(len(looper)):
        for x in looper[y]:
            if g[str(y)+str(',')+str(x)] == True:
                print("X", end='')
            else:
                print(".", end='')
        print('')
    print('')


def showBrightness(g):
    looper = [[x for x in range(gridWidth)] for y in range(gridHeight)]
    for y in range(len(looper)):
        for x in looper[y]:
            print(g[str(y)+str(',')+str(x)], end='')
        print('')
    print('')


# Todo: Make this waaaaay more idiomatic
def parseLine(l):
    parts = l.replace('turn on', 'turn-on').replace('turn off', 'turn-off').split(' ')
    startLoc = list(map(int, parts[1].split(',')))
    endLoc = list(map(int, parts[3].split(',')))
    return {'command': parts[0], 'start': parts[1], 'startLoc': {'y': startLoc[0], 'x': startLoc[1]}, 'end': parts[3], 'endLoc': {'y': endLoc[0], 'x': endLoc[1]}}
    
gridHeight = 1000
gridWidth = 1000

data = [parseLine(line) for line in open('2015/day06/input.txt').read().splitlines()]
grid = dict([str(y)+str(',')+str(x), False] for x in range(gridWidth) for y in range(gridHeight))
brightness = dict([str(y)+str(',')+str(x), 0] for x in range(gridWidth) for y in range(gridHeight))

for line in data:
    if line['command'] == 'turn-on':
        grid.update({i: True for i in [str(y)+str(',')+str(x) for x in range(line['startLoc']['x'],line['endLoc']['x']+1) for y in range(line['startLoc']['y'],line['endLoc']['y']+1)]})
        brightness.update({i: brightness[i]+1 for i in [str(y)+str(',')+str(x) for x in range(line['startLoc']['x'],line['endLoc']['x']+1) for y in range(line['startLoc']['y'],line['endLoc']['y']+1)]})
    if line['command'] == 'turn-off':
        grid.update({i: False for i in [str(y)+str(',')+str(x) for x in range(line['startLoc']['x'],line['endLoc']['x']+1) for y in range(line['startLoc']['y'],line['endLoc']['y']+1)]})
        brightness.update({i: brightness[i]-1 if brightness[i] > 0 else 0 for i in [str(y)+str(',')+str(x) for x in range(line['startLoc']['x'],line['endLoc']['x']+1) for y in range(line['startLoc']['y'],line['endLoc']['y']+1)]})
    if line['command'] == 'toggle':
        grid.update({i: True if grid[i] == False else False for i in [str(y)+str(',')+str(x) for x in range(line['startLoc']['x'],line['endLoc']['x']+1) for y in range(line['startLoc']['y'],line['endLoc']['y']+1)]})
        brightness.update({i: brightness[i]+2 for i in [str(y)+str(',')+str(x) for x in range(line['startLoc']['x'],line['endLoc']['x']+1) for y in range(line['startLoc']['y'],line['endLoc']['y']+1)]})

print('Part 1:', len([x for x in grid if grid[x] == True]))
print('Part 2:', sum([brightness[x] for x in brightness]))

