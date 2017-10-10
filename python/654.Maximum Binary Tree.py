#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums)==0:
        	return None
        i=self.findMax(nums)
        root=TreeNode(nums[i])
        if i!=0:
        	root.left=self.constructMaximumBinaryTree(nums[:i])
        if i!=len(nums)-1:
        	root.right=self.constructMaximumBinaryTree(nums[i+1:])
        return root

    def findMax(self,nums):
    	max=-99999999999
    	tag=0
    	for i in range(len(nums)):
    		if nums[i]>max:
    			max=nums[i]
    			tag=i
    	return tag

Solution().constructMaximumBinaryTree([3,2,1,6,0,5])