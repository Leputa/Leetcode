# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        stack = []
        maxSum = -float("inf")
        tmpNode = root
        while(tmpNode != None or len(stack) != 0):
            while(tmpNode != None):
                stack.append(tmpNode)
                maxSum = max(tmpNode.val + max(0, self.getMaxPathSum(tmpNode.left)) + max(0, self.getMaxPathSum(tmpNode.right)), maxSum)
                tmpNode = tmpNode.left
            if len(stack) != 0:
                tmpNode = stack.pop()
                tmpNode = tmpNode.right
        return maxSum

    def getMaxPathSum(self, root):
        if root == None:
            return 0
        return root.val + max(max(0, self.getMaxPathSum(root.left)), max(0, self.getMaxPathSum(root.right)))