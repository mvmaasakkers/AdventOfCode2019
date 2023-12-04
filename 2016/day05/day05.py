import hashlib


def part1(file_path):
    with open(file_path, 'r') as file:
        input_data = file.read()

        start = 0
        pw = ""
        for _ in range(8):
            for i in range(start, start + 113241929):
                hash = hashlib.md5(str(input_data + str(i)).encode()).hexdigest()

                if hash[:5] == "00000":
                    start = i + 1
                    pw += hash[5]
                    break

        return pw


def part2(file_path):
    with open(file_path, 'r') as file:
        input_data = file.read()

        start = 0
        pw = ["" for _ in range(8)]
        while any(item == "" for item in pw):
            for i in range(start, start + 113241929):
                hash = hashlib.md5(str(input_data + str(i)).encode()).hexdigest()

                if hash[:5] == "00000":
                    if hash[5].isdigit() and 0 <= int(hash[5]) <= 7 and pw[int(hash[5])] == "":
                        pw[int(hash[5])] = hash[6]

                    start = i + 1

                    break

        return ''.join(pw)


print("Part 1: ", part1('input.txt'))
print("Part 2: ", part2('input.txt'))
