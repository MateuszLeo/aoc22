with open("./input.txt") as f:
    xss = []
    xs = []
    while line := f.readline():
        x = line.strip()
        if not x:
            xss.append(xs)
            xs = []
            continue
        xs.append(int(x))
    xs = [sum(xs) for xs in xss]
    x = max(xs)
    print("1", x)
    xs = sorted(xs)[-3:]
    x = sum(xs)
    print("2", x)
