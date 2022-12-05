import sys
import re
from typing import Any, Dict, List, Tuple


def parse_input(puzzle_input: List[str]) -> Tuple[Dict[int, List[Any]], List[Any]]:
    crates = {i: [] for i in range(1, len(puzzle_input[0]) // 4 + 1)}
    moves = []
    moves_line = 0
    for i, line in enumerate(puzzle_input):
        if line.strip().split()[0].isdigit():
            moves_line = i + 2
            break
        for j, char in enumerate(line[1::4], 1):
            if char != ' ':
                crates[j].insert(0, char)
    for line in puzzle_input[moves_line:]:
        moves.append(map(int, re.findall(r'\d+', line)))
    return crates, moves

    
def part_one(puzzle_input: List[Any]) -> str:
    crates, moves = parse_input(puzzle_input)
    for count, start, end in moves:
        for i in range(count):
            crates[end].append(crates[start].pop())
    soln = ''
    for i in range(1, 10):
        if len(crates[i]) != 0:
            soln += crates[i][-1]
    return soln


def part_two(puzzle_input: List[Any]) -> str:
    crates, moves = parse_input(puzzle_input)
    for count, start, end in moves:
        crates[end].extend(crates[start][-count:])
        crates[start] = crates[start][:-count]
    soln = ''
    for i in range(1, 10):
        if len(crates[i]) != 0:
            soln += crates[i][-1]
    return soln


def main(puzzle_input: List[Any]):
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == '__main__':
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        file_input = [line for line in f]

    main(file_input)
