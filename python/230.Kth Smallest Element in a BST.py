# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        leftCount=self.getNodeCount(root.left)
        if (leftCount==k-1):
        	return root.val
        if (leftCount>k-1):
        	return self.kthSmallest(root.left,k)
        else:
        	return self.kthSmallest(root.right,k-(leftCount+1))

    def getNodeCount(self,root):
    	count=0
    	stack=[]
    	tmp=root
    	while(len(stack)!=0 or tmp!=None):
    		while(tmp!=None):
    			stack.append(tmp)
    			tmp=tmp.left
    		if(len(stack)!=0):
    			tmp=stack.pop()
    			count+=1
    			tmp=tmp.right
    	return count





