from queue import Queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root.val == x or root.val == y:
            return False
        q = Queue()
        q.put(root)
        x_parent_node, y_parent_node = None, None
        x_depth, y_depth = 0, 0
        depth = 0
        while(not q.empty()):
            if x_depth != 0 or y_depth != 0:
                if x_depth != y_depth:
                    return False
                if x_parent_node == y_parent_node:
                    return False
                return True

            length = q.qsize()
            for i in range(length):
                tmpNode = q.get()
                if tmpNode.left != None:
                    if tmpNode.left.val == x:
                        x_parent_node = tmpNode
                        x_depth = depth + 1
                    if tmpNode.left.val == y:
                        y_parent_node = tmpNode
                        y_depth = depth + 1
                    q.put(tmpNode.left)
                if tmpNode.right != None:
                    if tmpNode.right.val == x:
                        x_parent_node = tmpNode
                        x_depth = depth + 1
                    if tmpNode.right.val == y:
                        y_parent_node = tmpNode
                        y_depth = depth + 1
                    q.put(tmpNode.right)
        return False

