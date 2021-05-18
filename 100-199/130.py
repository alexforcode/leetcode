"""
Given an m x n matrix board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Constraints:
    m == board.length
    n == board[i].length
    1 <= m, n <= 200
    board[i][j] is 'X' or 'O'.
"""
from typing import List, Tuple


def solve(board: List[List[str]]) -> None:
    rows: int = len(board)
    cols: int = len(board[0])
    to_explore: List[Tuple[int, int]] = []

    for row in range(rows):
        to_explore += [(row, 0), (row, cols - 1)]
    for col in range(1, cols - 1):
        to_explore += [(0, col), (rows - 1, col)]

    while to_explore:
        row, col = to_explore.pop()

        if 0 <= row < rows and 0 <= col < cols and board[row][col] == 'O':
            board[row][col] = 'T'
            for drow, dcol in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                to_explore.append((row + drow, col + dcol))

    for row in range(rows):
        for col in range(cols):
            if board[row][col] == 'O':
                board[row][col] = 'X'
            elif board[row][col] == 'T':
                board[row][col] = 'O'


if __name__ == '__main__':
    matrix = [['X', 'X', 'X', 'X'],
              ['X', 'O', 'O', 'X'],
              ['X', 'X', 'O', 'X'],
              ['X', 'O', 'X', 'X']]
    solve(matrix)
    assert matrix == [['X', 'X', 'X', 'X'],
                      ['X', 'X', 'X', 'X'],
                      ['X', 'X', 'X', 'X'],
                      ['X', 'O', 'X', 'X']]

    matrix = [['X']]
    solve(matrix)
    assert matrix == [['X']]
