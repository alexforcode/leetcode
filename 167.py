"""
Given an array of integers numbers that is already sorted in ascending order,
find two numbers such that they add up to a specific target number.

Return the indices of the two numbers (1-indexed) as an integer array answer of size 2,
where 1 <= answer[0] < answer[1] <= numbers.length.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Constraints:
    2 <= numbers.length <= 3 * 104
    -1000 <= numbers[i] <= 1000
    numbers is sorted in increasing order.
    -1000 <= target <= 1000
    Only one valid answer exists.
"""
from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
    start: int = 0
    end: int = len(numbers) - 1

    while start <= end:
        temp_sum: int = numbers[start] + numbers[end]
        if temp_sum < target:
            start += 1
        elif temp_sum > target:
            end -= 1
        else:
            return [start+1, end+1]


if __name__ == '__main__':
    assert two_sum([2, 7, 11, 15], 9) == [1, 2]
    assert two_sum([2, 3, 4], 6) == [1, 3]
    assert two_sum([-1, 0], -1) == [1, 2]
