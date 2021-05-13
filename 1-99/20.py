"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
 - Open brackets must be closed by the same type of brackets.
 - Open brackets must be closed in the correct order.
"""
from collections import deque
from typing import Deque


def is_valid(s: str) -> bool:
    if len(s) % 2:
        return False

    stack: Deque[str] = deque()

    for char in s:
        if char in ('(', '[', '{'):
            stack.append(char)
        elif stack:
            if char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False
        else:
            return False

    return True if not stack else False


if __name__ == '__main__':
    assert is_valid('()') is True
    assert is_valid('()[]{}') is True
    assert is_valid('(]') is False
    assert is_valid('([)]') is False
    assert is_valid('{[]}') is True
