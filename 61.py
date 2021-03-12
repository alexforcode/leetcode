"""
Given the head of a linked list, rotate the list to the right by k places.

Constraints:
    The number of nodes in the list is in the range [0, 500].
    -100 <= Node.val <= 100
    0 <= k <= 2 * 10**9
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'ListNode({self.val}, {self.next})'


def rotate_right(head: ListNode, k: int) -> ListNode:
    if not head or not head.next or k == 0:
        return head

    cur: ListNode = head
    length: int = 1
    while cur.next:
        cur = cur.next
        length += 1
    cur.next = head

    new_head_index = length - k % length

    index: int = 0
    cur = head
    prev: ListNode = ListNode(0)
    while index < new_head_index:
        prev = cur
        cur = cur.next
        index += 1

    prev.next = None

    return cur


if __name__ == '__main__':
    lst = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(rotate_right(lst, 2))

    lst = ListNode(0, ListNode(1, ListNode(2)))
    print(rotate_right(lst, 4))
