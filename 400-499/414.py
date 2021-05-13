"""
Given integer array nums, return the third maximum number in this array.
If the third maximum does not exist, return the maximum number.

Constraints:
    1 <= nums.length <= 10**4
    -2**31 <= nums[i] <= 2**31 - 1

Follow up: Can you find an O(n) solution?
"""
from typing import List, Optional


def third_max(nums: List[int]) -> int:
    first: Optional[int] = None
    second: Optional[int] = None
    third: Optional[int] = None

    for num in nums:
        if num == first or num == second or num == third:
            continue

        if first is None or num > first:
            first, second, third = num, first, second
        elif second is None or num > second:
            second, third = num, second
        elif third is None or num > third:
            third = num

    return first if third is None else third


if __name__ == '__main__':
    assert third_max([3, 2, 1]) == 1
    assert third_max([2, 1]) == 2
    assert third_max([2, 3, 2, 1]) == 1
    assert third_max([3, 3, 4, 3, 4, 3, 0, 3, 3]) == 0
