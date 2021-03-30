"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
    - The left subtree of a node contains only nodes with keys less than the node's key.
    - The right subtree of a node contains only nodes with keys greater than the node's key.
    - Both the left and right subtrees must also be binary search trees.

Constraints:
    The number of nodes in the tree is in the range [1, 104].
    -2**31 <= Node.val <= 2**31 - 1
"""
from typing import Union


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: TreeNode) -> bool:
    def check_node(node: TreeNode, max_val: Union[int, float], min_val: Union[int, float]) -> bool:
        if not node:
            return True
        elif max_val != float('inf') and node.val >= max_val or min_val != -float('inf') and node.val <= min_val:
            return False
        return check_node(node.left, node.val, min_val) and check_node(node.right, max_val, node.val)

    return check_node(root, float('inf'), -float('inf'))


if __name__ == '__main__':
    tree = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
    assert is_valid_bst(tree) is True

    tree = TreeNode(5, TreeNode(1, None, None), TreeNode(4, TreeNode(3, None, None), TreeNode(6, None, None)))
    assert is_valid_bst(tree) is False

    tree = TreeNode(5, TreeNode(4, None, None), TreeNode(6, TreeNode(3, None, None), TreeNode(7, None, None)))
    assert is_valid_bst(tree) is False

    tree = TreeNode(0, None, TreeNode(-1, None, None))
    assert is_valid_bst(tree) is False
