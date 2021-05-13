"""
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list,
and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Constraints:
    1 <= digits.length <= 100
    0 <= digits[i] <= 9
"""
from typing import List


def plus_one(digits: List[int]) -> List[int]:
    carry: int = 0
    digits[-1] += 1

    for i in range(len(digits)-1, -1, -1):
        digits[i] += carry
        carry = digits[i] // 10
        digits[i] %= 10

    if carry:
        digits.insert(0, carry)

    return digits


if __name__ == '__main__':
    assert plus_one([1, 2, 3]) == [1, 2, 4]
    assert plus_one([0]) == [1]
    assert plus_one([9]) == [1, 0]
    assert plus_one([9, 9, 9]) == [1, 0, 0, 0]
