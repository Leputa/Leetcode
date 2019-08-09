# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root == None:
            return 0
        stack = []
        ret = 0
        while(len(stack) != 0 or root != None):
            while(root != None):
                diameter = self.get_level(root.left) + self.get_level(root.right) 
                if diameter > ret:
                    ret = diameter
                stack.append(root)
                root = root.left
            if len(stack) != 0:
                root = stack.pop()
                root = root.right
        return ret

    def get_level(self, root):
        if root == None:
            return 0
        return 1 + max(self.get_level(root.left), self.get_level(root.right))
