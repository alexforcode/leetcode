"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
vertically neighboring. The same letter cell may not be used more than once.

Constraints:
    m == board.length
    n = board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
    board and word consists of only lowercase and uppercase English letters.

Follow up: Could you use search pruning to make your solution faster with a larger board?
"""
from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    rows: int = len(board)
    cols: int = len(board[0])

    def can_find(idx: int, row: int, col: int):
        if idx >= len(word):
            return True

        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            return False

        if word[idx] != board[row][col]:
            return False

        board[row][col] = '*'

        if can_find(idx+1, row+1, col) or can_find(idx+1, row-1, col) or can_find(idx+1, row, col+1) or \
                can_find(idx+1, row, col-1):
            return True

        board[row][col] = word[idx]

        return False

    for row in range(rows):
        for col in range(cols):
            if can_find(0, row, col):
                return True

    return False


if __name__ == '__main__':
    assert exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCCED') is True
    assert exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'SEE') is True
    assert exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCB') is False
