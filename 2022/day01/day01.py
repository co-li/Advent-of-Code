import sys
from typing import Any, List


def part_one(puzzle_input: List[Any]) -> int:
    cur_cal, max_cal = 0, 0
    for line in puzzle_input:
        if line != '':
            cur_cal += int(line)
        else:
            max_cal = max(max_cal, cur_cal)
            cur_cal = 0
    return max_cal


def part_two(puzzle_input: List[Any]) -> int:
    cur_cal = 0
    cal_list = []
    for line in puzzle_input:
        if line != '':
            cur_cal += int(line)
        else:
            cal_list.append(cur_cal)
            cur_cal = 0
    cal_list.sort(reverse=True)
    return sum(cal_list[0:3])


def main(puzzle_input: List[Any]):
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == '__main__':
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        file_input = [line.strip() for line in f]

    main(file_input)
