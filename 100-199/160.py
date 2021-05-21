"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
If the two linked lists have no intersection at all, return null.

It is guaranteed that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Constraints:
    The number of nodes of listA is in the m.
    The number of nodes of listB is in the n.
    0 <= m, n <= 3 * 10**4
    1 <= Node.val <= 10**5
    0 <= skipA <= m
    0 <= skipB <= n
    intersectVal is 0 if listA and listB do not intersect.
    intersectVal == listA[skipA + 1] == listB[skipB + 1] if listA and listB intersect.

Follow up: Could you write a solution that runs in O(n) time and use only O(1) memory?
"""
from typing import Optional


class ListNode:
    def __init__(self, x: int = 0, next: 'ListNode' = None):
        self.val = x
        self.next = next

    def __repr__(self):
        return f'ListNode({self.val}, {self.next})'


def get_intersection_node(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    if not headA or not headB:
        return None

    savedA: ListNode = headA
    savedB: ListNode = headB

    while headA != headB:
        headA = savedB if not headA else headA.next
        headB = savedA if not headB else headB.next

    return headA


if __name__ == '__main__':
    listC: ListNode = ListNode(8, ListNode(4, ListNode(5)))
    listA: ListNode = ListNode(4, ListNode(1, listC))
    listB: ListNode = ListNode(5, ListNode(6, ListNode(1, listC)))
    assert get_intersection_node(listA, listB) == listC

    listC: ListNode = ListNode(2, ListNode(4))
    listA: ListNode = ListNode(1, ListNode(9, ListNode(1, listC)))
    listB: ListNode = ListNode(3, listC)
    assert get_intersection_node(listA, listB) == listC

    listA: ListNode = ListNode(2, ListNode(6, ListNode(4)))
    listB: ListNode = ListNode(1, ListNode(5))
    assert get_intersection_node(listA, listB) is None
