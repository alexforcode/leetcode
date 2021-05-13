"""
Given the head of a singly linked list where elements are sorted in ascending order,
convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees
of every node never differ by more than 1.

Constraints:
    The number of nodes in head is in the range [0, 2 * 10**4].
    -10*5 <= Node.val <= 10*5
"""
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'ListNode({self.val}, {self.next})'


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'TreeNode({self.val}, {self.left}, {self.right})'


def sorted_list_to_bst(head: Optional[ListNode]) -> Optional[TreeNode]:
    if not head:
        return

    converted: List[int] = []
    while head:
        converted.append(head.val)
        head = head.next

    def convert_to_bts(left: int, right: int) -> Optional[TreeNode]:
        if left > right:
            return None

        mid: int = (left + right) // 2
        node: TreeNode = TreeNode(converted[mid])

        if left == right:
            return node

        node.left = convert_to_bts(left, mid-1)
        node.right = convert_to_bts(mid+1, right)

        return node

    return convert_to_bts(0, len(converted)-1)


def sorted_list_to_bst_recursive(head: Optional[ListNode]) -> Optional[TreeNode]:
    if not head:
        return

    list_len: int = 0
    cur: ListNode = head
    while cur:
        cur = cur.next
        list_len += 1

    def convert_to_bts(left: int, right: int) -> Optional[TreeNode]:
        nonlocal head

        if left > right:
            return None

        mid: int = (left + right) // 2

        left_node: TreeNode = convert_to_bts(left, mid - 1)

        node: TreeNode = TreeNode(head.val)
        node.left = left_node

        head = head.next

        node.right = convert_to_bts(mid+1, right)

        return node

    return convert_to_bts(0, list_len-1)


if __name__ == '__main__':
    lst = ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9)))))
    print(sorted_list_to_bst(lst))
    print(sorted_list_to_bst_recursive(lst))

    lst = ListNode(1, ListNode(3))
    print(sorted_list_to_bst(lst))
    print(sorted_list_to_bst_recursive(lst))

    lst = ListNode(0)
    print(sorted_list_to_bst(lst))
    print(sorted_list_to_bst_recursive(lst))

    print(sorted_list_to_bst(None))
    print(sorted_list_to_bst_recursive(None))
