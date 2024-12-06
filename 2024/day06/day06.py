import copy


def part1(file_path):
    with open(file_path, 'r') as file:
        input_data = [list(line) for line in file.read().splitlines()]
        answer = 0

        guard_location = (-1, -1)
        guard_character = '^'

        obstacles = []
        max_y = len(input_data)
        max_x = len(input_data[0])

        for row in range(len(input_data)):
            for col in range(len(input_data[row])):
                if input_data[row][col] == '^':
                    guard_location = (row, col)
                if input_data[row][col] == '#':
                    obstacles.append((row, col))
        visited_positions = [guard_location]
        guard_in_bounds = True

        maze = input_data

        max_steps = 60
        cur_step = 0

        # print("First maze")
        # print_maze(maze)

        while guard_in_bounds:
            guard_character = maze[guard_location[0]][guard_location[1]]

            new_guard_location = step(guard_location, guard_character)
            if new_guard_location[0] < 0 or new_guard_location[0] >= max_y or new_guard_location[1] < 0 or new_guard_location[1] >= max_x:
                guard_in_bounds = False
                continue

            location_character = maze[new_guard_location[0]][new_guard_location[1]]

            if maze[new_guard_location[0]][new_guard_location[1]] == '#':
                maze[guard_location[0]][guard_location[1]] = switch_direction(guard_character)
            else:
                maze[guard_location[0]][guard_location[1]] = '.'
                maze[new_guard_location[0]][new_guard_location[1]] = guard_character

                guard_location = new_guard_location

            if guard_location not in visited_positions:
                visited_positions.append(guard_location)

            cur_step += 1
        answer = len(visited_positions)

        return answer




def step(location, direction):
    if direction == '^':
        return (location[0] + -1, location[1] + 0)
    if direction == '>':
        return (location[0] + 0, location[1] + 1)
    if direction == 'v':
        return (location[0] + 1, location[1] + 0)
    if direction == '<':
        return (location[0] + 0, location[1] + -1)


def switch_direction(original_direction: str) -> str:
    if original_direction == '^':
        return '>'
    if original_direction == '>':
        return 'v'
    if original_direction == 'v':
        return '<'
    if original_direction == '<':
        return '^'


def part2(file_path):
    with open(file_path, 'r') as file:
        input_data = [list(line) for line in file.read().splitlines()]
        answer = 0

        optional_mazes = []
        for row in range(len(input_data)):
            for col in range(len(input_data[row])):
                if input_data[row][col] == '.':
                    new_maze = copy.deepcopy(input_data)
                    new_maze[row][col] = 'O'
                    optional_mazes.append(new_maze)

        for new_maze in optional_mazes:
            # guard_location is a tuple Y, X
            guard_location = (-1, -1)
            guard_character = '^'
            # obstacles is a list of tuples Y,X
            obstacles = []
            max_y = len(new_maze)
            max_x = len(new_maze[0])

            for row in range(len(new_maze)):
                for col in range(len(new_maze[row])):
                    if new_maze[row][col] == '^':
                        guard_location = (row, col)
                    if new_maze[row][col] == '#':
                        obstacles.append((row, col))
            visited_positions = [guard_location]
            guard_in_bounds = True

            maze = new_maze

            max_steps = 10000
            cur_step = 1

            while guard_in_bounds:
                guard_character = maze[guard_location[0]][guard_location[1]]

                new_guard_location = step(guard_location, guard_character)
                if new_guard_location[0] < 0 or new_guard_location[0] >= max_y or new_guard_location[1] < 0 or \
                        new_guard_location[1] >= max_x:
                    guard_in_bounds = False
                    continue

                location_character = maze[new_guard_location[0]][new_guard_location[1]]

                if maze[new_guard_location[0]][new_guard_location[1]] == '#' or maze[new_guard_location[0]][new_guard_location[1]] == 'O':
                    maze[guard_location[0]][guard_location[1]] = switch_direction(guard_character)
                else:
                    maze[guard_location[0]][guard_location[1]] = '.'
                    maze[new_guard_location[0]][new_guard_location[1]] = guard_character

                    guard_location = new_guard_location

                if cur_step >= max_steps:
                    # Not going out of bounds, count it!
                    answer += 1
                    guard_in_bounds = False
                cur_step += 1

        return answer


print("Part 1: ", part1('input.txt'))
print("Part 2: ", part2('input.txt'))
