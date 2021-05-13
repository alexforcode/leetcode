"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Constraints:
    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'ListNode({self.val}, {self.next})'


def reverse_list_iter(head: Optional[ListNode]) -> ListNode:
    if not head or not head.next:
        return head

    prev: Optional[ListNode] = None
    cur_head: ListNode = head

    while cur_head:
        next_head: ListNode = cur_head.next
        cur_head.next = prev
        prev = cur_head
        cur_head = next_head

    return prev


def reverse_list_recur(head: Optional[ListNode]) -> ListNode:
    if not head or not head.next:
        return head

    p: ListNode = reverse_list_recur(head.next)
    head.next.next = head
    head.next = None

    return p


if __name__ == '__main__':
    lst = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(reverse_list_iter(lst))
    lst = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(reverse_list_recur(lst))

    lst = ListNode(1, ListNode(2))
    print(reverse_list_iter(lst))
    lst = ListNode(1, ListNode(2))
    print(reverse_list_recur(lst))

    lst = ListNode(1)
    print(reverse_list_iter(lst))
    lst = ListNode(1)
    print(reverse_list_recur(lst))

    lst = None
    print(reverse_list_iter(lst))
    lst = None
    print(reverse_list_recur(lst))
