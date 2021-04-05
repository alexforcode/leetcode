"""
Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list,
instead you will be given access to the node to be deleted directly.

It is guaranteed that the node to be deleted is not a tail node in the list.

Constraints:
    The number of the nodes in the given list is in the range [2, 1000].
    -1000 <= Node.val <= 1000
    The value of each node in the list is unique.
    The node to be deleted is in the list and is not a tail node
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def delete_node(node: ListNode) -> None:
    node.val = node.next.val
    node.next = node.next.next

# 4 -> 5 -> 1 -> 9, 5 to del
# 4 -> 1 -> 1 -> 9
# 4 -> 1 -> 9
