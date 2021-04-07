"""
Given an array of integers nums containing n + 1 integers
where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

Constraints:
    2 <= n <= 3 * 10**4
    nums.length == n + 1
    1 <= nums[i] <= n
    All the integers in nums appear only once except for precisely one integer which appears two or more times.

Follow up:
    How can we prove that at least one duplicate number must exist in nums?
    Can you solve the problem without modifying the array nums?
    Can you solve the problem using only constant, O(1) extra space?
    Can you solve the problem with runtime complexity less than O(n**2)?
"""
from typing import List, Set


def find_duplicate(nums: List[int]) -> int:
    # O(n) - time
    # O(n) - space
    if len(nums) == 2:
        return 1

    seen: Set = set()

    for num in nums:
        if num in seen:
            return num
        seen.add(num)


def find_duplicate_2(nums: List[int]) -> int:
    # O(n) - time
    # O(1) - space
    slow: int = nums[0]
    fast: int = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow = nums[0]

    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow


if __name__ == '__main__':
    assert find_duplicate([1, 3, 4, 2, 2]) == 2
    assert find_duplicate([3, 1, 3, 4, 2]) == 3
    assert find_duplicate([1, 1]) == 1
    assert find_duplicate([1, 1, 2]) == 1

    assert find_duplicate_2([1, 3, 4, 2, 2]) == 2
    assert find_duplicate_2([3, 1, 3, 4, 2]) == 3
    assert find_duplicate_2([1, 1]) == 1
    assert find_duplicate_2([1, 1, 2]) == 1
