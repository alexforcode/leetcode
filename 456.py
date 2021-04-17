"""
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k]
such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

Follow up: The O(n^2) is trivial, could you come up with the O(n logn) or the O(n) solution?

Constraints:
    n == nums.length
    1 <= n <= 10**4
    -10**9 <= nums[i] <= 10**9
"""
from typing import List


def find132pattern(nums: List[int]) -> bool:
    if len(set(nums)) < 3:
        return False

    min_nums: List[int] = [nums[0]]
    for idx in range(1, len(nums)):
        min_nums.append(min(nums[idx], min_nums[-1]))

    stack: List[int] = []
    for idx in range(len(nums) - 1, -1, -1):
        if nums[idx] > min_nums[idx]:
            while stack and stack[-1] <= min_nums[idx]:
                stack.pop()
            if stack and min_nums[idx] < stack[-1] < nums[idx]:
                return True
            stack.append(nums[idx])
    return False


if __name__ == '__main__':
    assert find132pattern([1, 2, 3, 4]) is False
    assert find132pattern([3, 1, 4, 2]) is True
    assert find132pattern([-1, 3, 2, 0]) is True
