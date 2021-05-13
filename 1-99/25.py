"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

Follow up:
    Could you solve the problem in O(1) extra memory space?
    You may not alter the values in the list's nodes, only nodes itself may be changed.

Constraints:
    The number of nodes in the list is in the range sz.
    1 <= sz <= 5000
    0 <= Node.val <= 1000
    1 <= k <= sz
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'ListNode({self.val}, {self.next})'


def reverse_k_group(head: ListNode, k: int) -> ListNode:
    if not head or k < 2:
        return head

    def reverse(start: ListNode, end: ListNode):
        prev: ListNode = start
        current: ListNode = start.next
        head: ListNode = current

        while current != end:
            temp: ListNode = current.next
            current.next = prev
            prev = current
            current = temp

        start.next = prev
        head.next = current

        return head

    before: ListNode = ListNode(0, head)
    start: ListNode = before
    end: ListNode = head
    count: int = 0

    while end:
        count += 1
        if count % k == 0:
            start = reverse(start, end.next)
            end = start.next
        else:
            end = end.next

    return before.next


if __name__ == '__main__':
    lst = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(reverse_k_group(lst, 2))
    # ListNode(2, ListNode(1, ListNode(4, ListNode(3, ListNode(5)))))

    lst = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(reverse_k_group(lst, 3))
    # ListNode(3, ListNode(2, ListNode(1, ListNode(4, ListNode(5)))))

    lst = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(reverse_k_group(lst, 1))
    # ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    print(reverse_k_group(ListNode(1), 1))
    # ListNode(1)
