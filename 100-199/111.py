"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Constraints:
    The number of nodes in the tree is in the range [0, 105].
    -1000 <= Node.val <= 1000
"""
from collections import deque
from typing import Deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'TreeNode({self.val}, {self.left}, {self.right})'


def min_depth(root: TreeNode) -> int:
    if not root:
        return 0

    queue: Deque = deque([(root, 1)])

    while queue:
        node: TreeNode
        depth: int
        node, depth = queue.popleft()

        if not node.left and not node.right:
            return depth

        if node.left:
            queue.append((node.left, depth+1))

        if node.right:
            queue.append((node.right, depth+1))


if __name__ == '__main__':
    tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert min_depth(tree) == 2

    tree = TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6)))))
    assert min_depth(tree) == 5
