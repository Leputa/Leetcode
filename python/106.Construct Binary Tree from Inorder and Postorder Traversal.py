class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        root = TreeNode(postorder[len(postorder) - 1])
        idx = inorder.index(postorder[len(postorder) - 1])
        root.left = self.buildTree(inorder[:idx], postorder[:idx])
        root.right = self.buildTree(inorder[idx+1:], postorder[idx:-1])
        return root