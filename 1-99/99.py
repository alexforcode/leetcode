"""
You are given the root of a binary search tree (BST), where exactly two nodes of the tree were swapped by mistake.
Recover the tree without changing its structure.

Follow up: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

Constraints:
    The number of nodes in the tree is in the range [2, 1000].
    -231 <= Node.val <= 231 - 1
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'TreeNode({self.val}, {self.left}, {self.right})'


def recover_tree(root: TreeNode) -> None:
    nodes: List[TreeNode] = []

    def dfs(node: TreeNode) -> None:
        if not node:
            return

        dfs(node.left)
        nodes.append(node)
        dfs(node.right)

    dfs(root)

    vals: List[int] = sorted(node.val for node in nodes)

    for idx in range(len(vals)):
        nodes[idx].val = vals[idx]


if __name__ == '__main__':
    tree = TreeNode(1, TreeNode(3, None, TreeNode(2)))
    recover_tree(tree)
    print(tree)
    # TreeNode(3, TreeNode(1, None, TreeNode(2)))

    tree = TreeNode(3, TreeNode(1), TreeNode(4, TreeNode(2)))
    recover_tree(tree)
    print(tree)
    # TreeNode(2, TreeNode(1), TreeNode(4, TreeNode(3)))
