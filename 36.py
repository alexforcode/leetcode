"""
Determine if a 9 x 9 Sudoku board is valid.
Only the filled cells need to be validated according to the following rules:
    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.

Constraints:
    board.length == 9
    board[i].length == 9
    board[i][j] is a digit or '.'.
"""
from typing import List, Set


def add_to_seen(string: str, seen: Set[str]) -> bool:
    if string not in seen:
        seen.add(string)
        return True

    return False


def is_valid_sudoku(board: List[List[str]]) -> bool:
    seen: Set[str] = set()

    for row in range(9):
        for col in range(9):
            cur_char: str = board[row][col]
            if cur_char != '.':
                if not add_to_seen(f'{cur_char} in row {row}', seen):
                    return False
                if not add_to_seen(f'{cur_char} in col {col}', seen):
                    return False
                if not add_to_seen(f'{cur_char} in box [{row // 3}, {col // 3}]', seen):
                    return False

    return True


if __name__ == '__main__':
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    assert is_valid_sudoku(board) is True

    board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    assert is_valid_sudoku(board) is False
