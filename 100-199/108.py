"""
Given an integer array nums where the elements are sorted in ascending order,
convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which
the depth of the two subtrees of every node never differs by more than one.

Constraints:
    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums is sorted in a strictly increasing order.
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'TreeNode({self.val}, {self.left}, {self.right})'


def sorted_array_to_bst(nums: List[int]) -> TreeNode:

    def get_tree_from_array(start: int, end: int) -> Optional[TreeNode]:
        if start > end:
            return

        mid: int = start + (end - start) // 2
        left: Optional[TreeNode] = get_tree_from_array(start, mid - 1)
        right: Optional[TreeNode] = get_tree_from_array(mid + 1, end)

        return TreeNode(nums[mid], left, right)

    return get_tree_from_array(0, len(nums)-1)


def sorted_array_to_bst_2(nums: List[int]) -> Optional[TreeNode]:
    if not nums:
        return

    if len(nums) == 1:
        return TreeNode(nums[0], None, None)

    mid: int = len(nums) // 2
    left: Optional[TreeNode] = sorted_array_to_bst(nums[:mid])
    right: Optional[TreeNode] = sorted_array_to_bst(nums[mid+1:])

    return TreeNode(nums[mid], left, right)


if __name__ == '__main__':
    lst = [-10, -3, 0, 5, 9]
    print(sorted_array_to_bst(lst))

    lst = [1, 3]
    print(sorted_array_to_bst(lst))

    lst = [-10, -3, 0, 5, 9]
    print(sorted_array_to_bst_2(lst))

    lst = [1, 3]
    print(sorted_array_to_bst_2(lst))
