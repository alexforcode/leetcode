"""
Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Constraints:
    The number of nodes in the tree is in the range [0, 10**4].
    0 <= Node.val <= 10**4
    The height of the n-ary tree is less than or equal to 1000.

Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from typing import List, Optional


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    def __repr__(self):
        return f'TreeNode({self.val}, {self.children})'


def preorder(root: Node) -> Optional[List[int]]:
    if not root:
        return None

    result: List[int] = []
    stack: List[Node] = [root]

    while stack:
        node: Node = stack.pop()
        result.append(node.val)

        if node.children:
            for child in node.children[::-1]:
                stack.append(child)

    return result


def preorder_recursive(root: Node) -> Optional[List[int]]:
    if not root:
        return None

    result: List[int] = []

    def traversal(node: Node) -> None:
        if not node:
            return

        result.append(node.val)

        if node.children:
            for child in node.children:
                traversal(child)

    traversal(root)

    return result


if __name__ == '__main__':
    root = Node(1)
    node2, node3, node4, node5, node6 = Node(2), Node(3), Node(4), Node(5), Node(6)
    node3.children = [node5, node6]
    root.children = [node3, node2, node4]

    assert preorder(root) == [1, 3, 5, 6, 2, 4]
    assert preorder_recursive(root) == [1, 3, 5, 6, 2, 4]
