def part1(file_path):
    with open(file_path, 'r') as file:
        input_data = [line for line in file.read().splitlines()]
        answer = 0

        for line in input_data:
            numbers = [int(n) for n in line.split(' ')]
            listdiff = [numbers]
            curdiff = numbers

            newdiff = []
            while len([1 for n in curdiff if n == 0]) != len(curdiff):
                for i in range(len(curdiff)):
                    if i + 1 < len(curdiff):
                        newdiff.append(curdiff[i + 1] - curdiff[i])

                curdiff = newdiff
                listdiff.append(newdiff)
                newdiff = []

            for diffI in range(len(listdiff)-2, -1, -1):
                if diffI <= len(listdiff):
                    listdiff[diffI-1].append(listdiff[diffI-1][-1] + listdiff[diffI][-1])

            answer += listdiff[0][-1]

        return answer


def part2(file_path):
    with open(file_path, 'r') as file:
        input_data = [line for line in file.read().splitlines()]
        answer = 0

        for line in input_data:
            numbers = [int(n) for n in line.split(' ')][::-1]
            listdiff = [numbers]
            curdiff = numbers

            newdiff = []
            while len([1 for n in curdiff if n == 0]) != len(curdiff):
                for i in range(len(curdiff)):
                    if i + 1 < len(curdiff):
                        newdiff.append(curdiff[i + 1] - curdiff[i])

                curdiff = newdiff
                listdiff.append(newdiff)
                newdiff = []

            for diffI in range(len(listdiff) - 2, -1, -1):
                if diffI <= len(listdiff):
                    listdiff[diffI - 1].append(listdiff[diffI - 1][-1] + listdiff[diffI][-1])

            answer += listdiff[0][-1]

        return answer


print("Part 1: ", part1('input.txt'))
print("Part 2: ", part2('input.txt'))
