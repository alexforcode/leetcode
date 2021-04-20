"""
Given an array of distinct integers nums and a target integer target,
return the number of possible combinations that add up to target.

The answer is guaranteed to fit in a 32-bit integer.

Constraints:
    1 <= nums.length <= 200
    1 <= nums[i] <= 1000
    All the elements of nums are unique.
    1 <= target <= 1000

Follow up: What if negative numbers are allowed in the given array? How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
"""
from functools import lru_cache
from typing import List


def combination_sum_4(nums: List[int], target: int) -> int:
    combs: List[int] = [0] * (target+1)
    combs[0] = 1

    for idx in range(1, target+1):
        for num in nums:
            if num <= idx:
                combs[idx] += combs[idx - num]

    return combs[target]


def combination_sum_4_recursive(nums: List[int], target: int) -> int:
    @lru_cache(None)
    def get_number_of_combinations(cur: int) -> int:
        if cur == target:
            return 1

        result: int = 0

        for num in nums:
            if cur + num <= target:
                result += get_number_of_combinations(cur + num)

        return result

    return get_number_of_combinations(0)


if __name__ == '__main__':
    assert combination_sum_4([1, 2, 3], 4) == 7
    assert combination_sum_4([9], 3) == 0

    assert combination_sum_4_recursive([1, 2, 3], 4) == 7
    assert combination_sum_4_recursive([9], 3) == 0
