import sys
import heapq
from typing import Any, List, Tuple


def find_start(puzzle_input: List[str]) -> Tuple[int, int]:
    for i, line in enumerate(puzzle_input):
        for j, char in enumerate(line):
            if char == 'S':
                return (i, j)
    return (-1, -1)


def find_end(puzzle_input: List[str]) -> Tuple[int, int]:
    for i, line in enumerate(puzzle_input):
        for j, char in enumerate(line):
            if char == 'E':
                return (i, j)
    return (-1, -1)


def find_starts(puzzle_input: List[str]) -> List[Tuple[int, int]]:
    starts = []
    for i, line in enumerate(puzzle_input):
        for j, char in enumerate(line):
            if char == 'S' or char == 'a':
                starts.append((i, j))
    return starts


def heuristic(cur_pos: Tuple[int, int], goal: Tuple[int, int]) -> int:
    return abs(goal[0]-cur_pos[0]) + abs(goal[1]-cur_pos[1])


def a_star(search_heapq: List[Any], end: Tuple[int, int], puzzle_input: List[Any]) -> int:
    moves = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    visited = set()
    while len(search_heapq) > 0:
        _, cur, steps = heapq.heappop(search_heapq)
        if cur == end:
            return steps
        cur_letter = puzzle_input[cur[0]][cur[1]]
        cur_letter = 'a' if cur_letter == 'S' else cur_letter
        if cur in visited:
            continue
        visited.add(cur)
        for move in moves:
            next_pos = (cur[0] + move[0], cur[1] + move[1])
            if 0 <= next_pos[0] < len(puzzle_input) and 0 <= next_pos[1] < len(puzzle_input[0]):
                next_letter = puzzle_input[next_pos[0]][next_pos[1]]
                next_letter = 'z' if next_letter == 'E' else next_letter
                if next_pos not in visited and ord(next_letter) <= ord(cur_letter) + 1:
                    heapq.heappush(search_heapq, (steps+1+heuristic(next_pos, end), next_pos, steps+1))
    return -1


def part_one(puzzle_input: List[Any]) -> int:
    start, end = find_start(puzzle_input), find_end(puzzle_input)
    search_heapq = []
    heapq.heappush(search_heapq, (0, start, 0))
    return a_star(search_heapq, end, puzzle_input)


def part_two(puzzle_input: List[Any]) -> int:
    starts, end = find_starts(puzzle_input), find_end(puzzle_input)
    search_heapq = []
    for start in starts:
        heapq.heappush(search_heapq, (0, start, 0))
    return a_star(search_heapq, end, puzzle_input)


def main(puzzle_input: List[Any]):
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == '__main__':
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        file_input = [line.strip() for line in f]

    main(file_input)
