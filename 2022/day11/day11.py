import sys
import re
from typing import Any, List, Tuple


def get_op_lambda(op_str: str):
    if op_str.count('old') == 1:
        if op_str.count('*'):
            return lambda x: x * int(re.findall(r'\d+', op_str)[0])
        else:
            return lambda x: x + int(re.findall(r'\d+', op_str)[0])
    else:
        if op_str.count('*'):
            return lambda x: x * x
        else:
            return lambda x: x + x


def get_divisible_lambda(factor: int, t_ret: int, f_ret: int):
    return lambda x: t_ret if x % factor == 0 else f_ret


def parse_input(puzzle_input: List[str]) -> Tuple[List[Any], int]:
    monkey_list = []
    factor_multiple = 1
    monkey_attributes = []
    i = 0
    while i < len(puzzle_input):
        line = puzzle_input[i]
        if line.startswith('Starting items:'):
            monkey_attributes.append(list(map(int, re.findall(r'\d+', line))))
        elif line.startswith('Operation:'):
            op_lambda = get_op_lambda(line)
            monkey_attributes.append(op_lambda)
        elif line.startswith('Test:'):
            div = int(re.findall(r'\d+', line)[0])
            factor_multiple *= div
            i += 1
            line = puzzle_input[i]
            true_cond = int(re.findall(r'\d+', line)[0])
            i += 1
            line = puzzle_input[i]
            false_cond = int(re.findall(r'\d+', line)[0])
            test_lambda = get_divisible_lambda(div, true_cond, false_cond)
            monkey_attributes.append(test_lambda)
            monkey_list.append(monkey_attributes)
            monkey_attributes = []
        i += 1
    return monkey_list, factor_multiple


def part_one(puzzle_input: List[str]) -> int:
    monkey_list, _ = parse_input(puzzle_input)
    monkey_count = [0] * len(monkey_list)
    for _ in range(20):
        for i, monkey in enumerate(monkey_list):
            for element in monkey[0]:
                new = monkey[1](element)//3
                next_monkey = monkey[2](new)
                monkey_list[next_monkey][0].append(new)
            monkey_count[i] += len(monkey[0])
            monkey[0] = []
    monkey_count.sort(reverse=True)
    return monkey_count[0]*monkey_count[1]


def part_two(puzzle_input: List[str]) -> int:
    monkey_list, factor_multiple = parse_input(puzzle_input)
    monkey_count = [0] * len(monkey_list)
    for _ in range(10000):
        for i, monkey in enumerate(monkey_list):
            for element in monkey[0]:
                new = monkey[1](element) % factor_multiple
                next_monkey = monkey[2](new)
                monkey_list[next_monkey][0].append(new)
            monkey_count[i] += len(monkey[0])
            monkey[0] = []
    monkey_count.sort(reverse=True)
    return monkey_count[0]*monkey_count[1]



def main(puzzle_input: List[str]):
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == '__main__':
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        file_input = [line.strip() for line in f]

    main(file_input)
