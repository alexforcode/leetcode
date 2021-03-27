"""
Implement a last in first out (LIFO) stack using only two queues.
The implemented stack should support all the functions of a normal queue (push, top, pop, and empty).

Implement the MyStack class:
    void push(int x) Pushes element x to the top of the stack.
    int pop() Removes the element on the top of the stack and returns it.
    int top() Returns the element on the top of the stack.
    boolean empty() Returns true if the stack is empty, false otherwise.

Notes:
    You must use only standard operations of a queue,
    which means only push to back, peek/pop from front, size, and is empty operations are valid.
    Depending on your language, the queue may not be supported natively. You may simulate a queue using
    a list or deque (double-ended queue), as long as you use only a queue's standard operations.

Constraints:
    1 <= x <= 9
    At most 100 calls will be made to push, pop, top, and empty.
    All the calls to pop and top are valid.

Follow-up: Can you implement the stack such that each operation is amortized O(1) time complexity?
In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.
You can use more than two queues.
"""
from collections import deque
from typing import Deque


class MyStack:
    _stack: Deque[int]

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._stack = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self._stack.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self._stack.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self._stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self._stack


if __name__ == '__main__':
    my_stack = MyStack()
    my_stack.push(1)
    my_stack.push(2)
    print(my_stack.top())  # 2
    print(my_stack.pop())  # 2
    print(my_stack.empty())  # False
