"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path
such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Constraints:
    The number of nodes in the tree is in the range [0, 5000].
    -1000 <= Node.val <= 1000
    -1000 <= targetSum <= 1000
"""
from collections import deque
from typing import Deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path_sum(root: TreeNode, target_sum: int) -> bool:
    if not root:
        return False

    node_stack: Deque[TreeNode] = deque()
    sum_stack: Deque[int] = deque()

    node_stack.append(root)
    sum_stack.append(target_sum - root.val)

    while node_stack:
        cur_node: TreeNode = node_stack.popleft()
        cur_sum: int = sum_stack.popleft()

        if not cur_node.left and not cur_node.right and cur_sum == 0:
            return True

        if cur_node.left:
            node_stack.append(cur_node.left)
            sum_stack.append(cur_sum - cur_node.left.val)

        if cur_node.right:
            node_stack.append(cur_node.right)
            sum_stack.append(cur_sum - cur_node.right.val)

    return False


if __name__ == '__main__':
    tree = TreeNode(5,
                    TreeNode(4, TreeNode(11, TreeNode(7, None, None), TreeNode(2, None, None)), None),
                    TreeNode(8, TreeNode(13, None, None), TreeNode(4, None, TreeNode(1, None, None))))
    assert has_path_sum(tree, 22) is True

    tree = TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))
    assert has_path_sum(tree, 5) is False

    tree = TreeNode(1, TreeNode(2, None, None), None)
    assert has_path_sum(tree, 0) is False

    tree = TreeNode(1, None, None)
    assert has_path_sum(tree, 1) is True
