# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 想用非递归硬是没写出来...还要多练

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        ans = []
        path = []
        if root == None:
            return path
        self.searchPath(root,expectNumber,ans,path)
        return ans

    def searchPath(self,root,expectNumber,ans,path):
        path.append(root.val)
        if root.left == None and root.right == None:
            if sum(path) == expectNumber:
                ans.append(path[:])
        if root.left != None:
            self.searchPath(root.left, expectNumber, ans, path)
        if root.right != None:
            self.searchPath(root.right, expectNumber, ans, path)
        path.pop()







root = TreeNode(3)
a = TreeNode(4)
b = TreeNode(10)
root.left = a
root.right = b

a.left = TreeNode(6)
a.right = TreeNode(5)

b.left = TreeNode(-1)

print(Solution().FindPath(root, 12))
