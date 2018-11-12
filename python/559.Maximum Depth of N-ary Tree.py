# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root == None:
        	return 0
        if root.children == None:
        	return 1

       	max_depth = 1
        for child in root.children:
        	max_depth = max(max_depth, 1 + self.maxDepth(child))
        return max_depth



        