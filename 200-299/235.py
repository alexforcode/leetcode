"""
Given a binary search tree (BST), find the lowest common ancestor of two given nodes in the BST.

The lowest common ancestor is defined between two nodes p and q as the lowest node in T
that has both p and q as descendants (where we allow a node to be a descendant of itself).

Constraints:
    The number of nodes in the tree is in the range [2, 10**5].
    -10**9 <= Node.val <= 10**9
    All Node.val are unique.
    p != q
    p and q will exist in the BST.
"""


class TreeNode:
    def __init__(self, x: int, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = x
        self.left = left
        self.right = right

    def __repr__(self):
        return f'TreeNode({self.val}, {self.left}, {self.right})'


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)

    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)

    return root


if __name__ == '__main__':
    node3: TreeNode = TreeNode(3)
    node5: TreeNode = TreeNode(5)
    node4: TreeNode = TreeNode(4, node3, node5)
    node0: TreeNode = TreeNode(0)
    node2: TreeNode = TreeNode(2, node0, node4)
    node7: TreeNode = TreeNode(7)
    node9: TreeNode = TreeNode(9)
    node8: TreeNode = TreeNode(8, node7, node9)
    node6: TreeNode = TreeNode(6, node2, node8)

    print(lowest_common_ancestor(node6, node2, node8))  # node6
    print(lowest_common_ancestor(node6, node2, node4))  # node2
