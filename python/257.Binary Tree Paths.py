# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import copy

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """ 
        ret = []
        if root == None:
        	return ret
        self.rec(root, ret, "")
        return ret

    def rec(self, root, ret, s):
    	if root.left == None and root.right == None:
    		s += str(root.val)
    		ret.append(copy.deepcopy(s))
    		return
    	
    	s += str(root.val) + "->"
    	if root.left != None:
    		self.rec(root.left, ret, s)
    	if root.right != None:
    		self.rec(root.right, ret, s)


