class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        
        mul=1
        for i in nums:
        	ans.append(mul)
        	mul*=i
        
        mul=1
        for i in range(len(nums)-1,-1,-1):
        	ans[i]*=mul
        	mul*=nums[i]
        	
        return ans

