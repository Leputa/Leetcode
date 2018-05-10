# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot1== None or pRoot2 == None:
            return False
        if pRoot1 == pRoot2:
            return True
        sub = False
        if pRoot1.val == pRoot2.val:
            sub = self.subTree(pRoot1,pRoot2)
        if sub == False and pRoot1.left!=None:
            sub = self.HasSubtree(pRoot1.left, pRoot2)
        if sub == False and pRoot1.right!=None:
            sub = self.HasSubtree(pRoot1.right, pRoot2)
        return sub

    def subTree(self,pRoot1, pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.subTree(pRoot1.left, pRoot2.left) and self.subTree(pRoot1.right, pRoot2.right)