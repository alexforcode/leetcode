"""
Given the root of a binary tree, invert the tree, and return its root.

Constraints:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'TreeNode({self.val}, {self.left}, {self.right})'


def invert_tree(root: Optional[TreeNode]) -> TreeNode:
    if not root:
        return root

    def invert(node: TreeNode) -> None:
        if not node:
            return

        invert(node.left)
        invert(node.right)

        node.right, node.left = node.left, node.right

    invert(root)

    return root


if __name__ == '__main__':
    tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    print(invert_tree(tree))
    # TreeNode(4, TreeNode(7, TreeNode(9), TreeNode(6)), TreeNode(2, TreeNode(3), TreeNode(1)))

    tree = TreeNode(2, TreeNode(1), TreeNode(3))
    print(invert_tree(tree))
    # TreeNode(2, TreeNode(3), TreeNode(1))

    tree = TreeNode(1, TreeNode(2))
    print(invert_tree(tree))
    # TreeNode(1, None, TreeNode(2))

    print(invert_tree(None))
    # None
