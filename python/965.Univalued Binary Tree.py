# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        val = root.val
        stack = []
        tmpNode = root
        while(tmpNode != None or len(stack) != 0):
            while tmpNode != None:
                if tmpNode.val != val:
                    return False
                stack.append(tmpNode)
                tmpNode = tmpNode.left

            if len(stack) != 0:
                tmpNode = stack.pop()
                tmpNode = tmpNode.right

        return True