from typing import List


def part1(p1, p2):
    (x1, y1), (x2, y2) = p1, p2
    return (x1 <= x2 and y1 >= y2) or (x2 <= x1 and y1 <= y2)


def part2(p1, p2):
    (x1, y1), (x2, y2) = p1, p2
    return (x1 <= x2 <= y1) or (x2 <= x1 <= y2)


def parse(xs: List[str]):
    [x, y] = [int(x) for x in xs.split("-")]
    return x, y


with open("./input.txt") as f:
    xss = []
    while line := f.readline():
        l = line.strip()
        r1, r2 = l.split(",")
        xss.append((parse(r1), parse(r2)))

    sol1 = sum([part1(p1, p2) for p1, p2 in xss])
    print("p1", sol1)

    sol2 = sum([part2(p1, p2) for p1, p2 in xss])
    print("p2", sol2)
