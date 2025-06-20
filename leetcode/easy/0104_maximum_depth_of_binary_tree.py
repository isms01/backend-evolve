# Leetcode Problem: 104. Maximum Depth of Binary Tree
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:  # LeetCode #104: Maximum Depth of Binary Tree
    # https://leetcode.com/problems/maximum-depth-of-binary-tree/
    # Given the root of a binary tree, return its maximum depth.
    # A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
