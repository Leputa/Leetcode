# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        pre_val = -float("inf")
        tmpNode = root
        while(tmpNode != None or len(stack)) != 0:
            while tmpNode != None:
                stack.append(tmpNode)
                tmpNode = tmpNode.left
            if len(stack) != 0:
                tmpNode = stack.pop()
                if tmpNode.val <= pre_val:
                    return False
                pre_val = tmpNode.val
                tmpNode = tmpNode.right
        return True
