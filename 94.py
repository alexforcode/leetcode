"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

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


def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    result: List[int] = []

    if not root:
        return result

    stack: List[TreeNode] = []
    cur_node: TreeNode = root

    while cur_node or stack:
        while cur_node:
            stack.append(cur_node)
            cur_node = cur_node.left

        cur_node = stack.pop()
        result.append(cur_node.val)
        cur_node = cur_node.right

    return result


def inorder_traversal_recursive(root: Optional[TreeNode]) -> List[int]:
    result: List[int] = []

    if not root:
        return result

    def traversal(node: TreeNode) -> None:
        if not node:
            return

        traversal(node.left)
        result.append(node.val)
        traversal(node.right)

    traversal(root)

    return result


if __name__ == '__main__':
    tree = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert inorder_traversal(tree) == [1, 3, 2]

    tree = None
    assert inorder_traversal(tree) == []

    tree = TreeNode(1)
    assert inorder_traversal(tree) == [1]

    tree = TreeNode(1, TreeNode(2))
    assert inorder_traversal(tree) == [2, 1]

    tree = TreeNode(1, None, TreeNode(2))
    assert inorder_traversal(tree) == [1, 2]

    tree = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert inorder_traversal_recursive(tree) == [1, 3, 2]
