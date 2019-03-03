from collections import defaultdict
from z3 import Int, Solver


def get_surrounds(grid, x, y, width, height):
    s = [
        grid[x + dx][y + dy]
        for dx in range(-1, 2)
        for dy in range(-1, 2)
        if x + dx >= 0 and x + dx < width and y + dy >= 0 and y + dy < height
    ]
    print(s)
    return s


def main():
    print("Please enter width:")
    width = int(input())
    print("Please enter height:")
    height = int(input())
    grid = [[Int(f"m_{x}_{y}") for y in range(height)] for x in range(width)]
    solver = Solver()
    for x in range(width):
        for y in range(height):
            solver.add(grid[x][y] >= 0)
            solver.add(grid[x][y] <= 1)
    print("Please enter hints:")
    print("Enter 3 integers (x, y, num) in one line")
    print("x: [1, width]")
    print("y: [1, height]")
    print("num: [1, 8]")
    print("-1 for terminate")
    inputs = defaultdict(dict)
    while True:
        line = input()
        if line == "-1":
            break
        else:
            vals = line.split()
            x = int(vals[0]) - 1
            y = int(vals[1]) - 1
            nums = int(vals[2])
            inputs[x][y] = nums
            assert (nums >= 1) and (nums <= 8)
            solver.add(grid[x][y] == 0)
            surrounds = get_surrounds(grid, x, y, width, height)
            solver.add(sum(surrounds) == nums)
    solver.check()
    model = solver.model()
    for y in range(height):
        for x in range(width):
            if y in inputs[x]:
                print(inputs[x][y], end=" ")
            elif model[grid[x][y]] == 0:
                print(".", end=" ")
            else:
                print("X", end=" ")
        print()


if __name__ == "__main__":
    main()
