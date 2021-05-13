"""
Given a string containing just the characters '(' and ')',
find the length of the longest valid (well-formed) parentheses substring.

Constraints:
    0 <= s.length <= 3 * 104
    s[i] is '(', or ')'.
"""
from typing import Deque
from collections import deque


def longest_valid_parentheses(s: str) -> int:
    if not s:
        return 0

    stack: Deque[int] = deque()
    cur_max: int = 0

    stack.append(-1)

    for index, char in enumerate(s):
        if char == '(':
            stack.append(index)
        else:
            stack.pop()
            if not stack:
                stack.append(index)
            else:
                cur_max = max(cur_max, index-stack[-1])

    return cur_max


if __name__ == '__main__':
    assert longest_valid_parentheses('(()') == 2
    assert longest_valid_parentheses(')()())') == 4
    assert longest_valid_parentheses('') == 0
    assert longest_valid_parentheses('())((())') == 4
    assert longest_valid_parentheses('()(()') == 2
