"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.

Constraints:
    The number of nodes in the tree is in the range [0, 104].
    -100 <= Node.val <= 100
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: TreeNode) -> int:
    if not root:
        return 0

    depth: int = 0

    def check_depth(node: TreeNode, cur_depth: int) -> None:
        if not node:
            return

        nonlocal depth

        if not node.left and not node.right:
            depth = max(depth, cur_depth)

        check_depth(node.left, cur_depth+1)
        check_depth(node.right, cur_depth+1)

    check_depth(root, 1)

    return depth


if __name__ == '__main__':
    tree = TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))
    assert max_depth(tree) == 3

    tree = TreeNode(1, None, TreeNode(2, None, None))
    assert max_depth(tree) == 2

    tree = TreeNode()
    assert max_depth(tree) == 1

    tree = None
    assert max_depth(tree) == 0
