"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Constraints:
    k == lists.length
    0 <= k <= 10^4
    0 <= lists[i].length <= 500
    -10**4 <= lists[i][j] <= 10**4
    lists[i] is sorted in ascending order.
    The sum of lists[i].length won't exceed 10**4.
"""
from typing import List, Union


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'ListNode({self.val}, {self.next})'


def merge_k_lists(lists: List[Union[List, ListNode]]) -> ListNode:
    values: List[int] = []

    head: ListNode = ListNode(0)
    cur_node: ListNode = head

    for lst in lists:
        while lst:
            values.append(lst.val)
            lst = lst.next

    for val in sorted(values):
        cur_node.next = ListNode(val)
        cur_node = cur_node.next

    return head.next


if __name__ == '__main__':
    lists = [ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))]
    print(merge_k_lists(lists))
    # ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4, ListNode(5, ListNode(6))))))))

    print(merge_k_lists([]))  # None
    print(merge_k_lists([[]]))  # None
