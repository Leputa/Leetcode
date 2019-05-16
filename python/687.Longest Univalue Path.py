# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from queue import Queue

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if root == None:
            return 0
        res = 1
        q = Queue()
        q.put(root)
        while(not q.empty()):
            length = q.qsize()
            for i in range(length):
                tmpNode = q.get()
                if tmpNode.left != None:
                    q.put(tmpNode.left)
                if tmpNode.right != None:
                    q.put(tmpNode.right)
                tmp_res = self.get_length(tmpNode.left, tmpNode.val) + self.get_length(tmpNode.right, tmpNode.val) + 1
                res = max(res, tmp_res)
        return res-1


    def get_length(self, tmpNode, val):
        if tmpNode == None or tmpNode.val != val:
            return 0
        return max(self.get_length(tmpNode.left, val), self.get_length(tmpNode.right, val)) + 1

