# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import queue

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        q = queue.Queue()
        q.put(root)
        full_size = 1
        is_end = False
        while(not q.empty()):
            size = q.qsize()
            if size == full_size:
                is_end = False
            else:
                is_end = True
            full_size *= 2
            pre_full = True
            while(size > 0):
                tmpNode = q.get()
                if tmpNode.left != None:
                    if is_end or not pre_full:
                        return False
                    q.put(tmpNode.left)
                else:
                    pre_full = False
                if tmpNode.right != None:
                    if is_end or not pre_full:
                        return False
                    q.put(tmpNode.right)
                else:
                    pre_full = False
                size -= 1
        return True
        