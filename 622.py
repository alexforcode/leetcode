"""
Design your implementation of the circular queue. The circular queue is a linear data structure in which
the operations are performed based on FIFO (First In First Out) principle and the last position is connected back
to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue.
In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front
of the queue. But using the circular queue, we can use the space to store new values.

Implementation the MyCircularQueue class:
    MyCircularQueue(k) Initializes the object with the size of the queue to be k.
    int Front() Gets the front item from the queue. If the queue is empty, return -1.
    int Rear() Gets the last item from the queue. If the queue is empty, return -1.
    boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
    boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
    boolean isEmpty() Checks whether the circular queue is empty or not.
    boolean isFull() Checks whether the circular queue is full or not.

Constraints:
    1 <= k <= 1000
    0 <= value <= 1000

Follow up: Could you solve the problem without using the built-in queue?
"""
from typing import List


class MyCircularQueue:
    _size: int
    _queue: List[int]

    def __init__(self, k: int):
        self._size = k
        self._queue = []

    def enqueue(self, value: int) -> bool:
        if not self._size:
            return False
        else:
            self._queue.append(value)
            self._size -= 1
            return True

    def dequeue(self) -> bool:
        if not self._queue:
            return False
        else:
            self._queue.pop(0)
            self._size += 1
            return True

    def front(self) -> int:
        if not self._queue:
            return -1
        else:
            return self._queue[0]

    def rear(self) -> int:
        if not self._queue:
            return -1
        else:
            return self._queue[-1]

    def is_empty(self) -> bool:
        return True if not self._queue else False

    def is_full(self) -> bool:
        return True if not self._size else False


if __name__ == '__main__':
    my_queue = MyCircularQueue(3)
    assert my_queue.is_empty() is True
    assert my_queue.enqueue(1) is True
    assert my_queue.enqueue(2) is True
    assert my_queue.enqueue(3) is True
    assert my_queue.is_empty() is False
    assert my_queue.enqueue(4) is False
    assert my_queue.rear() == 3
    assert my_queue.is_full() is True
    assert my_queue.dequeue() is True
    assert my_queue.enqueue(4) is True
    assert my_queue.rear() == 4
