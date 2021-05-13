"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Constraints:
    1 <= intervals.length <= 10**4
    intervals[i].length == 2
    0 <= starti <= endi <= 10**4
"""
from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    if len(intervals) == 1:
        return intervals

    intervals.sort(key=lambda x: x[0])
    result: List[List[int]] = []

    for interval in intervals:
        if not result or result[-1][1] < interval[0]:
            result.append(interval)
        else:
            result[-1][1] = max(result[-1][1], interval[1])

    return result


if __name__ == '__main__':
    assert merge([[1, 3], [8, 10], [2, 6], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert merge([[1, 3]]) == [[1, 3]]
