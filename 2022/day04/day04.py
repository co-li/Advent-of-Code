import sys
from typing import Any, List


def part_one(puzzle_input: List[Any]) -> int:
    soln = 0
    for pair1, pair2 in puzzle_input:
        if pair1[0] <= pair2[0] <= pair2[1] <= pair1[1] or pair2[0] <= pair1[0] <= pair1[1] <= pair2[1]:
            soln += 1
    return soln


def part_two(puzzle_input: List[Any]) -> int:
    soln = 0
    for pair1, pair2 in puzzle_input:
        if pair1[0] <= pair2[0] <= pair1[1] or pair2[0] <= pair1[0] <= pair2[1]:
            soln += 1
    return soln


def main(puzzle_input: List[Any]):
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == '__main__':
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        file_input = [[[int(num) for num in section.split('-')] for section in line.strip().split(',')] for line in f]

    main(file_input)
