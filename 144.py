"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.

Constraints:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'TreeNode({self.val}, {self.left}, {self.right})'


def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    result: List[int] = []

    if not root:
        return result

    stack: List[TreeNode] = [root]

    while stack:
        node: TreeNode = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


if __name__ == '__main__':
    tree = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert preorder_traversal(tree) == [1, 2, 3]

    tree = None
    assert preorder_traversal(tree) == []

    tree = TreeNode(1)
    assert preorder_traversal(tree) == [1]

    tree = TreeNode(1, TreeNode(2))
    assert preorder_traversal(tree) == [1, 2]

    tree = TreeNode(1, None, TreeNode(2))
    assert preorder_traversal(tree) == [1, 2]
