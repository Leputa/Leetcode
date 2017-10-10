class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low=0
        high=len(nums)-1
        mid=(low+high)//2
        # print("high="+str(high)+"   "+"mid="+str(mid))
        # print(nums[mid])
        if(mid+1<=high and nums[mid]==nums[mid+1]):
        	if mid>0:
        		a=self.singleNonDuplicate(nums[:mid])
        		if (a!=None):
        			return a
        	if mid+2<=high:
        		a=self.singleNonDuplicate(nums[mid+2:])
        		if (a!=None):
        			return a
        elif (mid-1>=0 and nums[mid]==nums[mid-1]):
        	if mid-1>0:
        		a=self.singleNonDuplicate(nums[:mid-1])
        		if (a!=None):
        			return a
        	if mid+1<=high:
        		a=self.singleNonDuplicate(nums[mid+1:])
        		if (a!=None):
        			return a
        else:
        	return nums[mid]

print(Solution().singleNonDuplicate( [3,3,7,7,10,11,11]))