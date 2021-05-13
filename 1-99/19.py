"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

Constraints:
    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'ListNode({self.val}, {self.next})'


def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    result: ListNode = ListNode(0)
    result.next = head

    fast: ListNode = result
    slow: ListNode = result

    for _ in range(n+1):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return result.next


if __name__ == '__main__':
    lst: ListNode = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(remove_nth_from_end(lst, 2))

    lst: ListNode = ListNode(1)
    print(remove_nth_from_end(lst, 1))

    lst: ListNode = ListNode(1, ListNode(2))
    print(remove_nth_from_end(lst, 1))
