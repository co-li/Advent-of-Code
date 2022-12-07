import sys
from typing import Any, List, Tuple, Union


class FileTree:
    def __init__(self, parent: Union['FileTree', None]=None) -> None:
        self.parent = parent
        self.subdirs = {}
        self.filesize = 0
    
    def __repr__(self):
        return f'FileTree(subdirs=({self.subdirs}), filesize={self.filesize})'

    def add_subdirs(self, subdirs: List[str]):
        for subdir in subdirs:
            self.subdirs[subdir] = FileTree(self)

    def get_dirs_under_size(self, max_size: int) -> Tuple[int, int]:
        if len(self.subdirs) == 0:
            if self.filesize <= max_size:
                return self.filesize, self.filesize
            return self.filesize, 0
        total_size = self.filesize
        subdirs_under_size = 0
        for subdir in self.subdirs.values():
            subdir_size, under_size = subdir.get_dirs_under_size(max_size)
            total_size += subdir_size
            subdirs_under_size += under_size
        if total_size <= max_size:
            return total_size, subdirs_under_size + total_size
        return total_size, subdirs_under_size

    def get_min_dir_above_size(self, min_size: int) -> Tuple[int, int]:
        min_dir_above_size = sys.maxsize
        total_size = self.filesize
        for subdir in self.subdirs.values():
            subdir_size, above_size = subdir.get_min_dir_above_size(min_size)
            min_dir_above_size = min(min_dir_above_size, above_size)
            total_size += subdir_size
        if total_size >= min_size:
            min_dir_above_size = min(min_dir_above_size, total_size)
        return total_size, min_dir_above_size


def build_filetree(puzzle_input: List[str]) -> 'FileTree':
    dir_root = FileTree()
    dir_root.add_subdirs(['/'])
    cur_dir = dir_root
    i = 0
    while i < len(puzzle_input):
        line = puzzle_input[i]
        if line.startswith('$ cd'):
            next_dir = line.split()[-1]
            if next_dir == '..':
                if cur_dir.parent is not None:
                    cur_dir = cur_dir.parent
                else:
                    print("Error: reached parent of NoneType")
                    return dir_root
            else:
                cur_dir = cur_dir.subdirs[next_dir]
        elif line.startswith('$ ls'):
            subdirs = []
            dir_size = 0
            while i + 1 < len(puzzle_input) and puzzle_input[i+1][0] != '$':
                i += 1
                line = puzzle_input[i].split()
                if line[0] == 'dir':
                    subdir_name = line[1]
                    subdirs.append(subdir_name)
                else:
                    dir_size += int(line[0])
            cur_dir.filesize = dir_size
            cur_dir.add_subdirs(subdirs)
        i += 1
    return dir_root


def part_one(puzzle_input: List[str]) -> int:
    filetree = build_filetree(puzzle_input)
    _, soln = filetree.get_dirs_under_size(100000)
    return soln


def part_two(puzzle_input: List[Any]) -> int:
    filetree = build_filetree(puzzle_input)
    total_size, _ = filetree.get_min_dir_above_size(0)
    cur_free = 70000000 - total_size
    _, soln = filetree.get_min_dir_above_size(30000000 - cur_free)
    return soln


def main(puzzle_input: List[Any]):
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == '__main__':
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        file_input = [line.strip() for line in f]

    main(file_input)
