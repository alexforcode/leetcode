"""
Given the head of a singly linked list and two integers left and right where left <= right,
reverse the nodes of the list from position left to position right, and return the reversed list.

Constraints:
    The number of nodes in the list is n.
    1 <= n <= 500
    -500 <= Node.val <= 500
    1 <= left <= right <= n

Follow up: Could you do it in one pass?
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'ListNode({self.val}, {self.next})'


def reverse_between(head: ListNode, left: int, right: int) -> ListNode:
    cur_head: ListNode = head
    prev_head: Optional[ListNode] = None

    while left > 1:
        prev_head = cur_head
        cur_head = cur_head.next
        left -= 1
        right -= 1

    end: ListNode = cur_head
    start: ListNode = prev_head

    while right:
        next_head: ListNode = cur_head.next
        cur_head.next = prev_head
        prev_head = cur_head
        cur_head = next_head
        right -= 1

    if start:
        start.next = prev_head
    else:
        head = prev_head

    end.next = cur_head

    return head


if __name__ == '__main__':
    lst = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(reverse_between(lst, 2, 4))  # ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5)))))

    lst = ListNode(5)
    print(reverse_between(lst, 1, 1))  # ListNode(5)
