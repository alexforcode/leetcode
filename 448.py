"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime?
You may assume the returned list does not count as extra space.
"""
from typing import List


def find_disappeared_numbers(nums: List[int]) -> List[int]:
    for num in nums:
        idx: int = abs(num) - 1
        nums[idx] = abs(nums[idx]) * -1

    return [idx+1 for idx, val in enumerate(nums) if val > 0]


if __name__ == '__main__':
    assert find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
