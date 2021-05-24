"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Constraints:
    n == nums.length
    1 <= n <= 5 * 10**4
    -2**31 <= nums[i] <= 2**31 - 1

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""
from typing import List, Optional


def majority_element(nums: List[int]) -> int:
    count: int = 0
    guess: Optional[int] = None

    for num in nums:
        if count == 0:
            guess = num

        count += 1 if guess == num else -1

    return guess


if __name__ == '__main__':
    assert majority_element([3, 2, 3]) == 3
    assert majority_element([2, 2, 1, 1, 1, 2, 2]) == 2
