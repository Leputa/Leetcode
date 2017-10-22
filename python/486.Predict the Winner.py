class Solution(object):
	max=0
	tag=0
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)):
        	if(nums[i]>self.max):
        		self.max=nums[i]
        		tag=i
