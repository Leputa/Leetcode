# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.index = -1

    def Serialize(self, root):
        # write code here
        s = ''
        if root == None:
            s += '#,'
            return s
        s = s + str(root.val) + ','
        s += self.Serialize(root.left)
        s += self.Serialize(root.right)
        return s

    def Deserialize(self, s):
        # write code here
        self.index += 1
        if self.index >= len(s):
            return None
        sList = s.split(",")
        pNode = None
        if sList[self.index]!='#':
            pNode = TreeNode(int(sList[self.index]))
            pNode.left = self.Deserialize(s)
            pNode.right = self.Deserialize(s)
        return pNode