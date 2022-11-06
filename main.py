with open(file='data.txt') as file:
    coordinates = [line.split(" -> ") for line in file.read().split("\n")]


def find_diagonal_route(x1, y1, x2, y2):
    min_y, max_y = min(y1, y2), max(y1, y2)
    max_x, min_x = max(x1, x2), min(x1, x2)
    example_one, example_two = [], []  # different diagonal templates

    for y in range(max_y, min_y - 1, -1):
        example_one.append((min_x, y))
        min_x += 1
    if (x1, y1) in example_one and (x2, y2) in example_one:
        return example_one

    max_x, min_x = max(x1, x2), min(x1, x2)

    for x in range(max_x, min_x - 1, -1):
        example_two.append((x, max_y))
        max_y -= 1
    if (x1, y1) in example_two and (x2, y2) in example_two:
        return example_two


def find_routes(find_diagonal):
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    converging_lines = 0
    for entry in coordinates:
        x1, y1 = map(int, entry[0].split(","))
        x2, y2 = map(int, entry[1].split(","))

        if x1 == x2:  # HORIZONTAL
            max_y, min_y = max(y1, y2), min(y1, y2)
            for y in range(min_y, max_y + 1):
                grid[y][x1] += 1
                if grid[y][x1] == 2:
                    converging_lines += 1

        elif y1 == y2:  # VERTICAL
            max_y, min_y = max(x1, x2), min(x1, x2)
            for x in range(min_y, max_y + 1):
                grid[y1][x] += 1
                if grid[y1][x] == 2:
                    converging_lines += 1

        else:  # DIAGONAL
            if find_diagonal:
                route = find_diagonal_route(x1, y1, x2, y2)
                print("entry:", entry, "route", route)
                for coord in route:
                    x, y = coord[0], coord[1]
                    grid[y][x] += 1
                    if grid[y][x] == 2:
                        converging_lines += 1

    print("converging lines:", converging_lines)


# part one:
find_routes(False)
# part two:
find_routes(True)
