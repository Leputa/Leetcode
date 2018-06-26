# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def GetNext(self, pNode):
        # write code here
        tmpNode = pNode
        while(tmpNode.next != None):
            tmpNode = tmpNode.next

        stack = []
        tag = 0 
        while(len(stack)!=0 or tmpNode!=None):
            while(tmpNode!=None):
                stack.append(tmpNode)
                tmpNode = tmpNode.left

            if len(stack)!=0:
                tmpNode = stack.pop()
                if tag == 1:
                    return tmpNode
                if tmpNode == pNode:
                    tag = 1
                tmpNode = tmpNode.right