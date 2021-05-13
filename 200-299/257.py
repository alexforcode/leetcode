"""
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

Constraints:
    The number of nodes in the tree is in the range [1, 100].
    -100 <= Node.val <= 100
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_tree_paths(root: TreeNode) -> List[str]:
    result: List[str] = []

    def check_path(node: TreeNode, path: str) -> None:
        if not node:
            return

        path += str(node.val)

        if not node.left and not node.right:
            result.append(path)
            return

        check_path(node.left, path+'->')
        check_path(node.right, path+'->')

    check_path(root, '')

    return result


if __name__ == '__main__':
    tree = TreeNode(1, TreeNode(2, None, TreeNode(5, None, None)), TreeNode(3, None, None))
    print(binary_tree_paths(tree))  # ['1->2->5', '1->3']

    tree = TreeNode(1, None, None)
    print(binary_tree_paths(tree))  # ['1']

    tree = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
    print(binary_tree_paths(tree))  # ['2->1', '2->3']

    tree = TreeNode(5, TreeNode(4, None, None), TreeNode(6, TreeNode(3, None, None), TreeNode(7, None, None)))
    print(binary_tree_paths(tree))  # ['5->4', '5->6->3', '5->6->7']
