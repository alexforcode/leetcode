"""
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

Constraints:
    1 <= num1.length, num2.length <= 10**4
    num1 and num2 consist of only digits.
    num1 and num2 don't have any leading zeros except for the zero itself.

Follow up: Could you solve it without using any built-in BigInteger library or
converting the inputs to integer directly?
"""
from typing import List


def add_strings(num1: str, num2: str) -> str:
    result: List[str] = []
    carry: int = 0
    p1: int = len(num1) - 1
    p2: int = len(num2) - 1

    while p1 >= 0 or p2 >= 0:
        cur_sum: int = carry
        if p1 >= 0:
            cur_sum += ord(num1[p1]) - ord('0')
            p1 -= 1
        if p2 >= 0:
            cur_sum += ord(num2[p2]) - ord('0')
            p2 -= 1
        result.append(str(cur_sum % 10))
        carry = cur_sum // 10

    if carry:
        result.append(str(carry))

    return ''.join(result[::-1])


if __name__ == '__main__':
    assert add_strings('11', '123') == '134'
    assert add_strings('456', '77') == '533'
    assert add_strings('0', '0') == '0'
