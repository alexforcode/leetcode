"""
Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions,
such as eval().

Constraints:
    1 <= s.length <= 3 * 10**5
    s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
    s represents a valid expression.
    All the integers in the expression are non-negative integers in the range [0, 2**31 - 1].
    The answer is guaranteed to fit in a 32-bit integer.
"""
from typing import List


def calculate(s: str) -> int:
    stack: List[int] = []
    num: int = 0
    operator: str = '+'

    for idx, char in enumerate(s):
        if char.isdigit():
            num = num * 10 + int(char)

        if (not char.isdigit() and char != ' ') or idx == len(s) - 1:
            if operator == '+':
                stack.append(num)
            elif operator == '-':
                stack.append(-num)
            elif operator == '*':
                stack.append(stack.pop() * num)
            else:
                left: int = stack.pop()
                stack.append(left // num)

                if left // num < 0 and left % num != 0:
                    stack[-1] += 1

            num = 0
            operator = char

    return sum(stack)


if __name__ == '__main__':
    assert calculate('3+2*2') == 7
    assert calculate(' 3/2 ') == 1
    assert calculate(' 3+5 / 2 ') == 5
