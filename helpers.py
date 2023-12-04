def transpose(lst):
    iRows = len(lst)
    iCols = len(lst[0])

    newList = [[] for _ in range(iCols)]

    for r in range(iRows):
        for c in range(iCols):
            newList[c].append(lst[r][c])

    return newList

def batch(lst, size):
    return [lst[i:i + size] for i in range(0, len(lst), size)]


def print_grid(grid):
    for row in grid:
        for col in row:
            print(col, sep="", end="")
        print()