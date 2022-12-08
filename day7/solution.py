from dataclasses import dataclass
from typing import List, Optional, Tuple, Union, Callable


@dataclass
class Cmd:
    name: str
    args: str


@dataclass
class Dir:
    name: str


@dataclass
class File:
    name: str
    size: int


@dataclass
class Node:
    parent_node: Optional["Node"]
    value: Optional[Union[File, Dir]]
    edges: List["Node"]

    @property
    def size(self) -> int:
        if isinstance(self.value, Dir):
            return sum(edge.size for edge in self.edges)
        if isinstance(self.value, File):
            return self.value.size


class Tree(Node):
    ...


def create_tree(lines: List[str]) -> Tree:
    tree = Tree(value=None, parent_node=None, edges=[])
    current_dir = tree

    for line in lines:
        line = line.strip()
        match line.split():
            case ["$", "ls"]:
                ...
            case ["$", "cd", "/"]:
                current_dir.value = Dir(name="/")
            case ["$", "cd", ".."]:
                current_dir = current_dir.parent_node
            case ["$", "cd", dir_name]:
                current_dir = next(
                    edge for edge in current_dir.edges if edge.value.name == dir_name
                )
            case ["dir", dir_name]:
                current_dir.edges.append(
                    Node(parent_node=current_dir, value=Dir(name=dir_name), edges=[])
                )
            case [size, file_name]:
                current_dir.edges.append(
                    Node(
                        parent_node=current_dir,
                        value=File(name=file_name, size=int(size)),
                        edges=[],
                    )
                )
    return tree


def get_dir_sizes(tree: Tree) -> List[Tuple[Dir, int]]:
    sizes = []

    def get(node: Node):
        size = 0
        for edge in node.edges:
            size += edge.size
            if isinstance(edge.value, Dir):
                get(edge)
        sizes.append(size)
        return size

    get(tree)
    return sizes


with open("./input.txt") as f:
    tree = create_tree(f.readlines())

    MAX_SIZE = 100_000

    sizes = get_dir_sizes(tree)
    p1 = (size for size in sizes if size <= MAX_SIZE)
    print("p1", sum(p1))

    TOTAL = 70_000_000
    MIN_UNUSED = 30_000_000

    FREE = TOTAL - tree.size
    TO_FREE = MIN_UNUSED - FREE
    p2 = (size for size in sizes if size >= TO_FREE)
    print("p2", min(p2))
