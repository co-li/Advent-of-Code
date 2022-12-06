import sys
from typing import Any, List


def find_distinct_chars(s: str, d: int) -> int:
    for i in range(0, len(s) - d):
        if len(set(s[i:i+d])) == d:
            return i+d
    return -1


def part_one(puzzle_input: List[Any]) -> int:
    return find_distinct_chars(puzzle_input[0], 4)


def part_two(puzzle_input: List[Any]) -> int:
    return find_distinct_chars(puzzle_input[0], 14)


def main(puzzle_input: List[Any]):
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == '__main__':
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        file_input = [line.strip() for line in f]

    main(file_input)
