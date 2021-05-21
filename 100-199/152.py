"""
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product,
and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

Constraints:
    1 <= nums.length <= 2 * 10**4
    -10 <= nums[i] <= 10
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""
from typing import List, Union


def max_product(nums: List[int]) -> int:
    largest_prod: Union[float, int] = float('-inf')
    most_neg: int = 1
    most_pos: int = 1

    for num in nums:
        most_pos, most_neg = max(num, most_pos * num, most_neg * num), min(num, most_pos * num, most_neg * num)
        largest_prod = max(largest_prod, most_pos, most_neg)

    return largest_prod


if __name__ == '__main__':
    assert max_product([2, 3, -2, 4]) == 6
    assert max_product([-2, 0, -1]) == 0
