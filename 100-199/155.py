"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
    MinStack() initializes the stack object.
    void push(val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

Constraints:
    -2**31 <= val <= 2**31 - 1
    Methods pop, top and getMin operations will always be called on non-empty stacks.
    At most 3 * 10*4 calls will be made to push, pop, top, and getMin.
"""
from typing import List


class MinStack:
    _stack: List[int]
    _min: List[int]

    def __init__(self):
        self._stack = []
        self._min = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        self._min.append(val if not self._min else min(self._min[-1], val))

    def pop(self) -> None:
        self._stack.pop()
        self._min.pop()

    def top(self) -> int:
        return self._stack[-1]

    def get_min(self) -> int:
        return self._min[-1]


if __name__ == '__main__':
    stack: MinStack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    print(stack.get_min())  # -3
    stack.pop()
    print(stack.top())  # 0
    print(stack.get_min())  # -2
