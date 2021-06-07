"""
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

Constraints:
    n == nums.length
    1 <= n <= 10**4
    0 <= nums[i] <= n
    All the numbers of nums are unique
"""
from typing import List


def missing_number(nums: List[int]) -> int:
    # n * (n - 1) / 2 - sum(nums)
    return ((len(nums) + 1) * len(nums) // 2) - sum(nums)


if __name__ == '__main__':
    assert missing_number([3, 0, 1]) == 2
    assert missing_number([0, 1]) == 2
    assert missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    assert missing_number([0]) == 1
