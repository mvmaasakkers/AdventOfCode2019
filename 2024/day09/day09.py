def part1(file_path):
    with open(file_path) as f:
        disk = f.read().strip()
        blocks = []

        for i in range(len(disk)):
            ch = i // 2 if i % 2 == 0 else "."
            blocks.extend([ch] * int(disk[i]))

        while blocks.count("."):
            pos = blocks.index(".")
            n = blocks.pop()
            blocks[pos] = n

            while blocks[-1] == ".":
                blocks.pop()

        return sum(c * i for i, c in enumerate(blocks))


def clean_free(free_space):
    new_free_space = []
    free_space.sort(key=lambda x: x[0])

    for fpos, fsize in free_space:
        if fsize == 0:
            continue

        if len(new_free_space) == 0:
            new_free_space.append((fpos, fsize))
        else:
            if new_free_space[-1][0] + new_free_space[-1][1] == fpos:
                new_free_space[-1] = (new_free_space[-1]
                                      [0], new_free_space[-1][1] + fsize)
            else:
                new_free_space.append((fpos, fsize))

    return new_free_space


def part2(file_path):
    with open(file_path) as f:
        disk = f.read().strip()

        files = []
        free_space = []

        pos = 0
        for idx in range(len(disk)):

            size = int(disk[idx])

            if idx % 2 == 0:
                files.append((idx // 2, pos, size))
            else:
                free_space.append((pos, size))

            pos += size

        for fi in range(len(files))[::-1]:
            fid, fpos, fsize = files[fi]
            if fsize == 0:
                continue

            for i in range(len(free_space)):
                free_pos, free_size = free_space[i]

                if fsize <= free_size and free_pos < fpos:
                    files[fi] = (fid, free_pos, fsize)

                    if free_size == fsize:
                        free_space.pop(i)
                    else:
                        free_space[i] = (free_pos + fsize, free_size - fsize)

                    free_space.append((fpos, fsize))

                    free_space = clean_free(free_space)

                    break

        return sum((fpos + i) * fid for fid, fpos, fsize in files for i in range(fsize))


print("Part 1: ", part1('input.txt'))
print("Part 2: ", part2('input.txt'))
