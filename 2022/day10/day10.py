import sys
from typing import Any, List


def part_one(puzzle_input: List[Any]) -> int:
    soln = 0
    reg = 1
    cycle = 0
    for line in puzzle_input:
        cycle += 1
        if (cycle - 20) % 40 == 0:
            soln += cycle * reg
        if line[0] == 'addx':
            cycle += 1
            if (cycle - 20) % 40 == 0:
                soln += cycle * reg
            reg += int(line[1])
    return soln


def part_two(puzzle_input: List[Any]) -> int:
    crt = ['.'] * 240
    reg = 1
    cycle = 0
    draw_set = ([reg-1, reg, reg+1])
    for line in puzzle_input:
        if cycle % 40 in draw_set:
            crt[cycle] = '#'
        cycle += 1
        if cycle % 40 in draw_set:
            crt[cycle] = '#'
        if line[0] == 'addx':
            cycle += 1
            reg += int(line[1])
            draw_set = ([reg-1, reg, reg+1])

    for i in range(0,len(crt),40):
        for char in crt[i:i+40]:
            print(char, end='')
        print()
    return 0


def main(puzzle_input: List[Any]):
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == '__main__':
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        file_input = [line.strip().split() for line in f]

    main(file_input)
