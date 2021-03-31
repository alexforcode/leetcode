"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list sorted as well.

Constraints:
    The number of nodes in the list is in the range [0, 300].
    -100 <= Node.val <= 100
    The list is guaranteed to be sorted in ascending order.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'ListNode({self.val}, {self.next})'


def delete_duplicates(head: Optional[ListNode]) -> ListNode:
    cur_head: ListNode = head
    while cur_head and cur_head.next:
        if cur_head.val == cur_head.next.val:
            cur_head.next = cur_head.next.next
        else:
            cur_head = cur_head.next

    return head


if __name__ == '__main__':
    lst = ListNode(1, ListNode(1, ListNode(2)))
    print(delete_duplicates(lst))  # ListNode(1, ListNode(2))

    lst = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
    print(delete_duplicates(lst))  # ListNode(1, ListNode(2, ListNode(3)))

    lst = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(3))))))
    print(delete_duplicates(lst))  # ListNode(1, ListNode(2, ListNode(3)))

    lst = None
    print(delete_duplicates(lst))  # None
