"""
Given the root of a binary tree, return the leftmost value in the last row of the tree.

Constraints:
    The number of nodes in the tree is in the range [1, 10**4].
    -2**31 <= Node.val <= 2**31 - 1
"""
from collections import deque
from typing import Deque, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'TreeNode({self.val}, {self.left}, {self.right})'


def find_bottom_left_value(root: TreeNode) -> int:
    queue: Deque[TreeNode] = deque([root])
    cur_left: Optional[int] = root.val
    check_left: bool = True

    while queue:
        for _ in range(len(queue)):
            node: TreeNode = queue.popleft()
            if not check_left:
                cur_left = node.val
                check_left = True

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        check_left = False

    return cur_left


if __name__ == '__main__':
    tree = TreeNode(2, TreeNode(1), TreeNode(3))
    assert find_bottom_left_value(tree) == 1

    tree = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5, TreeNode(7)), TreeNode(6)))
    assert find_bottom_left_value(tree) == 7

    tree = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5)))
    assert find_bottom_left_value(tree) == 4
