# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def TreeDepth(self, pRoot):
        if pRoot == None:
            return 0
        if pRoot.left == None and pRoot.right == None:
            return 1
        return 1 + max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right))

    def IsBalanced_Solution(self, pRoot):
        if pRoot == None:
            return True

        if abs(self.TreeDepth(pRoot.left) - self.TreeDepth(pRoot.right)) > 1:
            return False

        if pRoot.left != None:
            self.IsBalanced_Solution(pRoot.left)
        if pRoot.right != None:
            self.IsBalanced_Solution(pRoot.right)

        return True


        