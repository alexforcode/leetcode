"""
Given the head of a singly linked list, return true if it is a palindrome.

Constraints:
    The number of nodes in the list is in the range [1, 105].
    0 <= Node.val <= 9
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'ListNode({self.val}, {self.next})'


def get_reversed(head: ListNode) -> ListNode:
    prev: Optional[ListNode] = None

    while head:
        next_head: ListNode = head.next
        head.next = prev
        prev = head
        head = next_head

    return prev


def is_palindrome(head: ListNode) -> bool:
    fast: ListNode = head
    slow: ListNode = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    slow = get_reversed(slow)
    fast = head

    while slow:
        if slow.val != fast.val:
            return False

        slow = slow.next
        fast = fast.next

    return True


if __name__ == '__main__':
    lst = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    assert is_palindrome(lst) is True

    lst = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
    assert is_palindrome(lst) is True

    lst = ListNode(1, ListNode(2))
    assert is_palindrome(lst) is False

    lst = ListNode(1)
    assert is_palindrome(lst) is True


