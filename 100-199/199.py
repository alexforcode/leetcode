"""
Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

Constraints:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100
"""
from collections import deque
from typing import Deque, List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root: Optional[TreeNode]) -> List[int]:
    result: List[int] = []

    if not root:
        return result

    queue: Deque = deque([root])

    while queue:
        for idx in range(len(queue)):
            node: TreeNode = queue.popleft()

            if idx == 0:
                result.append(node.val)

            if node.right:
                queue.append(node.right)

            if node.left:
                queue.append(node.left)

    return result


if __name__ == '__main__':
    tree = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    assert right_side_view(tree) == [1, 3, 4]

    tree = TreeNode(1, TreeNode(2, None), TreeNode(3, TreeNode(4, None, TreeNode(5))))
    assert right_side_view(tree) == [1, 3, 4, 5]

    tree = TreeNode(1, None, TreeNode(3))
    assert right_side_view(tree) == [1, 3]

    assert right_side_view(None) == []
