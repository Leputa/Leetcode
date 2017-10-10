class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        copy=nums[:]
        copy.sort()

        head=0
        tail=len(nums)-1
        tag=0
        for i in range (len(nums)):
        	if(nums[i]!=copy[i]):
        		head=i
        		tag=1
        		break
        if(tag==0):
        	return 0
        for j in range(len(nums)-1,-1,-1):
        	if(nums[j]!=copy[j]):
        		tail=j
        		break
        return tail-head+1


