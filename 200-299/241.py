"""
Given a string expression of numbers and operators, return all possible results from computing
all the different possible ways to group numbers and operators. You may return the answer in any order.

Constraints:
    1 <= expression.length <= 20
    expression consists of digits and the operator '+', '-', and '*'.
"""
from typing import Dict, List, Tuple, Union


def diff_ways_to_compute(expression: str) -> List[int]:
    start: int = 0
    parsed: List[Union[int, str]] = []

    for idx in range(len(expression)):
        if not expression[idx].isdigit():
            parsed.append(int(expression[start:idx]))
            parsed.append(expression[idx])
            start = idx + 1

    parsed.append(int(expression[start:len(expression)]))

    def diff_ways(left: int, right: int, memo: Dict[Tuple[int, int], List[int]]) -> List[int]:
        if left == right:
            return [parsed[left]]

        if (left, right) in memo:
            return memo[(left, right)]

        ways: List[int] = []

        for idx in range(left + 1, right, 2):
            left_res: List[int] = diff_ways(left, idx - 1, memo)
            right_res: List[int] = diff_ways(idx + 1, right, memo)

            for l in left_res:
                for r in right_res:
                    if parsed[idx] == '+':
                        ways.append(l + r)
                    elif parsed[idx] == '-':
                        ways.append(l - r)
                    elif parsed[idx] == '*':
                        ways.append(l * r)

        memo[(left, right)] = ways

        return ways

    return diff_ways(0, len(parsed) - 1, {})


if __name__ == '__main__':
    print(diff_ways_to_compute('2-1-1'))  # [0, 2]
    print(diff_ways_to_compute('2*3-4*5'))  # [-34, -14, -10, -10, 10]
