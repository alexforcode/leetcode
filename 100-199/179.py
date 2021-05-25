"""
Given a list of non-negative integers nums, arrange them such that they form the largest number.

Note: The result may be very large, so you need to return a string instead of an integer.

Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 10**9
"""
from functools import cmp_to_key
from typing import List


def largest_number(nums: List[int]) -> str:
    def comparator(a: str, b: str) -> int:
        if a + b > b + a:
            return -1
        else:
            return 1

    strings: List[str] = list(map(str, nums))
    strings.sort(key=cmp_to_key(comparator))

    return str(int(''.join(strings)))


if __name__ == '__main__':
    assert largest_number([10, 2]) == '210'
    assert largest_number([3, 30, 34, 5, 9]) == '9534330'
    assert largest_number([1]) == '1'
    assert largest_number([10]) == '10'

