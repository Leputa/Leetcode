# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root == None:
            return 0
        ret = []
        self.get_path(root, [], ret)
        return sum(ret)
    def get_path(self, tmpNode, tmpList, ret):
        tmpList.append(tmpNode.val)
        if tmpNode.left == None and tmpNode.right == None:
            tmp = 0
            for i in range(len(tmpList)):
                tmp += tmpList[i] * 10 ** (len(tmpList) - i - 1) 
            ret.append(tmp)
            return 
        if tmpNode.left != None:
            self.get_path(tmpNode.left, tmpList, ret)
            tmpList.pop()
        if tmpNode.right != None:
            self.get_path(tmpNode.right, tmpList, ret)
            tmpList.pop()