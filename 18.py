"""
Given an array nums of n integers and an integer target,
are there elements a, b, c, and d in nums such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

Notice that the solution set must not contain duplicate quadruplets.

Constraints:
    0 <= nums.length <= 200
    -10**9 <= nums[i] <= 10**9
    -10**9 <= target <= 10**9
"""
from typing import List, Optional


def two_sum(nums: List[int], target: int) -> List[List[int]]:
    result: List[List[int]] = []
    low: int = 0
    high: int = len(nums) - 1

    while low < high:
        total: int = nums[low] + nums[high]
        if total < target or (low > 0 and nums[low] == nums[low-1]):
            low += 1
        elif total > target or (high < len(nums) - 1 and nums[high] == nums[high+1]):
            high -= 1
        else:
            result.append([nums[low], nums[high]])
            low += 1
            high -= 1

    return result


def k_sum(nums: List[int], target: int, k: int) -> Optional[List[List[int]]]:
    result: List[List[int]] = []

    if not nums or nums[0] * k > target or target > nums[-1] * k:
        return result

    if k == 2:
        return two_sum(nums, target)

    for i in range(len(nums)):
        if i == 0 or nums[i-1] != nums[i]:
            for _, lst in enumerate(k_sum(nums[i+1:], target-nums[i], k-1)):
                result.append([nums[i]] + lst)

    return result


def four_sum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()

    return k_sum(nums, target, 4)


if __name__ == '__main__':
    assert four_sum([1, 0, -1, 0, -2, 2], 0) == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    assert four_sum([], 0) == []
