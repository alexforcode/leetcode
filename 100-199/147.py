"""
Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

The steps of the insertion sort algorithm:

    Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
    At each iteration, insertion sort removes one element from the input data,
        finds the location it belongs within the sorted list and inserts it there.
    It repeats until no input elements remain.

Constraints:
    The number of nodes in the list is in the range [1, 5000].
    -5000 <= Node.val <= 5000
"""
from typing import Union


class ListNode:
    def __init__(self, val: Union[int, float] = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'ListNode({self.val}, {self.next})'


def insertion_sort_list(head: ListNode) -> ListNode:
    sorted_lst = ListNode(float('-inf'))
    dummy: ListNode = sorted_lst
    dummy.next = head

    while sorted_lst.next:
        node: ListNode = sorted_lst.next

        if node.val >= sorted_lst.val:
            sorted_lst = sorted_lst.next
            continue

        sorted_lst.next = sorted_lst.next.next

        insertion: ListNode = dummy
        while insertion.next.val <= node.val:
            insertion = insertion.next

        node.next = insertion.next
        insertion.next = node

    return dummy.next


if __name__ == '__main__':
    lst: ListNode = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    print(insertion_sort_list(lst))

    lst: ListNode = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
    print(insertion_sort_list(lst))
