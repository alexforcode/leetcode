"""
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support
all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:
    void push(int x) Pushes element x to the back of the queue.
    int pop() Removes the element from the front of the queue and returns it.
    int peek() Returns the element at the front of the queue.
    boolean empty() Returns true if the queue is empty, false otherwise.

Notes:
    You must use only standard operations of a stack, which means only push to top, peek/pop from top, size,
    and is empty operations are valid.
    Depending on your language, the stack may not be supported natively. You may simulate a stack using
     a list or deque (double-ended queue) as long as you use only a stack's standard operations.

Follow-up:
    Can you implement the queue such that each operation is amortized O(1) time complexity? In other words,
    performing n operations will take overall O(n) time even if one of those operations may take longer.

Constraints:
    1 <= x <= 9
    At most 100 calls will be made to push, pop, peek, and empty.
    All the calls to pop and peek are valid.
"""
from collections import deque
from typing import Deque


class MyQueue:
    _queue: Deque[int]

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._queue = deque()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self._queue.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self._queue.popleft()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self._queue[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self._queue


if __name__ == '__main__':
    my_queue = MyQueue()
    my_queue.push(1)
    my_queue.push(2)
    print(my_queue.peek())  # 1
    print(my_queue.pop())  # 1
    print(my_queue.empty())  # False
