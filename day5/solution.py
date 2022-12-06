import re
from collections import defaultdict
from copy import deepcopy
from dataclasses import dataclass
from typing import DefaultDict, List, Literal

move = r"^move\s(?P<n>\d+)\sfrom\s(?P<from>\d+)\sto\s(?P<to>\d+)"
stack_item = r"\[(\D)\]"
STACK_ITEM_SIZE = 3
SPACING_SIZE = 1


def parse_stack_items(tokens, stacks):
    n = 1
    omit_next = False

    while tokens:
        if omit_next:
            omit_next = False
            tokens = tokens[SPACING_SIZE:]
            continue

        token = tokens[:STACK_ITEM_SIZE]
        if m := re.match(stack_item, token):
            stacks[n].append(m.group(1))

        tokens = tokens[STACK_ITEM_SIZE:]
        n += 1
        omit_next = True


@dataclass
class Instruction:
    _n: int
    _from: int
    _to: int


Model = Literal["CrateMover 9001", "CrateMover 9000"]


@dataclass
class CrateMover:
    model: Model
    instructions: List[Instruction]
    stacks: List[DefaultDict[str, List[str]]]

    def move(self):
        for i in self.instructions:
            self._move_stacks(self.stacks, i)

    def move_stacks(self, stacks, i: Instruction):
        raise NotImplementedError()

    def __str__(self) -> str:
        keys = sorted(self.stacks)
        return "".join([self.stacks[k][0] for k in keys])


class CrateMover9000(CrateMover):
    def move_stacks(self, stacks, i: Instruction):
        for _ in range(i._n):
            item = stacks[i._from].pop(0)
            stacks[i._to].insert(0, item)


class CrateMover9001(CrateMover):
    def move_stacks(self, stacks, i: Instruction):
        items = stacks[i._from][0 : i._n]
        stacks[i._from] = stacks[i._from][i._n :]
        stacks[i._to] = items + stacks[i._to]


def parse(lines):
    stacks = defaultdict(list)
    instructions = []
    parsed = False

    for line in lines:
        if line == "\n" or re.match(r"\s+?\d\s+?", line):
            parsed = True
            continue

        if not parsed:
            parse_stack_items(line, stacks)
            continue

        if m := re.match(move, line):
            instructions.append(
                Instruction(
                    _n=int(m.group("n")),
                    _from=int(m.group("from")),
                    _to=int(m.group("to")),
                )
            )

    c9000 = CrateMover9000(
        model="CrateMover 9000",
        instructions=instructions,
        stacks=deepcopy(stacks),
    )
    c9000.move()
    print("1", c9000)

    c9001 = CrateMover9001(
        model="CrateMover 9001",
        instructions=instructions,
        stacks=deepcopy(stacks),
    )
    c9001.move()
    print("2", c9001)


with open("./input.txt") as f:
    parse(f.readlines())
