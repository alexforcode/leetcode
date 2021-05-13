"""
Given the root of a binary tree, flatten the tree into a "linked list":

    The "linked list" should use the same TreeNode class where the right child pointer points to the next node
        in the list and the left child pointer is always null.
    The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Constraints:
    The number of nodes in the tree is in the range [0, 2000].
    -100 <= Node.val <= 100

Follow up: Can you flatten the tree in-place (with O(1) extra space)?
"""
from collections import deque
from typing import Deque, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'TreeNode({self.val}, {self.left}, {self.right})'


def flatten(root: Optional[TreeNode]) -> None:
    if not root:
        return

    stack: Deque = deque([root])

    while stack:
        node: TreeNode = stack.pop()

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

        if stack:
            node.right = stack[-1]

        node.left = None


if __name__ == '__main__':
    tree = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
    flatten(tree)
    print(tree)

    tree = None
    flatten(tree)
    print(tree)

    tree = TreeNode(0)
    flatten(tree)
    print(tree)
