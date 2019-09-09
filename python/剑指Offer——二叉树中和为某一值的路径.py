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
        ret = []
        if root == None:
            return ret
        self.pathSum(root, expectNumber, 0, [], ret)
        return sorted(ret, key = lambda info: len(info), reverse=True)

    def pathSum(self, tmpNode, expectNumber, tmpSum, tmpList, ret):
        tmpList.append(tmpNode.val)
        tmpSum += tmpNode.val

        if tmpNode.left == None and tmpNode.right == None:
            if tmpSum == expectNumber:
                ret.append(tmpList[:])
        else:
            if tmpNode.left != None:
                self.pathSum(tmpNode.left, expectNumber, tmpSum, tmpList, ret)
            if tmpNode.right != None:
                self.pathSum(tmpNode.right, expectNumber, tmpSum, tmpList, ret)

        tmpList.pop()
        tmpSum -= tmpNode.val








root = TreeNode(3)
a = TreeNode(4)
b = TreeNode(10)
root.left = a
root.right = b

a.left = TreeNode(6)
a.right = TreeNode(5)

b.left = TreeNode(-1)

print(Solution().FindPath(root, 12))
