def get_data(file):
    with open(file, 'r') as f:
        data = f.read()
    return data


def split(data, length):
    chunks, chunk_size = len(data), len(data)//(len(data)//length)
    lst = [data[i:i+chunk_size] for i in range(0, chunks, chunk_size)]    
    return lst

data = get_data("2019/day08/input.txt")

lst = split(data, 25*6)
lst0 = [x.count('0') for x in lst]
minList = min(list(zip([x.count('0') for x in lst], lst)))[1]
print('Part 1:', minList.count('1') * minList.count('2'))

extendedLayer = list(lst[0])
for layer in lst:
    newLayer = []
    cl = list(layer)
    for c in range(len(cl)):
        if extendedLayer[c] == '2':
            newLayer.append(cl[c])
        else:
            newLayer.append(extendedLayer[c])
    extendedLayer = newLayer

parts = split(extendedLayer, 25)
for part in parts:
    for c in part:
        if c == '0':
            print(' ', end='')
        if c == '1':
            print('X', end='')
    print('')
