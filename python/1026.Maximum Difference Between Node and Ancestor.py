# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from queue import Queue

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        minDiff = 0