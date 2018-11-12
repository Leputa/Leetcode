# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        new_root = None
        stack = []
        tmpNode = root
        while(tmpNode != None or len(stack)!=0):
        	while(tmpNode != None):
        		stack.append(tmpNode)
        		tmpNode = tmpNode.left
        	if len(stack) != 0:
        		tmpNode = stack.pop()
        		if new_root == None:
        			new_root = TreeNode(tmpNode.val)
        			new_tmpNode = new_root
        		else:
        			new_tmpNode.right = TreeNode(tmpNode.val)
        			new_tmpNode = new_tmpNode.right
        		tmpNode = tmpNode.right
        return new_root

