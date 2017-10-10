class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1=-9999999
        max2=-9999999
        max3=-9999999
        for i in range(len(nums)):
        	if nums[i]>max1:
        		max1=nums[i]
        		tag1=i
        for j in range(len(nums)):
        	if nums[j]<max1 and nums[j]>max2:
        		max2=nums[j]
        		tag2=j
        for k in range(len(nums)):
        	if nums[k]<max2 :
        		if nums[k]>max3:
        			max3=nums[k]
       	if max3==-9999999:
       		return max1
        return max3




