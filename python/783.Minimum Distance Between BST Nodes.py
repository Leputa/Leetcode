class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        minDiff = float("inf")
        stack = []
        tmpNode = root 
        pre_val = None
        while (tmpNode != None or len(stack) != 0):
            while(tmpNode != None):
                stack.append(tmpNode)
                tmpNode = tmpNode.left
            if len(stack) != 0:
                tmpNode = stack.pop()
                if pre_val != None:
                    minDiff = min(tmpNode.val - pre_val, minDiff)
                pre_val = tmpNode.val
                tmpNode = tmpNode.right
        return minDiff
