"""
Given an array nums of n integers and an integer target,
find three integers in nums such that the sum is closest to target.[-1,2,1,-4]
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Constraints:
    3 <= nums.length <= 10^3
    -10^3 <= nums[i] <= 10^3
    -10^4 <= target <= 10^4
"""
from typing import List


def three_sum_closest(nums: List[int], target: int) -> int:
    total: int = nums[0] + nums[1] + nums[2]
    nums.sort()

    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            cur_total = nums[i] + nums[left] + nums[right]
            if cur_total > target:
                right -= 1
            else:
                left += 1

            if abs(cur_total - target) < abs(total - target):
                total = cur_total

    return total


if __name__ == '__main__':
    assert three_sum_closest([-1, 2, 1, -4], 1) == 2
