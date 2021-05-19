"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Constraints:
    1 <= nums.length <= 3 * 10**4
    -3 * 10**4 <= nums[i] <= 3 * 10**4
    Each element in the array appears twice except for one element which appears only once.
"""
from collections import defaultdict, Counter
from typing import List, DefaultDict


def single_number_list(nums: List[int]) -> int:
    unique: List[int] = []

    for num in nums:
        if num not in unique:
            unique.append(num)
        else:
            unique.remove(num)

    return unique.pop()


def single_number_hash(nums: List[int]) -> int:
    nums_of_rep: DefaultDict[int, int] = defaultdict(int)

    for num in nums:
        nums_of_rep[num] += 1

    for idx in nums_of_rep:
        if nums_of_rep[idx] == 1:
            return idx


def single_number_counter(nums: List[int]) -> int:
    nums_of_rep: Counter[int, int] = Counter(nums)

    return nums_of_rep.most_common()[-1][0]


def single_number_math(nums: List[int]) -> int:
    return 2 * sum(set(nums)) - sum(nums)


def single_number_bit(nums: List[int]) -> int:
    xor: int = 0

    for num in nums:
        xor ^= num

    return xor


if __name__ == '__main__':
    assert single_number_list([2, 2, 1]) == 1
    assert single_number_list([4, 1, 2, 1, 2]) == 4
    assert single_number_list([1]) == 1

    assert single_number_hash([2, 2, 1]) == 1
    assert single_number_hash([4, 1, 2, 1, 2]) == 4
    assert single_number_hash([1]) == 1

    assert single_number_counter([2, 2, 1]) == 1
    assert single_number_counter([4, 1, 2, 1, 2]) == 4
    assert single_number_counter([1]) == 1

    assert single_number_math([2, 2, 1]) == 1
    assert single_number_math([4, 1, 2, 1, 2]) == 4
    assert single_number_math([1]) == 1

    assert single_number_bit([2, 2, 1]) == 1
    assert single_number_bit([4, 1, 2, 1, 2]) == 4
    assert single_number_bit([1]) == 1
