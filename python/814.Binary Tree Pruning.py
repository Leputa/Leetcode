class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
        	return root
    	if root.left != None:
    		self.prune(root.left, root, "left")
    	if root.right != None:
    		self.prune(root.right, root, "right")
    	return root

    def prune(self, node, parentNode, direct):
    	if node.val == 1:
	    	if node.left != None:
	    		self.prune(node.left, node, "left")
	    	if node.right != None:
	    		self.prune(node.right, node, "right")
	    	return

    	if node.val == 0:
    		if node.left == None and node.right == None:
	    		if direct == 'left':
	    			parentNode.left = None
	    		if direct == 'right':
	    			parentNode.right = None
	    		return

	    	if node.left != None:
	    		self.prune(node.left, node, "left")
	    	if node.right != None:
	    		self.prune(node.right, node, "right")

	    	if node.left == None and node.right == None:
	    		if direct == 'left':
	    			parentNode.left = None
	    		if direct == 'right':
	    			parentNode.right = None


        