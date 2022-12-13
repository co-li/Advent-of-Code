import sys
from typing import Any, List, Tuple


def sgn(num: float) -> int:
    if num == 0:
        return 0
    if num > 0:
        return 1
    return -1


def move_knot(a: Tuple[int, int], b: Tuple[int, int]) -> Tuple[int, int]:
    dist = (a[0] - b[0], a[1] - b[1])
    if abs(dist[0]) > 1 or abs(dist[1]) > 1:
        return (b[0] + sgn(dist[0]), b[1] + sgn(dist[1]))
    return b


def part_one(puzzle_input: List[Any]) -> int:
    head = (0, 0)
    tail = (0, 0)
    dir_map = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    visited_set = set()
    for d, units in puzzle_input:
        move = dir_map[d]
        for _ in range(int(units)):
            head = (head[0] + move[0], head[1] + move[1])
            tail = move_knot(head, tail)
            visited_set.add(tail)
    return len(visited_set)


def part_two(puzzle_input: List[Any]) -> int:
    knots: List[Tuple[int, int]] = [(0, 0) for _ in range(10)]
    dir_map = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    visited_set = set()
    for d, units in puzzle_input:
        move = dir_map[d]
        for _ in range(int(units)):
            knots[0] = (knots[0][0] + move[0], knots[0][1] + move[1])
            for i in range(len(knots) - 1):
                knots[i+1] = move_knot(knots[i], knots[i+1])
            visited_set.add(knots[-1])
    return len(visited_set)


def main(puzzle_input: List[Any]):
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == '__main__':
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        file_input = [line.strip().split() for line in f]

    main(file_input)
