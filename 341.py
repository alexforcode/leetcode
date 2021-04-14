"""
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may
also be integers or other lists. Implement an iterator to flatten it.

Implement the NestedIterator class:
    NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
    int next() Returns the next integer in the nested list.
    boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.

Constraints:
    1 <= nestedList.length <= 500
    The values of the integers in the nested list is in the range [-10**6, 10**6].
"""
from collections import deque
from typing import Deque, List


class NestedInteger(list):
    def is_integer(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        pass

    def get_integer(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        pass

    def get_list(self) -> 'NestedInteger':
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        pass


class NestedIterator:
    _queue: Deque

    def __init__(self, nested_list: NestedInteger):

        def flatten(n_lst: [NestedInteger]) -> List[int]:
            tmp: List[int] = []
            for val in n_lst:
                if val.isInteger():
                    tmp.append(val.getInteger())
                else:
                    tmp.extend(flatten(val.getList()))
            return tmp

        self._queue = deque(flatten(nested_list))

    def next(self) -> int:
        return self._queue.popleft()

    def has_next(self) -> bool:
        return bool(self._queue)
