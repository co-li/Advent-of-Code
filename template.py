import sys
from typing import Any, List


def part_one(puzzle_input: List[Any]) -> int:
    return 0


def part_two(puzzle_input: List[Any]) -> int:
    return 0


def main(puzzle_input: List[Any]):
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == '__main__':
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        file_input = [line.strip() for line in f]

    main(file_input)
