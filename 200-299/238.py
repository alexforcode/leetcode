"""
Given an integer array nums, return an array answer such that
answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Constraints:
    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up:
    Could you solve it in O(n) time complexity and without using division?
    Could you solve it with O(1) constant space complexity?
     (The output array does not count as extra space for space complexity analysis.)
"""
from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    result: List[int] = [0] * len(nums)

    result[0] = 1
    for i in range(1, len(nums)):
        result[i] = nums[i-1] * result[i-1]

    temp: int = 1
    for i in reversed(range(len(nums))):
        result[i] *= temp
        temp *= nums[i]

    return result


if __name__ == '__main__':
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
