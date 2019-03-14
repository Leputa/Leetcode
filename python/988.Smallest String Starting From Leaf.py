class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        return self.dfs(root, [])
    def dfs(self, root, path):
        if root == None:
            path.reverse()
            return "".join(path)
        path.append(chr(root.val+97))
        if root.left == None and root.right == None:
            path.reverse()
            return "".join(path)
        if root.left != None and root.right != None:
            return min(self.dfs(root.left, path[:]), self.dfs(root.right, path[:]))
        elif root.left != None:
            return self.dfs(root.left, path[:])
        else:
            return self.dfs(root.right, path[:])

