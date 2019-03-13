class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if self.get_depth(root.left) == self.get_depth(root.right):
            return root
        elif self.get_depth(root.left) > self.get_depth(root.right):
            return self.subtreeWithAllDeepest(root.left)
        else:
            return self.subtreeWithAllDeepest(root.right)
     
    def get_depth(self, root):
        if root == None:
            return 0
        return max(self.get_depth(root.left) + 1, self.get_depth(root.right) + 1)




        