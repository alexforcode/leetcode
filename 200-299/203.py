"""
Given the head of a linked list and an integer val,
remove all the nodes of the linked list that has Node.val == val, and return the new head.

Constraints:
    The number of nodes in the list is in the range [0, 10**4].
    1 <= Node.val <= 50
    0 <= k <= 50
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'ListNode({self.val}, {self.next})'


def remove_elements(head: Optional[ListNode], val: int) -> ListNode:
    while head and head.val == val:
        head = head.next

    cur_head: ListNode = head
    while cur_head and cur_head.next:
        if cur_head.next.val == val:
            cur_head.next = cur_head.next.next
        else:
            cur_head = cur_head.next

    return head


if __name__ == '__main__':
    lst = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
    print(remove_elements(lst, 6))  # ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    lst = None
    print(remove_elements(lst, 1))  # None

    lst = ListNode(7, ListNode(7, ListNode(7, ListNode(7))))
    print(remove_elements(lst, 7))  # None
