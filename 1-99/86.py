"""
Given the head of a linked list and a value x,
partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Constraints:
    The number of nodes in the list is in the range [0, 200].
    -100 <= Node.val <= 100
    -200 <= x <= 200
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'ListNode({self.val}, {self.next})'


def partition(head: ListNode, x: int) -> ListNode:
    if not head or not head.next:
        return head

    before_top: ListNode = ListNode()
    before: ListNode = before_top
    after_top: ListNode = ListNode()
    after: ListNode = after_top

    while head:
        if head.val < x:
            before.next = head
            before = before.next
        else:
            after.next = head
            after = after.next

        head = head.next

    after.next = None
    before.next = after_top.next

    return before_top.next


if __name__ == '__main__':
    lst = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
    print(partition(lst, 3))
    # ListNode(1, ListNode(2, ListNode(2, ListNode(4, ListNode(3, ListNode(5))))))

    lst = ListNode(2, ListNode(1))
    print(partition(lst, 2))  # ListNode(1, ListNode(2))
