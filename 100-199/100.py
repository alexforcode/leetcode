"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical,
and the nodes have the same value.

Constraints:
    The number of nodes in both trees is in the range [0, 100].
    -10**4 <= Node.val <= 10**4
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'TreeNode({self.val}, {self.left}, {self.right})'


def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True

    if not p or not q:
        return False

    if p.val != q.val:
        return False

    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


if __name__ == '__main__':
    tree1 = TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))
    tree2 = TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))
    assert is_same_tree(tree1, tree2) is True

    tree1 = TreeNode(1, TreeNode(2, None, None), TreeNode(1, None, None))
    tree2 = TreeNode(1, TreeNode(1, None, None), TreeNode(2, None, None))
    assert is_same_tree(tree1, tree2) is False
