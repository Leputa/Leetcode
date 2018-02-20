class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=len(nums)-1
        if(nums[left]<nums[right]):
        	return nums[left]
        while(right-left>1):
        	mid=(left+right)//2
        	if(nums[mid]<nums[0]):
        		right=mid
        	else:
        		left=mid
        return min(nums[left],nums[right])

