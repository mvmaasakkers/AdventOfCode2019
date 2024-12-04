from collections import defaultdict

from parse import parse

def part1(file_path):
    with open(file_path, 'r') as file:
        input_data = [line for line in file.read().splitlines()]

        answer = 0
        d = defaultdict(int)

        data = '\n'.join(input_data)

        data += '\n'
        data = data.replace('\n', ' else 0\n')
        data = data.replace('inc', '+=')
        data = data.replace('dec', '-=')

        exec(data, {}, d)
        answer = max(d.values())

        return answer


def part2(file_path):
    with open(file_path, 'r') as file:
        input_data = [parse('{registry} {op} {amount:d} if {cond_registry} {cond} {cond_amount:d}', line) for line in
                      file.read().splitlines()]
        answer = 0
        registries = {}
        for line in input_data:
            registries[line['registry']] = registries[line['registry']] if line['registry'] in registries else 0
            registries[line['cond_registry']] = registries[line['cond_registry']] if line[
                                                                                         'cond_registry'] in registries else 0


            do = False

            if line['cond'] == '>':
                if registries[line['cond_registry']] > line['cond_amount']:
                    do = True
            if line['cond'] == '<':
                if registries[line['cond_registry']] < line['cond_amount']:
                    do = True

            if line['cond'] == '>=':
                if registries[line['cond_registry']] >= line['cond_amount']:
                    do = True

            if line['cond'] == '<=':
                if registries[line['cond_registry']] <= line['cond_amount']:
                    do = True

            if line['cond'] == '==':
                if registries[line['cond_registry']] == line['cond_amount']:
                    do = True

            if line['cond'] == '!=':
                if registries[line['cond_registry']] != line['cond_amount']:
                    do = True

            if do:
                if line['op'] == 'inc':
                    registries[line['registry']] += line['amount']

                if line['op'] == 'dec':
                    registries[line['registry']] -= line['amount']
            for i, key in enumerate(registries.keys()):
                if registries[key] > answer:
                    answer = registries[key]

        return answer


print("Part 1: ", part1('input.txt'))
print("Part 2: ", part2('input.txt'))
