# Definition for a binary tree node.
from queue import Queue

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        
    def insert(self, v: int) -> int:
        q = Queue()
        q.put(self.root)
        while(not q.empty()):
            tmpNode = q.get()
            if tmpNode.left != None:
                q.put(tmpNode.left)
            else:
                tmpNode.left = TreeNode(v)
                return tmpNode.val
            if tmpNode.right != None:
                q.put(tmpNode.right)
            else:
                tmpNode.right = TreeNode(v)
                return tmpNode.val
        
    def get_root(self) -> TreeNode:
        return self.root