

def get_data(file):
    with open(file, 'r') as f:
        data = list(map(str, f.read().split("\n")))
    if data[len(data)-1] == "":
        del data[len(data)-1]
    return data


packages = get_data("2015/day02/input.txt")

keys = "lxwxh"
part1 = 0
part2 = 0
for package in packages:
    dimensions = dict(zip(keys.split("x"), list(map(int, package.split("x")))))
    
    sides = [(dimensions['l']*dimensions['w']), (dimensions['w'] *
                                                 dimensions['h']), (dimensions['h']*dimensions['l'])]

    ribbon = (dimensions['l']*dimensions['w']*dimensions['h'])
    ribbon += 2 * min([(dimensions['l']+dimensions['w']), (dimensions['w'] +
                                                 dimensions['h']), (dimensions['h']+dimensions['l'])])
    
    part1 += sum([x * 2 for x in sides]) + min(sides)
    part2 += ribbon

print(part1)
print(part2)
