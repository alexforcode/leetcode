"""
Given a binary tree. Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Follow up:
    You may only use constant extra space.
    Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

Constraints:
    The number of nodes in the given tree is less than 6000.
    -100 <= node.val <= 100
"""
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __repr__(self):
        next_node_val: int = self.next.val if self.next else None
        return f'Node({self.val}, {self.left}, {self.right}, {next_node_val})'


def connect(root: Node) -> Node:
    if not root:
        return root

    first_on_level: Optional[Node] = root

    while first_on_level:
        cur_node: Node = first_on_level
        first_on_level = None
        prev_node: Optional[Node] = None

        while cur_node:
            if cur_node.left:
                if not first_on_level:
                    first_on_level = cur_node.left

                if prev_node:
                    prev_node.next = cur_node.left

                prev_node = cur_node.left

            if cur_node.right:
                if not first_on_level:
                    first_on_level = cur_node.right

                if prev_node:
                    prev_node.next = cur_node.right

                prev_node = cur_node.right

            cur_node = cur_node.next

    return root


if __name__ == '__main__':
    tree = Node(1, Node(2, Node(4), Node(5)), Node(3, None, Node(7)))
    print(connect(tree))
