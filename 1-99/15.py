"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

Constraints:
    0 <= nums.length <= 3000
    -105 <= nums[i] <= 105
"""
from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    result: List[List[int]] = []

    if len(nums) <= 2:
        return result

    nums.sort()

    for i in range(len(nums) - 2):
        if i == 0 or (i > 0 and nums[i] != nums[i-1]):
            low: int = i + 1
            high: int = len(nums) - 1
            total: int = 0 - nums[i]

            while low < high:
                if nums[low] + nums[high] == total:
                    result.append([nums[i], nums[low], nums[high]])
                    while low < high and nums[low] == nums[low+1]:
                        low += 1
                    while low < high and nums[high] == nums[high-1]:
                        high -= 1
                    low += 1
                    high -= 1
                elif nums[low] + nums[high] < total:
                    low += 1
                else:
                    high -= 1

    return result


if __name__ == '__main__':
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert three_sum([]) == []
    assert three_sum([0]) == []
    assert three_sum([0, 0]) == []
