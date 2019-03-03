from z3 import Int, Solver, Distinct


def read_input():
    print("Enter input:")
    print("(Separate by space, 0 for unknown)")
    known = []
    for _ in range(9):
        line = input().split()
        if len(line) != 9:
            raise RuntimeError("Invalid input")
        known.append([int(x) for x in line])
    return known


def main(known):
    s = Solver()
    matrix = [[Int(f"m{x}{y}") for x in range(1, 10)] for y in range(1, 10)]
    for i in range(9):
        for j in range(9):
            v = matrix[i][j]
            if known[i][j]:
                s.add(v == known[i][j])
            else:
                s.add(v >= 1)
                s.add(v <= 9)
    for i in range(9):
        s.add(Distinct(*[matrix[i][j] for j in range(9)]))
        s.add(Distinct(*[matrix[j][i] for j in range(9)]))
    for i in range(3):
        for j in range(3):
            s.add(
                Distinct(
                    *[matrix[3 * i + k][3 * j + l] for k in range(3) for l in range(3)]
                )
            )
    s.check()
    m = s.model()
    print("Solution:")
    for i in range(9):
        print(*[m[matrix[i][j]] for j in range(9)])


if __name__ == "__main__":
    known = read_input()
    main(known)
