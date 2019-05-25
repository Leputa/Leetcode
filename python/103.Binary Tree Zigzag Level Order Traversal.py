# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from queue import Queue

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ret = []
        if root == None:
            return ret 
        q = Queue()
        q.put(root)
        is_reverse = 0
        while(not q.empty()):
            length = q.qsize()
            tmpList = []
            for i in range(length):
                tmpNode = q.get()
                if tmpNode.left != None:
                    q.put(tmpNode.left)
                if tmpNode.right != None:
                    q.put(tmpNode.right)
                tmpList.append(tmpNode.val)
            if is_reverse % 2 == 0:
                ret.append(tmpList)
            else:
                ret.append(tmpList[::-1])
            is_reverse = (is_reverse + 1) %2
        return ret
