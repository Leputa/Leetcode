
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        ret = []
        self.preOrder(root, ret)
        return ret

    def preOrder(self, root, ret):
    	if root == None:
    		return
    	ret.append(root.val)

    	for child in root.children:
    		self.preOrder(child, ret)
        