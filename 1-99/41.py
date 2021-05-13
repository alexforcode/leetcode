"""
Given an unsorted integer array nums, find the smallest missing positive integer.

Constraints:
    0 <= nums.length <= 300
    -2**31 <= nums[i] <= 2**31 - 1

Follow up:
Could you implement an algorithm that runs in O(n) time and uses constant extra space?
"""
from typing import List


def first_missing_positive(nums: List[int]) -> int:
    # Time: O(n)
    # Space: O(1)

    if not nums or max(nums) < 1:
        return 1

    if len(nums) == 1:
        return 2 if nums[0] == 1 else 1

    step: int = 0
    for idx in range(len(nums)):
        if nums[idx] <= 0:
            nums[idx], nums[step] = nums[step], nums[idx]
            step += 1

    nums = nums[step:]

    for idx in range(len(nums)):
        abs_val: int = abs(nums[idx]) - 1
        if abs_val < len(nums) and nums[abs_val] > 0:
            nums[abs_val] = -nums[abs_val]

    for idx in range(len(nums)):
        if nums[idx] > 0:
            return idx + 1

    return len(nums) + 1


if __name__ == '__main__':
    assert first_missing_positive([1, 2, 0]) == 3
    assert first_missing_positive([3, 4, -1, 1]) == 2
    assert first_missing_positive([7, 8, 9, 11, 12]) == 1
