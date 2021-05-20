"""
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

Constraints:
    The number of nodes in the list is in the range [0, 5 * 10**4].
    -10**5 <= Node.val <= 10**5
"""
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'ListNode({self.val}, {self.next})'


def sort_list(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    fast: ListNode = head
    slow: ListNode = head
    prev: Optional[ListNode] = None

    while fast and fast.next:
        prev, slow, fast = slow, slow.next, fast.next.next

    prev.next = None
    left: ListNode = sort_list(head)
    right: ListNode = sort_list(slow)

    def merge(one: ListNode, two: ListNode) -> ListNode:
        merged: ListNode = ListNode()
        dummy: ListNode = merged

        while one and two:
            if one.val <= two.val:
                merged.next = one
                one = one.next
            else:
                merged.next = two
                two = two.next

            merged = merged.next

        merged.next = one or two

        return dummy.next

    return merge(left, right)


if __name__ == '__main__':
    lst: ListNode = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    print(sort_list(lst))
    # ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

    lst = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
    print(sort_list(lst))
    # lst = ListNode(-1, ListNode(0, ListNode(3, ListNode(4, ListNode(5)))))
