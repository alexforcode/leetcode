"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Constraints:
    The number of nodes in the tree is in the range [1, 1000].
    -100 <= Node.val <= 100

Follow up: Could you solve it both recursively and iteratively?
"""
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'TreeNode({self.val}, {self.left}, {self.right})'


def is_symmetric(root: TreeNode) -> bool:
    nodes: List[TreeNode] = [root, root]

    while nodes:
        node1: TreeNode = nodes.pop()
        node2: TreeNode = nodes.pop()

        if not node1 and not node2:
            continue

        if not node1 or not node2 or node1.val != node2.val:
            return False

        nodes.extend([node1.left, node2.right, node1.right, node2.left])

    return True


def is_symmetric_recursive(root: TreeNode) -> bool:
    def is_mirror(node1: TreeNode, node2: TreeNode) -> bool:
        if not node1 and not node2:
            return True

        if not node1 or not node2:
            return False

        return node1.val == node2.val and is_mirror(node1.left, node2.right) and is_mirror(node1.right, node2.left)

    return is_mirror(root, root)


if __name__ == '__main__':
    tree = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
    assert is_symmetric(tree) is True

    tree = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
    assert is_symmetric(tree) is False

    tree = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
    assert is_symmetric_recursive(tree) is True

    tree = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
    assert is_symmetric_recursive(tree) is False
