def to_int(c: str) -> int:
    x, y = 52, "Z"
    if c.islower():
        x, y = 26, "z"
    return x + ord(c) - ord(y)


def part1(xs, ys) -> int:
    intersection = set(xs) & set(ys)
    [fst] = intersection
    return to_int(fst)


def part2(xs, ys, zs):
    intersection = set(xs) & set(ys) & set(zs)
    [fst] = intersection
    return to_int(fst)


with open("./input.txt") as f:
    xss = []
    while line := f.readline():
        l = line.strip()
        xss.append(l)

    part1_data = []
    for xs in xss:
        char_count = len(xs)
        half = int(char_count / 2)
        fh, sh = xs[0:half], xs[half:]
        part1_data.append((fh, sh))

    print("1", sum([part1(fh, sh) for fh, sh in part1_data]))

    yss = []
    ys = []
    for xs in xss:
        ys.append(xs)
        if len(ys) == 3:
            yss.append(ys)
            ys = []

    print("2", sum([part2(fh, sh, th) for fh, sh, th in yss]))
