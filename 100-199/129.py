"""
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number:
    - For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.

Return the total sum of all root-to-leaf numbers.

A leaf node is a node with no children.

Constraints:
    The number of nodes in the tree is in the range [1, 1000].
    0 <= Node.val <= 9
    The depth of the tree will not exceed 10.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sum_numbers(root: TreeNode) -> int:
    total: int = 0

    def add_to_total(node: TreeNode, cur_sum: int) -> None:
        if not node:
            return

        cur_sum = cur_sum * 10 + node.val

        if not node.left and not node.right:
            nonlocal total
            total += cur_sum

        add_to_total(node.left, cur_sum)
        add_to_total(node.right, cur_sum)

    add_to_total(root, 0)

    return total


if __name__ == '__main__':
    tree = TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))
    assert sum_numbers(tree) == 25

    tree = TreeNode(4, TreeNode(9, TreeNode(5, None, None), TreeNode(1, None, None)), TreeNode(0, None, None))
    assert sum_numbers(tree) == 1026
