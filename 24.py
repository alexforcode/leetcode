"""
Given a linked list, swap every two adjacent nodes and return its head.

Constraints:
    The number of nodes in the list is in the range [0, 100].
    0 <= Node.val <= 100

Follow up: Can you solve the problem without modifying the values in the list's nodes?
(i.e., Only nodes themselves may be changed.)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'ListNode({self.val}, {self.next})'


def swap_pairs(head: ListNode) -> ListNode:
    result: ListNode = ListNode(0)
    result.next = head
    current: ListNode = result

    while current.next and current.next.next:
        first: ListNode = current.next
        second: ListNode = current.next.next
        first.next = second.next
        current.next = second
        current.next.next = first
        current = current.next.next

    return result.next


if __name__ == '__main__':
    lst = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print(swap_pairs(lst))

    lst = ListNode()
    print(swap_pairs(lst))

    lst = ListNode(1)
    print(swap_pairs(lst))
