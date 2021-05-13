"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:
    a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Constraints:
    The number of nodes in the tree is in the range [0, 5000].
    -104 <= Node.val <= 104
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(root: TreeNode) -> bool:
    def is_subtree_balanced(node: TreeNode) -> int:
        if not node:
            return 0

        left_subtree_height: int = is_subtree_balanced(node.left)
        if left_subtree_height == -1:
            return -1

        right_subtree_height: int = is_subtree_balanced(node.right)
        if right_subtree_height == -1:
            return -1

        if abs(left_subtree_height - right_subtree_height) > 1:
            return -1

        return max(left_subtree_height, right_subtree_height) + 1

    return True if is_subtree_balanced(root) != -1 else False


if __name__ == '__main__':
    tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert is_balanced(tree) is True

    tree = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
    assert is_balanced(tree) is False
