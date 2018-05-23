# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree == None:
        	return None
        	
        head = TreeNode(None)
        preNode = head
        tmpNode = pRootOfTree

        stack = []

        while (len(stack)!=0 or tmpNode!=None):
        	while(tmpNode != None):
        		stack.append(tmpNode)
        		tmpNode = tmpNode.left
        	if len(stack)!=0:
        		tmpNode = stack.pop()
        		preNode.right = tmpNode
        		tmpNode.left = preNode
        		preNode = tmpNode
        		tmpNode = tmpNode.right
        head = head.right
        head.left = None
        return head


