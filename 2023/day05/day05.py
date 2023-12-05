from itertools import count


def part1(file_path):
    with open(file_path, 'r') as file:
        input_data = [line for line in file.read().split("\n\n")]

        seed_names, map_sets = input_data[0], input_data[1:]
        seeds = [int(n) for n in input_data[0][len('seeds: '):].split(' ')]
        locations = []

        for seed in seeds:
            location = seed
            for map_set in map_sets:
                for line in map_set.split('\n')[1:]:
                    dst_start, src_start, rng = [int(n) for n in line.split(' ')]
                    if location in range(src_start, src_start + rng):
                        location = dst_start + (location - src_start)
                        break
            locations.append(location)

        return min(locations)


def part2(file_path):
    with open(file_path, 'r') as file:
        input_data = file.read()
        lines = input_data.split("\n\n")

        seeds = [int(n) for n in lines[0][len('seeds: '):].split(' ')]
        parts = lines[1:]
        collections = []
        for part in parts:
            collections.append("\n".join(part.split("\n")[1:]))

        nsss = [[int(n) for n in collection.split(' ')] for collection in collections[0].split("\n")]
        nssf = [[int(n) for n in collection.split(' ')] for collection in collections[1].split("\n")]
        nsfw = [[int(n) for n in collection.split(' ')] for collection in collections[2].split("\n")]
        nswl = [[int(n) for n in collection.split(' ')] for collection in collections[3].split("\n")]
        nslt = [[int(n) for n in collection.split(' ')] for collection in collections[4].split("\n")]
        nsth = [[int(n) for n in collection.split(' ')] for collection in collections[5].split("\n")]
        nshl = [[int(n) for n in collection.split(' ')] for collection in collections[6].split("\n")]

        # Part 2
        def seedsoilinv(inp):
            for nl in nsss:
                if nl[0] <= inp < nl[0] + nl[2]:
                    return nl[1] + (inp - nl[0])
            return inp

        def soilfertinv(inp):
            for nl in nssf:
                if nl[0] <= inp < nl[0] + nl[2]:
                    return nl[1] + (inp - nl[0])
            return inp

        def fertwatinv(inp):
            for nl in nsfw:
                if nl[0] <= inp < nl[0] + nl[2]:
                    return nl[1] + (inp - nl[0])
            return inp

        def watlightinv(inp):
            for nl in nswl:
                if nl[0] <= inp < nl[0] + nl[2]:
                    return nl[1] + (inp - nl[0])
            return inp

        def lighttempinv(inp):
            for nl in nslt:
                if nl[0] <= inp < nl[0] + nl[2]:
                    return nl[1] + (inp - nl[0])
            return inp

        def temphuminv(inp):
            for nl in nsth:
                if nl[0] <= inp < nl[0] + nl[2]:
                    return nl[1] + (inp - nl[0])
            return inp

        def humlocinv(inp):
            for nl in nshl:
                if nl[0] <= inp < nl[0] + nl[2]:
                    return nl[1] + (inp - nl[0])
            return inp

        def is_needed(n):
            for x, y in zip(seeds[::2], seeds[1::2]):
                if x <= n < x + y:
                    return True
            return False

        for n in count():
            seed = seedsoilinv(
                soilfertinv(fertwatinv(watlightinv(lighttempinv(temphuminv(humlocinv(n))))))
            )
            if is_needed(seed):
                return n


print("Part 1: ", part1('input.txt'))
print("Part 2: ", part2('input.txt'))
