"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.

Populate each next pointer to point to its next right node. If there is no next right node,
the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Follow up:
    You may only use constant extra space.
    Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

Constraints:
    The number of nodes in the given tree is less than 4096.
    -1000 <= node.val <= 1000
"""


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

    cur_node: Node = root

    while cur_node.left:
        next_level_node: Node = cur_node.left

        while cur_node:
            cur_node.left.next = cur_node.right

            if cur_node.next:
                cur_node.right.next = cur_node.next.left

            cur_node = cur_node.next

        cur_node = next_level_node

    return root


if __name__ == '__main__':
    tree = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
    print(connect(tree))
