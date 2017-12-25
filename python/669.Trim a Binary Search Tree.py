# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        while (root.val<L):
        	root=root.right
        while (root.val>R):
        	root=root.left
        if (root.val==L):
        	root.left=None
        if (root.val==R):
        	root.right=None
        while(root.left!=None and root.left.val<L):
        	root.left=root.left.right
        while(root.right!=None and root.right.val>R):
        	root.right=root.right.left
        if(root.left!=None):
        	root.left=self.trimBST(root.left,L,R)
        if(root.right!=None):
        	root.right=self.trimBST(root.right,L,R)
        return root
