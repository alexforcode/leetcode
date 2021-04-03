"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Follow-up: Could you solve the problem in linear time and in O(1) space?

Constraints:
    1 <= nums.length <= 5 * 104
    -109 <= nums[i] <= 109
"""
from typing import List, Optional


def majority_element(nums: List[int]) -> List[int]:
    if len(nums) < 2:
        return nums

    result: List[int] = []
    third: int = len(nums) // 3
    f_val: Optional[int] = None
    f_count: int = 0
    s_val: Optional[int] = None
    s_count: int = 0

    for num in nums:
        if f_val == num:
            f_count += 1
        elif s_val == num:
            s_count += 1
        elif not f_count:
            f_val, f_count = num, 1
        elif not s_count:
            s_val, s_count = num, 1
        else:
            f_count -= 1
            s_count -= 1

    f_count, s_count = 0, 0
    for num in nums:
        if f_val == num:
            f_count += 1
        if s_val == num:
            s_count += 1

    if f_count > third:
        result.append(f_val)
    if s_count > third:
        result.append(s_val)

    return result


if __name__ == '__main__':
    assert majority_element([3, 2, 3]) == [3]
    assert majority_element([1]) == [1]
    assert majority_element([1, 2]) == [1, 2]
    assert majority_element([2, 2]) == [2]
