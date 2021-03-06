"""
Merge two sorted linked lists and return it as a sorted list.
The list should be made by splicing together the nodes of the first two lists.

Constraints:
    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both l1 and l2 are sorted in non-decreasing order.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'ListNode({self.val}, {self.next})'


def merge_lists(l1: ListNode, l2: ListNode) -> ListNode:
    result = ListNode
    current = result

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next

        current = current.next

    if not l1:
        while l2:
            current.next = l2
            l2 = l2.next
            current = current.next

    if not l2:
        while l1:
            current.next = l1
            l1 = l1.next
            current = current.next

    return result.next


if __name__ == '__main__':
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    print(merge_lists(l1, l2))

    l1 = ListNode()
    l2 = ListNode()
    print(merge_lists(l1, l2))

    l1 = ListNode()
    l2 = ListNode(0, ListNode(1, ListNode(6)))
    print(merge_lists(l1, l2))
