# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import Queue

class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        ret = []
        if root == None:
            return ret

        q = Queue.Queue()
        q.put(root)

        while(not q.empty()):
            tmpNode = q.get()
            ret.append(tmpNode.val)
            if tmpNode.left != None:
                q.put(tmpNode.left)
            if tmpNode.right != None:
                q.put(tmpNode.right)
        return ret


print(Solution().PrintFromTopToBottom(TreeNode(1)))


