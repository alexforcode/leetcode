"""
Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).

Constraints:
    The number of nodes in the tree is in the range [0, 2000].
    -1000 <= Node.val <= 1000
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


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
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

    return result


if __name__ == '__main__':
    tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert level_order(tree) == [[3], [9, 20], [15, 7]]

    tree = TreeNode(1)
    assert level_order(tree) == [[1]]

    assert level_order(None) == []
