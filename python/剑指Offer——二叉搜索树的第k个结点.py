# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        tmpNode = pRoot
        stack = []
        cnt = 0

        while(tmpNode!=None or len(stack)!=0):
            while(tmpNode!=None):
                stack.append(tmpNode)
                tmpNode = tmpNode.left
            if len(stack)!=0:
                tmpNode = stack.pop()
                cnt += 1
                if cnt == k:
                    return tmpNode
                tmpNode = tmpNode.right