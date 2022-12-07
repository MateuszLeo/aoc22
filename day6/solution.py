def find_marker(stream: str, size: int):
    for cursor, _ in enumerate(stream):
        start, end = cursor, cursor + size
        if len(set(c[start:end])) == size:
            return end


START_OF_PACKET_SIZE = 4
MESSAGE_PACKET_SIZE = 14

with open("./input.txt") as f:
    c = f.read()

    print("p1", find_marker(c, START_OF_PACKET_SIZE))
    print("p2", find_marker(c, MESSAGE_PACKET_SIZE))
