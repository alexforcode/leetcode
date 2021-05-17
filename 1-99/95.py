"""
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique
values from 1 to n. Return the answer in any order.

Constraints:
    1 <= n <= 8
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'TreeNode({self.val}, {self.left}, {self.right})'


def generate_trees(n: int) -> List[TreeNode]:
    def generate(left: int, right: int) -> List[Optional[TreeNode]]:
        if left > right:
            return [None]

        results: List[TreeNode] = []

        for idx in range(left, right+1):
            left_trees: List[TreeNode] = generate(left, idx-1)
            right_trees: List[TreeNode] = generate(idx+1, right)

            for l_tree in left_trees:
                for r_tree in right_trees:
                    root: TreeNode = TreeNode(idx)
                    root.left = l_tree
                    root.right = r_tree
                    results.append(root)

        return results

    return generate(1, n)


if __name__ == '__main__':
    print(generate_trees(3))
    print(generate_trees(1))
