import sys
from typing import Any, List


def part_one(puzzle_input: List[Any]) -> int:
    soln = 2 * (len(puzzle_input) + len(puzzle_input[0])) - 4
    visible_set = set()
    for i, row in enumerate(puzzle_input[1:-1], 1):
        left_max = int(row[0])
        for j, col in enumerate(row[1:-1], 1):
            if int(col) > left_max:
                visible_set.add((i, j))
                left_max = int(col)
        right_max = int(row[-1])
        for j, col in reversed(list(enumerate(row[1:-1], 1))):
            if int(col) > right_max:
                visible_set.add((i, j))
                right_max = int(col)
    for j, col in enumerate(puzzle_input[0][1:-1], 1):
        top_max = int(col)
        for i, row in enumerate(puzzle_input[1:-1], 1):
            height = int(row[j])
            if height > top_max:
                visible_set.add((i, j))
                top_max = height
    for j, col in enumerate(puzzle_input[-1][1:-1], 1):
        bottom_max = int(col)
        for i, row in reversed(list(enumerate(puzzle_input[1:-1], 1))):
            height = int(row[j])
            if height > bottom_max:
                visible_set.add((i, j))
                bottom_max = height
    soln += len(visible_set)
    return soln


def part_two(puzzle_input: List[Any]) -> int:
    score = 0
    directions = {(-1, 0), (0, -1), (0, 1), (1, 0)}
    for i, row in enumerate(puzzle_input[1:-1], 1):
        for j, col in enumerate(row[1:-1], 1):
            base_score = 1
            cur_height = int(col)
            for d in directions:
                dir_score = 0
                c = (i + d[0], j + d[1])
                if int(puzzle_input[c[0]][c[1]]) < cur_height:
                    while 0 <= c[0] < len(puzzle_input) and 0 <= c[1] < len(puzzle_input[0]):
                        dir_score += 1
                        if int(puzzle_input[c[0]][c[1]]) >= cur_height:
                            break
                        c = (c[0] + d[0], c[1] + d[1])
                base_score *= dir_score
            score = max(score, base_score)
    return score


def main(puzzle_input: List[Any]):
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == '__main__':
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        file_input = [line.strip() for line in f]

    main(file_input)
