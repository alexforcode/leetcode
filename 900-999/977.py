"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number
sorted in non-decreasing order.

Constraints:
    1 <= nums.length <= 10**4
    -10**4 <= nums[i] <= 10**4
    nums is sorted in non-decreasing order.

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution
using a different approach?
"""
from typing import List, Optional


def sorted_squares_1(nums: List[int]) -> List[int]:
    pos_point: int = 0

    while pos_point < len(nums) and nums[pos_point] <= 0:
        pos_point += 1

    neg_point: int = pos_point - 1
    squared: List[int] = []

    while neg_point >= 0 and pos_point < len(nums):
        if nums[neg_point] ** 2 < nums[pos_point] ** 2:
            squared.append(nums[neg_point] ** 2)
            neg_point -= 1
        else:
            squared.append(nums[pos_point] ** 2)
            pos_point += 1

    while neg_point >= 0:
        squared.append(nums[neg_point] ** 2)
        neg_point -= 1

    while pos_point < len(nums):
        squared.append(nums[pos_point] ** 2)
        pos_point += 1

    return squared


def sorted_squares_2(nums: List[int]) -> List[int]:
    squared: List[Optional[int]] = [None] * len(nums)
    left: int = 0
    right: int = len(nums) - 1

    for idx in range(len(nums)-1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            squared[idx] = nums[left]**2
            left += 1
        else:
            squared[idx] = nums[right]**2
            right -= 1

    return squared


if __name__ == '__main__':
    assert sorted_squares_1([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    assert sorted_squares_1([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
    assert sorted_squares_1([-1]) == [1]
    assert sorted_squares_1([1]) == [1]

    assert sorted_squares_2([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    assert sorted_squares_2([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
    assert sorted_squares_2([-1]) == [1]
    assert sorted_squares_2([1]) == [1]
