# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        我猜这道题是按照先序遍历往右边放
        """
        stack = []
        tmpNode = root
        while(len(stack) != 0 or tmpNode != None):
            while(tmpNode != None):
                stack.append(tmpNode)
                preNode = tmpNode
                tmpNode = tmpNode.left
            if len(stack) != 0:
                tmpNode = stack.pop()
                nextNode = tmpNode.right
                if tmpNode.right != None:
                    tmpNode.right = None
                    preNode.left = nextNode
                tmpNode = nextNode
        tmpNode = root
        while(tmpNode != None):
            nextNode = tmpNode.left
            tmpNode.left = None
            tmpNode.right = nextNode
            tmpNode = nextNode
        