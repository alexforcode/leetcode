"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as
descendants (where we allow a node to be a descendant of itself).

Constraints:
    The number of nodes in the tree is in the range [2, 10**5].
    -10**9 <= Node.val <= 10**9
    All Node.val are unique.
    p != q
    p and q will exist in the tree.
"""


class TreeNode:
    def __init__(self, val: int, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'TreeNode({self.val}, {self.left}, {self.right})'


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root or p == root or q == root:
        return root

    left_lca: TreeNode = lowest_common_ancestor(root.left, p, q)
    right_lca: TreeNode = lowest_common_ancestor(root.right, p, q)

    if left_lca and right_lca:
        return root

    return left_lca or right_lca


if __name__ == '__main__':
    node7: TreeNode = TreeNode(7)
    node4: TreeNode = TreeNode(4)
    node2: TreeNode = TreeNode(2, node7, node4)
    node6: TreeNode = TreeNode(6)
    node5: TreeNode = TreeNode(5, node6, node2)
    node0: TreeNode = TreeNode(0)
    node8: TreeNode = TreeNode(8)
    node1: TreeNode = TreeNode(1, node0, node8)
    node3: TreeNode = TreeNode(3, node5, node1)

    print(node3, node5, node1)
    print(node3, node5, node4)
