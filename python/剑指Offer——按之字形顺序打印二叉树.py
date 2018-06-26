class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import queue

class Solution:
    def Print(self, pRoot):
        # write code here
        ans = []
        tag = 0

        if pRoot == None:
            return ans

        q = queue.Queue()
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
            
            if tag%2 == 0:
                ans.append(tmpList)
            else:
                ans.append(tmpList[::-1])
            tag += 1
        return ans

