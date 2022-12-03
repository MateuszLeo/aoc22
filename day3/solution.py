def to_int(c: str) -> int:
    x, y = 52, 'Z'
    if c.islower():
        x, y = 26, 'z'
    return x + ord(c) - ord(y)

def part1(xs, ys) -> int:
    intersection = set(xs) & set(ys)
    [fst] = intersection
    return to_int(fst)

def part2(xs, ys, zs):
    intersection = set(xs) & set(ys) & set(zs)
    [fst] = intersection
    return to_int(fst)
    
with open('./input.txt') as f:
    xss = []
    while line := f.readline():
        l = line.strip()
        char_count= len(l) 
        half = int(char_count / 2)
        fh, sh = l[0:half], l[half:]
        xss.append((fh, sh))
    
    print('1', sum([part1(fh, sh) for fh, sh in xss]))

    yss = []
    ys = []
    for xs in xss:
        ys.append(''.join(xs))
        if len(ys) == 3:
            yss.append(ys)
            ys = []

    print('2', sum([part2(fh, sh, th) for fh, sh, th in yss]))
    