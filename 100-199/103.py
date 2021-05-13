"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
(i.e., from left to right, then right to left for the next level and alternate between).

Constraints:
    The number of nodes in the tree is in the range [0, 2000].
    -100 <= Node.val <= 100
"""
from collections import deque
from typing import Deque, List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'TreeNode({self.val}, {self.left}, {self.right})'


def zigzag_level_order(root: Optional[TreeNode]) -> List[List[int]]:
    result: List[List[int]] = []

    if not root:
        return result

    queue: Deque[TreeNode] = deque([root])
    count: int = 0

    while queue:
        result.append([])

        for _ in range(len(queue)):
            node: TreeNode = queue.popleft()
            result[count].append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        count += 1

    for idx in range(len(result)):
        if idx % 2 != 0:
            result[idx] = result[idx][::-1]

    return result


if __name__ == '__main__':
    tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert zigzag_level_order(tree) == [[3], [20, 9], [15, 7]]

    tree = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, None, TreeNode(5)))
    assert zigzag_level_order(tree) == [[1], [3, 2], [4, 5]]

    tree = TreeNode(1)
    assert zigzag_level_order(tree) == [[1]]

    assert zigzag_level_order(None) == []