"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list. Return the linked list sorted as well.

Constraints:
    The number of nodes in the list is in the range [0, 300].
    -100 <= Node.val <= 100
    The list is guaranteed to be sorted in ascending order.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'ListNode({self.val}, {self.next})'


def delete_duplicates(head: ListNode) -> ListNode:
    if not head:
        return head

    top: ListNode = ListNode(0, head)
    cur_head: ListNode = top
    while cur_head.next and cur_head.next.next:
        if cur_head.next.val == cur_head.next.next.val:
            val: int = cur_head.next.val
            while cur_head.next and cur_head.next.val == val:
                cur_head.next = cur_head.next.next
        else:
            cur_head = cur_head.next

    return top.next


if __name__ == '__main__':
    lst = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
    print(delete_duplicates(lst))  # ListNode(1, ListNode(2, ListNode(5)))

    lst = ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3)))))
    print(delete_duplicates(lst))  # ListNode(2, ListNode(3))

    lst = ListNode(0, ListNode(0, ListNode(1, ListNode(2, ListNode(3)))))
    print(delete_duplicates(lst))  # ListNode(1, ListNode(2, ListNode(3)))
