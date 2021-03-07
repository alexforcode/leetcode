"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Constraints:
    1 <= n <= 8
"""
from typing import List


def add_parenthesis(result: List[str], cur_str: str, cnt_open: int, cnt_close: int, max_pairs: int) -> None:
    if len(cur_str) == max_pairs * 2:
        result.append(cur_str)
        return

    if cnt_open < max_pairs:
        add_parenthesis(result, cur_str+'(', cnt_open+1, cnt_close, max_pairs)

    if cnt_close < cnt_open:
        add_parenthesis(result, cur_str+')', cnt_open, cnt_close+1, max_pairs)


def generate_parenthesis(n: int) -> List[str]:
    result: List[str] = []
    add_parenthesis(result, '', 0, 0, n)

    return result


if __name__ == '__main__':
    assert generate_parenthesis(3) == ['((()))', '(()())', '(())()', '()(())', '()()()']
    assert generate_parenthesis(1) == ['()']
