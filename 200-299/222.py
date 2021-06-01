"""
Given the root of a complete binary tree, return the number of the nodes in the tree.

Every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in
the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

Constraints:
    The number of nodes in the tree is in the range [0, 5 * 10**4].
    0 <= Node.val <= 5 * 10**4
    The tree is guaranteed to be complete.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'TreeNode({self.val}, {self.left}, {self.right})'


def count_nodes(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    def left_depth(node: TreeNode) -> int:
        depth: int = 0

        while node:
            node = node.left
            depth += 1

        return depth

    left_subtree_depth: int = left_depth(root.left)
    right_subtree_depth: int = left_depth(root.right)

    if left_subtree_depth == right_subtree_depth:
        return 2**left_subtree_depth + count_nodes(root.right)
    else:
        return 2**right_subtree_depth + count_nodes(root.left)


if __name__ == '__main__':
    tree: TreeNode = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
    assert count_nodes(tree) == 6

    tree = TreeNode(1)
    assert count_nodes(tree) == 1

    assert count_nodes(None) == 0
