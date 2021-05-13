"""
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths
where each path's sum equals targetSum.

A leaf is a node with no children.

Constraints:
    The number of nodes in the tree is in the range [0, 5000].
    -1000 <= Node.val <= 1000
    -1000 <= targetSum <= 1000
"""
from collections import deque
from typing import Deque, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'TreeNode({self.val}, {self.left}, {self.right})'


def path_sum(root: TreeNode, target_sum: int) -> List[List[int]]:
    result: List[List[int]] = []

    if not root:
        return result

    path: List[int] = []

    def traversal(node: TreeNode, cur_sum: int) -> None:
        if not node:
            return

        path.append(node.val)
        if node.val == cur_sum and not node.left and not node.right:
            result.append(path[:])
            path.pop()
            return

        traversal(node.left, cur_sum - node.val)
        traversal(node.right, cur_sum - node.val)
        path.pop()

    traversal(root, target_sum)

    return result


if __name__ == '__main__':
    tree = TreeNode(5,
                    TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
                    TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
    assert path_sum(tree, 22) == [[5, 4, 11, 2], [5, 8, 4, 5]]

    tree = TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))
    assert path_sum(tree, 5) == []

    tree = TreeNode(1, TreeNode(2, None, None), None)
    assert path_sum(tree, 0) == []
