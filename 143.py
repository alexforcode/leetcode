"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Constraints:
    The number of nodes in the list is in the range [1, 5 * 10**4].
    1 <= Node.val <= 1000
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'ListNode({self.val}, {self.next})'


def reverse_list(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    prev: Optional[ListNode] = None
    cur: ListNode = head

    while cur:
        next_head: ListNode = cur.next
        cur.next = prev
        prev = cur
        cur = next_head

    return prev


def merge_lists(first_head: ListNode, second_head: ListNode) -> None:
    while first_head:
        first_next: ListNode = first_head.next
        second_next: ListNode = second_head.next

        first_head.next = second_head

        if not first_next:
            break

        second_head.next = first_next

        first_head = first_next
        second_head = second_next


def reorder_list(head: ListNode) -> None:
    #    1->2->3->4->5->None
    # 1: 1->2->None  3->4->5->None
    # 2: 1->2->None  5->4->3->None
    # 3: 1->5->2->4->3->None

    if not head.next:
        return

    # 1
    first_head: ListNode = head
    first_tail: Optional[ListNode] = None
    second_head: ListNode = head
    second_tail: ListNode = head

    while second_tail and second_tail.next:
        first_tail = second_head
        second_head = second_head.next
        second_tail = second_tail.next.next

    first_tail.next = None

    # 2
    head_of_reversed: ListNode = reverse_list(second_head)

    # 3
    merge_lists(first_head, head_of_reversed)


if __name__ == '__main__':
    lst = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    reorder_list(lst)
    print(lst)  # lst = ListNode(1, ListNode(4, ListNode(2, ListNode(3))))

    lst = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    reorder_list(lst)
    print(lst)  # lst = ListNode(1, ListNode(5, ListNode(2, ListNode(4, ListNode(3)))))
