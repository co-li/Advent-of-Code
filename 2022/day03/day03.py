import sys
from typing import Any, List


def get_priority(char: str):
    if char.isupper():
        return ord(char) - ord('A') + 27
    return ord(char) - ord('a') + 1


def part_one(puzzle_input: List[str]) -> int:
    priorities = 0
    for line in puzzle_input:
        length = len(line) // 2
        (shared_item,) = set(line[:length]).intersection(set(line[length:]))
        priorities += get_priority(shared_item)
    return priorities


def part_two(puzzle_input: List[str]) -> int:
    priorities = 0
    for line1, line2, line3 in zip(puzzle_input[::3], puzzle_input[1::3], puzzle_input[2::3]):
        (shared_item,) = set(line1).intersection(set(line2)).intersection(set(line3))
        priorities += get_priority(shared_item)
    return priorities


def main(puzzle_input: List[Any]):
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == '__main__':
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        file_input = [line.strip() for line in f]

    main(file_input)
