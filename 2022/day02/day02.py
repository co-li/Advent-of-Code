import sys
from typing import Any, List


def part_one(puzzle_input: List[Any]) -> int:
    letter_score = {'X': 1, 'Y': 2, 'Z': 3}
    win_score = {'lose': 0, 'tie': 3, 'win': 6}
    score_dict = {
        'A X': letter_score['X'] + win_score['tie'],
        'A Y': letter_score['Y'] + win_score['win'],
        'A Z': letter_score['Z'] + win_score['lose'],
        'B X': letter_score['X'] + win_score['lose'],
        'B Y': letter_score['Y'] + win_score['tie'],
        'B Z': letter_score['Z'] + win_score['win'],
        'C X': letter_score['X'] + win_score['win'],
        'C Y': letter_score['Y'] + win_score['lose'],
        'C Z': letter_score['Z'] + win_score['tie'],
    }
    score = 0
    for line in puzzle_input:
        score += score_dict[line]
    return score


def part_two(puzzle_input: List[Any]) -> int:
    letter_score = {'A': 1, 'B': 2, 'C': 3}
    win_score = {'X': 0, 'Y': 3, 'Z': 6}
    score_dict = {
        'A X': letter_score['C'] + win_score['X'],
        'A Y': letter_score['A'] + win_score['Y'],
        'A Z': letter_score['B'] + win_score['Z'],
        'B X': letter_score['A'] + win_score['X'],
        'B Y': letter_score['B'] + win_score['Y'],
        'B Z': letter_score['C'] + win_score['Z'],
        'C X': letter_score['B'] + win_score['X'],
        'C Y': letter_score['C'] + win_score['Y'],
        'C Z': letter_score['A'] + win_score['Z']
    }
    score = 0
    for line in puzzle_input:
        score += score_dict[line]
    return score


def main(puzzle_input: List[Any]):
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == '__main__':
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        file_input = [line.strip() for line in f]

    main(file_input)
