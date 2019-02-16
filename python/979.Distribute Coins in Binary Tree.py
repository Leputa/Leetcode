# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.moves = 0
    def distributeCoins(self, root: 'TreeNode') -> 'int':
        self.dfs(root)
        return self.moves
    def dfs(self, root):
        if root == None:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.moves += abs(left) + abs(right)  # eg.左子树移动到根节点，根节点移动到右子树
        return root.val + left + right - 1

        
