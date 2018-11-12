
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        ret = []
        self.postOrder(root, ret)
        return ret

    def postOrder(self, root, ret):
    	if root == None:
    		return
    	if root.children == None:
    		ret.append(root.val)
    		return

    	for child in root.children:
    		self.postOrder(child, ret)
    	ret.append(root.val)
