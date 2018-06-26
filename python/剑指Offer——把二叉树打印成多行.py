# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import Queue

class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        ans = []

        if pRoot == None:
            return ans

        q = Queue.Queue()
        q.put(pRoot)


        while (not q.empty()):
            tmpList = []
            cnt = q.qsize()

            for i in range(cnt):
                tmpNode = q.get()
                tmpList.append(tmpNode.val)
                if tmpNode.left != None:
                    q.put(tmpNode.left)
                if tmpNode.right != None:
                    q.put(tmpNode.right)
            
            ans.append(tmpList)

        return ans


